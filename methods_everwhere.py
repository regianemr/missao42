import sys


def shrink(arg):
    print(arg[:8])


def enlarge(arg):
    print(arg.ljust(8, "z"))


def main():
    args = sys.argv[1:]
    print(args)
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)


main()
