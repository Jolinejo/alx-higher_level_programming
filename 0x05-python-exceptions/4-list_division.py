#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    y = 0
    for i in range(list_length):
        try:
            y = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            y = 0
        except (TypeError, ValueError):
            print("wrong type")
            y = 0
        except IndexError:
            print("out of range")
            y = 0
        finally:
            new_list.append(y)
    return (new_list)
