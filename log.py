import sys
from datetime import datetime

DEBUG=1
LOGFILE="test.log"

def _log(*args, **kwargs):
    print(*args, **kwargs)
    if 'file' in kwargs:
        file = kwargs['file']
        if not file in (sys.stdout, sys.stderr):
            del kwargs['file']
            print(*args, file=sys.stdout, **kwargs)

def log(*args, **kwargs):
    if DEBUG:
        try:
            with open(LOGFILE, "a") as f:
                _log("[{:%d%b%Y %H:%M:%S.%f}] ".format(datetime.now()), end="", file=f)
                _log(*args, file=f, **kwargs)
        except:
            pass
