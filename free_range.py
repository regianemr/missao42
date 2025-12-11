import sys


def free_range(startRange, endRange):
    print(list(range(startRange, endRange + 1)))


def main():
    args = sys.argv[1::]
    if len(args) != 2:
        print("none")
        return

    arg1, arg2 = int(args[0]), int(args[1])
    if arg2 <= arg1:
        print("O primeiro argumento deve ser menor que o segundo!")
        return

    free_range(int(args[0]), int(args[1]))


if __name__ == "__main__":
    main()
