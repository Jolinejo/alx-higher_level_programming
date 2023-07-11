#!/usr/bin/python3
for ascii_val in range(ord('z'), ord('a') - 1, -1):
    if ascii_val % 2 != 0:
        ascii_val = ascii_val - ord('a') + ord('A')
    print("{alpha}".format(alpha=chr(ascii_val)), end='')
