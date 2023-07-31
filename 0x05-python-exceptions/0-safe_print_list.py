#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    if x <= 0:
        return y
    for i in range(0, x):
        try:
            print(my_list[i], end='')
            y += 1
            if i == x - 1:
                print("")
        except:
            if y != 0:
                print("")
            return y
    return y
