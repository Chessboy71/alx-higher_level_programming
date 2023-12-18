#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictt = sorted(a_dictionary)
    for i in dictt:
        print("{}: {}".format(i, a_dictionary[i]))
