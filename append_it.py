import sys


def append_it(args):
    if not len(args):
        print("none")
        return
    for arg in args:
        if not arg.endswith("ism"):
            print(arg + "ism")


append_it(sys.argv[1:])
