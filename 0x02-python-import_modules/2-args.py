#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    if (len(sys.argv) == 1):
        print ("{} arguments.".format(len(sys.argv) - 1))
    elfif (len(sys.argv) == 2):
        print ("{} argument.".format(len(sys.argv) - 1))
    else:    
        print ("{} arguments:".format(len(sys.argv) - 1))
        for c, arg in enumerate(sys.argv):
            if (c > 0):
                print ("{}: {}".format(c, arg))

