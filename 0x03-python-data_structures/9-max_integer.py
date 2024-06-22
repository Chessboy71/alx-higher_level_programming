#!/usr/bin/python3
def max_integer(my_list=[]):
    Max = None
    if not my_list:
        return None
    for i in my_list:
        if not Max:
            Max = i
        else:
            Max = i if i > Max else Max
    return Max
