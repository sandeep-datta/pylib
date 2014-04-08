#!/usr/bin/env python3

import os, pwd, grp

#Throws OSError exception (it will be thrown when the process is not allowed
#to switch its effective UID or GID):
def drop_privileges():
    if os.getuid() != 0:
        # We're not root so, like, whatever dude
        return

    # Get the uid/gid from the name
    user_name = os.getenv("SUDO_USER")
    pwnam = pwd.getpwnam(user_name)

    # Remove group privileges
    os.setgroups([])

    # Try setting the new uid/gid
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)

    # Ensure a very conservative umask
    old_umask = os.umask(0o22)


#Test by running...
#./drop_privileges
#sudo ./drop_privileges
if __name__ == '__main__':
    print(os.getresuid())
    drop_privileges()
    print(os.getresuid())