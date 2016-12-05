#!/usr/bin/env python
import pickle
import logging
import time
import os.path
from pageable import Menu, Library
from utility import write_pid_file, remove_pid_file
import buttons_config
import config_loader
from setup_logs import setup_logs

import argparser

log = logging.getLogger(__name__)

class UI():
    """This is the UI class which is a framework to build a UI for the braille
    machine

    The UI can be configured to either use the :class:`.Pi` or
    :class:`.Emulated` driver class, or both at the same time.

    :param driver: the :class:`driver` object that abstracts the hardware
    """

    state_file = 'ui.pkl'

    def __init__(self, driver, config):
        self.driver = driver
        self.dimensions = (self.driver.chars, self.driver.rows)
        self.last_data = []

        # load the books into the library
        self.library = Library(self.dimensions, config, self)
        self.menu = Menu(self.dimensions, config, self)

        # the screen is the object that is shown and operated on by the
        # buttons, it will be either the library or the book
        self.load_state()
        if self.state['mode'] == 'book':
            log.info("starting in book mode")
            try:
                self.book = self.library.get_book(self.state['book_num'])
                self.screen = self.book
            except (IndexError, OSError, IOError):
                #TODO make sure crap like this doesn't happen
                #book doesn't exist, reset the state
                self.state = {}
                self.state['mode'] = 'library'
                self.state['book_num'] = 0
                self.screen = self.library
            self.show()
        elif self.state['mode'] == 'library':
            log.info("starting in library mode")
            self.screen = self.library
            self.show()
        elif self.state['mode'] == 'menu':
            log.info("starting in menu mode")
            self.screen = self.menu
            self.show()

    def finish(self):
        self.is_running = False
        # next time we start, start in book mode
        self.state['mode'] = 'book'
        self.save_state()
        self.driver.clear_page()
        os.system("sudo shutdown -h now")

    def save_state(self):
        with open(UI.state_file, 'w') as fh:
            pickle.dump(self.state, fh)

    def load_state(self):
        try:
            with open(UI.state_file) as fh:
                self.state = pickle.load(fh)
        except IOError:
            log.debug("no state file; initialising")
            self.state = {}
            self.state['mode'] = 'library'
            self.state['book_num'] = 0

    def despatch(self, button_type, button_id):
        log.debug(buttons_config.conf[self.state['mode']][button_type])
        log.debug(button_type)
        # fetch the config for the button
        try:
            config = buttons_config.conf[self.state['mode']][button_type][button_id]
        except KeyError:
            # try get the default
            try:
                config = buttons_config.conf['default'][button_type][button_id]
            except KeyError:
                # otherwise return False
                log.debug("nothing defined for that button")
                return False

        log.debug(config)
        # to call the method we need the object
        if config['obj'] == 'ui':
            obj = self
        elif config['obj'] == 'screen':
            obj = self.screen

        # get the method
        try:
            method = getattr(obj, config['method'])
        except AttributeError:
            log.warning("object %s has no method %s to call"
                    % (obj, config['method']))
            return False

        # we're going to do something, so make an OK sound
        self.driver.send_ok_sound()

        # call method, maybe with args
        if config.has_key('args'):
            log.info("despatching %s->%s(%s)"
                    % (config['obj'], config['method'], config['args']))
            method(config['args'])
        else:
            log.info("despatching %s->%s()"
                    % (config['obj'], config['method']))
            method()

        # update the screen
        self.show()
        return True

    def start(self):
        '''
        start the UI running, runs the UI until the driver returns an error or something sets is_running to False
        '''
        self.is_running = True
        while self.driver.is_ok() and self.is_running:
            # fetch all buttons (a fetch resets button register)
            buttons = self.driver.get_buttons()
            for button_id in buttons:
                if buttons[button_id] != False:
                    button_type = buttons[button_id]
                    # if a button is pressed, deal with it
                    result = self.despatch(button_type, button_id)
                    if result is False:
                        self.driver.send_error_sound()
            time.sleep(0.1)
        else:
            log.info("UI main loop ending")

    def reset_display(self):
        self.driver.reset_display()
        self.driver.set_braille(self.last_data)
        log.info("display reset & updated")

    def library_mode(self):
        log.info("library mode")
        self.state['mode'] = 'library'
        self.screen = self.library
        self.library.add_new_books()

    def menu_mode(self):
        log.info("menu mode")
        self.state['mode'] = 'menu'
        self.screen = self.menu

    def load_book(self, number):
        '''
        load a book into self.book, set the screen to point at the book
        update the screen. If no book, don't set and update the screen
        '''
        try:
            self.book = self.library.get_book(number)
            self.screen = self.book
            self.state['book_num'] = number
            self.state['mode'] = 'book'
        except (IndexError, OSError, IOError):
            log.warning("no book at slot %d" % number)
            self.driver.send_error_sound()

    def show(self):
        '''
        shows the current screen object's braille, but only if it's changed
        from last time
        '''
        data = self.screen.show()

        if data == self.last_data:
            log.info("not updating display with identical data")
            self.driver.send_error_sound()
            return

        self.driver.set_braille(data)
        self.last_data = data
        self.save_state()
        log.info("display updated")

if __name__ == '__main__':

    args = argparser.parser.parse_args()

    config = config_loader.load()

    log = setup_logs(config, args.loglevel)

    if not buttons_config.test_config():
        log.exception("bad button config")
        exit(1)

    write_pid_file()

    try:
        if args.emulated and not args.both:
            log.info("running with emulated hardware")
            from driver_emulated import Emulated
            with Emulated(delay=args.delay, display_text=args.text) as driver:
                ui = UI(driver, config)
                ui.start()
        elif args.emulated and args.both:
            log.info("running with both emulated and real hardware on port %s" % args.tty)
            from driver_both import DriverBoth
            with DriverBoth(port=args.tty, pi_buttons=args.pi_buttons,
                    delay=args.delay, display_text=args.text) as driver:
                ui = UI(driver, config)
                ui.start()
        else:
            # have to do this because couldn't find a way to set a default inside a section
            if config.has_option('comms', 'timeout'):
                timeout = float(config.get('comms', 'timeout'))
            else:
                timeout = 60
            log.info("running with real hardware on port %s, timeout %s" % (args.tty, timeout))
            from driver_pi import Pi
            with Pi(port=args.tty, pi_buttons=args.pi_buttons, timeout=timeout) as driver:
                ui = UI(driver, config)
                ui.start()
    except Exception as e:
        log.exception(e)
    finally:
        remove_pid_file()
