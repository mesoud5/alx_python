"""
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module

"""

class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size
