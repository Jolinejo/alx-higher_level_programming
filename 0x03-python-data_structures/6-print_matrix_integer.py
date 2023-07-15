#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for row in matrix:
        for idx in range(len(row)):
            if idx == len(row) - 1:
                print("{:d}".format(row[idx]))
            else:
                print("{:d} ".format(row[idx]), end='')
