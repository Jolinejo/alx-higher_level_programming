#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for i in range(0, x):
        try:
            print(my_list[i], end='')
            y += 1
        except IndexError:
            print("")
            return y
    print("")
    return y
