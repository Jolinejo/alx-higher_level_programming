#!/usr/bin/python3
def uppercase(str):
    for let in str:
        if ord(let) >= ord('a') and ord(let) <= ord('z'):
            c = chr(ord(let) - ord('a') + ord('A'))
        else:
            c = let
        print("{alpha}".format(alpha=c), end='')
    print("")
