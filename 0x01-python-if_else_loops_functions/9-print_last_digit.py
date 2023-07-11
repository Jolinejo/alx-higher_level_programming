#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    last = number - int(number / 10) * 10
    print(last, end='')
    return (last)
