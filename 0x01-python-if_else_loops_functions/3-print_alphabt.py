#!/usr/bin/python3
for ascii_val in range(ord('a'), ord('z') + 1):
    if ascii_val != ord('c') and ascii_val != ord('q'):
        print("{alpha}".format(alpha=chr(ascii_val)), end='')
