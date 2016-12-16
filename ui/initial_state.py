from frozendict import frozendict
from functools import partial
import pickle
import logging
log = logging.getLogger(__name__)

import utility
import menu


INITIAL_WIDTH = 40
INITIAL_HEIGHT = 9

initial_state = frozendict({
    'location' : 'library',
    'library'  : frozendict({'data': tuple(), 'page': 0}),
    'menu'     : frozendict({
        'data': tuple(map(partial(utility.pad_line, INITIAL_WIDTH), menu.menu_titles_braille)),
        'page': 0
    }),
    'books'             : tuple(),
    'replacing_library' : False,
    'backing_up_log'    : False,
    'shutting_down'     : False,
    'dimensions'        : frozendict({'width': INITIAL_WIDTH, 'height': INITIAL_HEIGHT}),
    'display_buffer'    : tuple([frozendict({'set': True, 'data': tuple()})]) * INITIAL_HEIGHT
})

state_file = 'state.pkl'

def read():
    log.debug('reading initial state')
    try:
        with open(state_file) as fh:
            state = pickle.load(fh)
            return state
    except:
        log.debug('error reading state file, using hard-coded initial state: {}'.format(initial_state))
        return initial_state


def write(state):
    log.debug('writing state file')
    write_state                      = dict(state)
    write_state['library']           = state['library'].copy(page = 0)
    location = state['location']
    if location == 'menu':
        location = 'library'
    write_state['location']          = location
    write_state['backing_up_log']    = False
    write_state['replacing_library'] = False
    write_state['shutting_down']     = False
    with open(state_file, 'w') as fh:
        pickle.dump(frozendict(write_state), fh)
