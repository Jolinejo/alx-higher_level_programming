#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    summ = 0
    for item in a:
        summ = summ + item
    return summ
