#!/usr/bin/python3
def main():
    import sys
    n = len(sys.argv)
    summ = 0
    for i in range(1, n):
        summ = summ + int(sys.argv[i])
    print(summ)


if __name__ == "__main__":
    main()
