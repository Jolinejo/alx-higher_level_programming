#!/usr/bin/python3
def main():
    import sys
    n = len(sys.argv)
    if n == 2:
        out = 'argument:'
    elif n == 1:
        out = 'arguments.'
    else:
        out = 'arguments:'
    print("{n} {args}".format(n=n - 1, args=out))
    for i in range(1, n):
        print("{i}: {arg}".format(i=i, arg=sys.argv[i]))


if __name__ == "__main__":
    main()
