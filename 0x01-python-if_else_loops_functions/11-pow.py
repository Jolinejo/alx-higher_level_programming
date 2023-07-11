#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(0, b):
            result = result * a
    elif b < 0:
        for i in range(b, 0):
            result = result / a
    return (result)
