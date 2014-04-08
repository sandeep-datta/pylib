#!/usr/bin/env python3
"""
Run external commands
"""
import sys
import subprocess

#Usage:
#
def run(args):
    """
    Run an external command and capture its output. Uses subprocess.check_output
    internally but decodes the byte stream into unicode (using sys.stdout.encoding).
    Any leading and trailing white space from the output is trimmed.

    Examples:
        run(['ls'])
        run(['ls', '-lh'])
        print(run(['ls', '-lh']))
    """
    encoding = sys.stdout.encoding.lower()
    encoding = encoding.replace("-", "_")
    retVal = subprocess.check_output(args).decode(encoding, 'replace').strip()
    return retVal


#Test module functionality from the command line
if __name__ == '__main__':
    print(run(sys.argv[1:]))