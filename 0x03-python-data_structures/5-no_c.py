#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for let in my_string:
        if let not in "Cc":
            a = a + let
    return (a)
