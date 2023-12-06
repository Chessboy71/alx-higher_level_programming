#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = []
    for i in my_list:
        if (i == search):
            newl.append(replace)
        else:
            newl.append(i)

    return newl
