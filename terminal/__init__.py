#!/usr/bin/env python3

import curses.ascii as ascii

from .keys import keySubstitutions
from .terminal import sanitize_key



#Test module functionality from the command line
if __name__ == '__main__':
    print(sanitize_key(sys.argv[1]))