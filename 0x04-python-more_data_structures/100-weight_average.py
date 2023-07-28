#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum = 0
    mul = 0
    for x, y in my_list:
        sum = sum + y
        mul = mul + (x * y)
    return (mul / sum)
