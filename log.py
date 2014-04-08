#!/usr/bin/env python3
"""
Basic logging functions.

 Module Variables
==================
DEBUG - Set to 0 to disable logging and to some other number to renable it.
LOGFILE - Defaults to <program-name>.log. But can be changed anytime.
"""

import sys
from datetime import datetime

DEBUG=1
LOGFILE="%s.log" % sys.argv[0]

def _log(*args, **kwargs):
    print(*args, **kwargs)
    if 'file' in kwargs:
        file = kwargs['file']
        if not file in (sys.stdout, sys.stderr):
            del kwargs['file']
            print(*args, file=sys.stdout, **kwargs)

def log(*args, **kwargs):
    """
    Log arguments to LOGFILE and to stdout. The logging is done
    using the python print function. Log() has the same features
    as print.
    """
    if DEBUG:
        try:
            with open(LOGFILE, "a") as f:
                _log("[{:%d%b%Y %H:%M:%S.%f}] ".format(datetime.now()), end="", file=f)
                _log(*args, file=f, **kwargs)
        except:
            pass

#Test module functionality from the command line
if __name__ == '__main__':
    log(*sys.argv[1:])