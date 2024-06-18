#!/usr/bin/python3
if __name__ == "__main__":
    res = 0
    import sys
    for i in range(1, len(sys.argv)):
        res = res + int(sys.argv[i])
    print(res)
