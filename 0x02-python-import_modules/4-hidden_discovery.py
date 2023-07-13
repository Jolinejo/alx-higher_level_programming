#!/usr/bin/python3
def main():
    import hidden_4 as h
    names = dir(h)
    for name in names:
        if name.startswith('__') is False:
            print(name)


if __name__ == "__main__":
    main()
