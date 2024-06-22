#!/usr/bin/python3
"""
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
"""


def new_in_list(my_list, idx, element):
    newlist = my_list[:]
    if idx < 0:
        return newlist
    elif idx >= len(my_list):
        return newlist
    else:
        newlist = newlist[:idx] + [element] + my_list[idx:]
        return newlist
