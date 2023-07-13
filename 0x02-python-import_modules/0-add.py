#!/usr/bin/python3
def main():
    a = 1
    b = 2
    from add_0 import add
    print("{a} + {b} = {val}".format(a=a, b=b, val=add(a, b)))
if __name__ == "__main__":
    main()
