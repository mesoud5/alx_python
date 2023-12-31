"""
we will Write a class Square that defines a square by: 

(based on 1-square.py)
"""

class square:
    """
     class Square that defines a square by: (based on 1-square.py)

         Private instance attribute: size
         Instantiation with optional size: def __init__(self, size=0):
         size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
         if size is less than 0, raise a ValueError exception with the message size must be >= 0
         Public instance method: def area(self): that returns the current square area
         with out importing any module 
    """
    def __init__(self, size=0):
        """
        initializes a new instances of the square class
        parameters:
        size which set to 0 by defalut
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
    def area(self):
        """
        this is a public instance method that returns 
          
         -the current square area
        
        """
        return self.__size    