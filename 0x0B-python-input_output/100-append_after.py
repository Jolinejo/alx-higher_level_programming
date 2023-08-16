#!/usr/bin/python3



def append_after(filename="", search_string="", new_string=""):
    s = ""
    with open(filename, encoding="utf-8") as myfile:
        for line in myfile:
            s += line
            if search_string in line:
                s += new_string
    with open(filename, mode="w", encoding="utf-8") as myfile:
        myfile.write(s)
