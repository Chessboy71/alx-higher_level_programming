#!/usr/bin/bash
for i in range(ord('a'), ord('z')):
    if (chr(i) != 'q' and chr(i) != 'e'):
        print(chr(i), end="")
