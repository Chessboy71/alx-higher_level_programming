#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        r = 0
        for i in range(x):
            print(my_list[i], end="")
            r += 1
    except IndexError:
        None
    print()
    return r
