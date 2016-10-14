import os
import pydux
from pydux.extend import extend
from pydux.create_store import create_store
import functools
import time

import logging
log = logging.getLogger(__name__)

from bookfile_list import BookFile_List
import utility
import argparser
import buttons_config
import config_loader
from ui import setup_logs

HEIGHT = 9
WIDTH = 40

initial_state = {
    'location'        : 'library',
    'library'         : {'data': [], 'page': 0},
    'books'           : [],
    'button_bindings' : {}
}

def update(state, action = None):
    if action['type'] == 'GO_TO_BOOK':
        try:
            location = state['books'][action['value']]
        except:
            log.warning('no book at {}'.format(action['value']))
            return state
        return extend(state, {'location': location})
    elif action['type'] == 'SET_BOOKS':
        books = []
        for filename in action['value']:
            books.append({'data': BookFile_List(filename, [WIDTH, HEIGHT]), 'page': 0})
        library = {'data': map(get_title, books), 'page': 0}
        return extend(state, {'books': books, 'library': library})
    return state

store = create_store(update, initial_state)

def get_title(book):
    return utility.alphas_to_pin_nums(os.path.basename(book['data'].filename))


def render(driver, state):
    if state['location'] == 'library':
        render_location(driver, state['library']['page'], state['library']['data'])


def render_location(driver, page, data):
    n = page * HEIGHT
    lines = data[n : n + HEIGHT]
    lines = map(functools.partial(utility.pad_line, WIDTH), lines)
    log.debug(lines)
    driver.set_braille(utility.flatten(lines))


def handle_changes(driver):
    state = store['get_state']()
    log.debug(state)
    render(driver, state)


if __name__ == '__main__':
    args = argparser.parser.parse_args()

    config = config_loader.load()
    library_dir = config.get('files', 'library_dir')
    log = setup_logs(config, args.loglevel)

    from driver_emulated import Emulated
    with Emulated(delay=args.delay, display_text=args.text) as driver:
        state = initial_state
        render(driver, state)
        quit = False
        store['subscribe'](functools.partial(handle_changes, driver))
        file_names = utility.find_files(library_dir, '.canute')
        store['dispatch']({'type':'SET_BOOKS', 'value': file_names})
        while not quit:
            time.sleep(1)

