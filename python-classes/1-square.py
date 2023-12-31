"""
   in this moduleor file we write a class square that defines a square based on our last project 
    
    go back there and check it
"""
class Square:
    """
           In this class we will  Write a class Square that defines a square by: (based on 0-square.py)

             -Private instance attribute: size
              Instantiation with optional size: def __init__(self, size=0):
              size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
              if size is less than 0, raise a ValueError exception with the message size must be >= 0
              You are not allowed to import any module
    """
    def __init__(self, size=0):
        """
        initializes a new instances of the sqaure class
        parameteres
         size(int, optional)the size of the square is defualeted to 0 if not provided
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
  