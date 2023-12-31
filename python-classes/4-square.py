"""
we will Write a class Square that defines a square by: 

(based on 1-square.py)
"""
class Square:
    """
    Class Square that defines a square by:

    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0)
    - size must be an integer, otherwise raise a TypeError exception with the message "size must be an integer"
    - if size is less than 0, raise a ValueError exception with the message "size must be >= 0"
    - Public instance method: def area(self) that returns the current square area
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square is defaulted to 0 if not provided.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    @property
    def size(self):
        """
        this is a getter method to retrieve the private attribute



        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        this is a setter method give access to the private attribute 
           -to be modified
         also checks
           -that the new value that is modified is integer and not negative number
        
        
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0") 
        self.__size = value 
    def area(self):
        """
        Public instance method that returns the current square area.



        """
        return self.__size**2
    def my_print(self):
        """
       
         public instance method that prints in standard output the square with character #
       
         """
        if self.__size == 0:
            print() 
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
        