#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_matrix = []
    if my_list == []:
        return new_matrix
    new_matrix = my_list[:]
    new_matrix = list(map(lambda x: x * number, new_matrix))
    return new_matrix
