#!/usr/bin/python3
"""
    This is a file for a class Declaration names square
    """


class Square:
    """ This class defines a square,
        it is pretty useful if you need to learn geometry
    """

    def __init__(self, size=0) -> int:
        try:
            if size < 0:
                raise (ValueError)
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
