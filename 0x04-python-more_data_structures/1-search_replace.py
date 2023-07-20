#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = []
    if my_list == []:
        return new_matrix
    new_matrix = my_list[:]
    new_matrix = list(map(lambda x: replace if x == search else x, new_matrix))
    return new_matrix
