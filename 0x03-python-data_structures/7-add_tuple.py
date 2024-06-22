#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l1, l2 = 0, 0
    if len(tuple_b) >= 2:
        l1 = tuple_b[0]
        l2 = tuple_b[1]
    elif len(tuple_b) == 1:
        l1 = tuple_b[0]
    if len(tuple_a) >= 2:
        l1 = l1 + tuple_a[0]
        l2 = l2 + tuple_a[1]
    elif len(tuple_a) == 1:
        l1 = l1 + tuple_a[0]
    return (l1, l2)
