#!/usr/bin/python3
for ascii_val in range(ord('a'), ord('z') + 1):
    print("{alpha}".format(alpha=chr(ascii_val)), end='')
