#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print('{}'.format(chr(ord(char) - ord('a') + ord('A'))), end='')
        else:
            print('{}'.format(char), end='')
<<<<<<< HEAD
=======
    print()
>>>>>>> dc94a55de663c2012ae5f447070f7448681b45fc
