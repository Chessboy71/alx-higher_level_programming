#!/usr/bin/python3

"""class that defines a square"""


class Square:

    """ initiation function with a private size instance"""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
