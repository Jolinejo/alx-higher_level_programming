#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = tuple_a + ()
    tuple_2 = tuple_b + ()
    while len(tuple_1) < 2:
        tuple_1 = tuple_1 + (0,)
    while len(tuple_2) < 2:
        tuple_2 = tuple_2 + (0,)
    t = (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
    return t
