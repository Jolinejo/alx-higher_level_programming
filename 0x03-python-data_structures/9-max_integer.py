#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_n = my_list[0]
    for item in my_list:
        if item > max_n:
            max_n = item
    return max_n
