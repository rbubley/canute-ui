import argparse
import logging

parser = argparse.ArgumentParser(description="Canute UI")

parser.add_argument(
    '--pi-buttons',
    action='store_const',
    dest='pi_buttons',
    const=True,
    default=False,
    help="use evdev to process button presses more directly"
    + "(recommended for embedded usage on the Raspberry Pi)"
)
parser.add_argument(
    '--debug',
    action='store_const',
    dest='loglevel',
    const=logging.DEBUG,
    default=logging.INFO,
    help="debugging content"
)
parser.add_argument(
    '--text',
    action='store_const',
    dest='text',
    const=True,
    help="show text instead of braille"
)
parser.add_argument(
    '--tty',
    action='store',
    dest='tty',
    help="serial port for the display and button board",
    default='/dev/ttyACM0'
)
parser.add_argument(
    '--delay',
    action='store',
    dest='delay',
    help="simulate mechanical delay in milliseconds in the emulator",
    default=0,
    type=int
)
parser.add_argument(
    '--disable-emulator',
    action='store_const',
    dest='emulated',
    const=False,
    default=True,
    help="do not run the graphical emulator, run with real hardware"
)
parser.add_argument(
    '--both',
    action='store_const',
    dest='both',
    const=True,
    default=False,
    help="run both the emulator and the real hardware at the same time"
)
