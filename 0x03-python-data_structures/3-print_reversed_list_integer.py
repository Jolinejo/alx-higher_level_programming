#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in range(-1, -len(my_list), -1):
        print("{:d}".format(num))
