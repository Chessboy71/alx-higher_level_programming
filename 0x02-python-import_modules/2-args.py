#!/usr/bin/python3
import sys
print ("{} arguments.".format(len(sys.argv) - 1))
for c, arg in enumerate(sys.argv):
    if (c > 0):
        print ("{} : {}".format(c, arg))

