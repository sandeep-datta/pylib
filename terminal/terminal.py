import curses.ascii
from ..str import remove_prefix

def sanitize_key(key):
    if len(key) == 1 and curses.ascii.isctrl(key):
        key = curses.ascii.unctrl(key)

    if key.startswith("^"):
        key = "Ctrl+"+key[1]
    elif key.startswith("KEY_"):
        key = remove_prefix(key, "KEY_")

    return key