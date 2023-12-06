#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    newl = set(my_list)
    for i in newl:
        result += i
    return result
