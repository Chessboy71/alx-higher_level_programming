#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (len(my_list) == 0):
        return None
    for i in my_list:
        if (my_list[i] % 2):
            my_list[i] = True
        else:
            my_list[i] = False

