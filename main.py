import sys

def main(progPath, args):
    pass

if __name__ == '__main__':
    try:
        main(sys.argv[0], sys.argv[1:])
    except Exception as e:
        print("ERROR:", e, file=sys.stderr)
    except:
        print("ERROR: Unknown error.", file=sys.stderr)
