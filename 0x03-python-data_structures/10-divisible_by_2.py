#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    if not my_list:
        return None
    for i in my_list:
        if i % 2 == 0:
            res = res + [True]
        else:
            res = res + [False]
    return res
