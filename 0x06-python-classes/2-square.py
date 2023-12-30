#!/usr/bin/python3

"""class that defines a square"""


class Square:

    """ initiation function with a private size instance"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        """
        Raisign errors if the value is not correct
        """

        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
