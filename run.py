import subprocess as subp

def log(*args, **kwargs):
    #return print(*args, **kwargs)
    pass

#Usage:
#print(run(['ls', '-lh']))
def run(args):
    log("run({})".format(args))
    retVal = subp.check_output(args).decode('utf_8', 'replace').strip()
    if retVal:
        log(retVal)
    return retVal


