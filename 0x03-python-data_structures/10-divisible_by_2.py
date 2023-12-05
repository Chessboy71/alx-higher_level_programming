#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (len(my_list) == 0):
        return None
    newList = []
    for i in my_list:
        if (my_list[i] % 2 == 0):
            newList.append(True)
        else:
            newList.append(False)
    return newList
