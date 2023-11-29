#!/usr/bin/python3
for i in range (26):
    if (i % 2 == 0):
        n = 'z'
    else:
        n = 'Z'
    print('{}'.format(chr(ord(n) - i)), end="")   
