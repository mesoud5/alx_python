"""
in this module we will create a class which will inherit from 
base class and in this class we will have a constructer method 
    we have already inherited from base but now we will override it
    but first we will call the super to initialize the base constructer
    then as i said earlier we will override it giving it a new 
       private instance attributes
"""
from .base import Base
"""
we are importing class base from module base
"""
class Rectangle(Base):
    """
    in this class we will have a constructer method 
    we have already inherited from base but now we will override it
    but first we will call the super to initialize the base constructer
    then as ai said earlier we will override it giving it a new 
    private instance attributes
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is a constructer method
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width
    @property
    def height(self):
        """Getter method for height"""
        return self.__height
    @property
    def x(self):
        """Getter method for x"""
        return self.__x
    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    # Setter methods
    @width.setter
    def width(self, width):
        """Setter method for width"""
        self.__width = width
    @height.setter
    def height(self, height):
        """Setter method for height"""
        self.__height = height
    @x.setter
    def x(self, x):
        """Setter method for x"""
        self.__x = x
    @y.setter
    def y(self, y):
        """Setter method for y"""
        self.__y = y
