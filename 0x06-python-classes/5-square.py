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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            return the area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):

        """ print the square using #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print("")
