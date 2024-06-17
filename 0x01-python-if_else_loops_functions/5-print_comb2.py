#!/usr/bin/python3
for i in range(99):
    print("{:.0f}{:d}".format(i//10, i % 10), end=", ")
print("99")
