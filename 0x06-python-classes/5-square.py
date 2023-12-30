#!/usr/bin/python3

"""class that defines a square"""


class Square:

    """ initiation function with a private size instance"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        """
        Raisign errors if the value is not correct
        """
        self.size = size
        self.position = position

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
    @property
    def position(self):
        return self.__position
    
    def position(self, value):
            if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")

            self.__position = value

    def area(self):
        """
            return the area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):

        for i in range(self.__position[0]):
            print()
        """ print the square using #"""
        for i in range(self.__size):
            for j in range(self.__position[1]):
                print("_", end="")
            for j in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print("")

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
