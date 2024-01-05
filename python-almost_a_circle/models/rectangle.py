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

    # Getter methods
    def get_width(self):
        """
        This is a getter method for private instanace attribute __width
        In this methode we will retriev the value
        """
        return self.__width

    def get_height(self):
        """
        This is a getter method for private instanace attribute __height
        In this methode we will retriev the value
        """
        return self.__height

    def get_x(self):
        """
        This is a getter method for private instanace attribute __x
        In this methode we will retriev the value
        """
        return self.__x

    def get_y(self):
        """
        This is a getter method for private instanace attribute __y
        In this methode we will retriev the value
        """
        return self.__y

    # Setter methods
    def set_width(self, new_width):
        """
        This is a setter method for private instance attribute __width 
        In this method we will modify the private instance attribute
        """
        self.__width = new_width

    def set_height(self, new_height):
        """
        This is a setter method for private instance attribute __height 
        In this method we will modify the private instance attribute
        """
        self.__height = new_height

    def set_x(self, new_x):
        """
        This is a setter method for private instance attribute __x
        In this method we will modify the private instance attribute
        """
        self.__x = new_x

    def set_y(self, new_y):
        """
        This is a setter method for private instance attribute __y
        In this method we will modify the private instance attribute
        """
        self.__y = new_y
