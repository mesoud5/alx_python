#!/usr/bin/python3
"""Module that defines the Rectangle class"""
from models.base import Base

class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor method
        """

        # Call the super class with id
        super().__init__(id)

        # Assign each argument to the right attribute
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter methods
    def get_width(self):
        """Getter method for width"""
        return self.__width

    def get_height(self):
        """Getter method for height"""
        return self.__height

    def get_x(self):
        """Getter method for x"""
        return self.__x

    def get_y(self):
        """Getter method for y"""
        return self.__y

    # Setter methods
    def set_width(self, width):
        """Setter method for width"""
        self.__width = width

    def set_height(self, height):
        """Setter method for height"""
        self.__height = height

    def set_x(self, x):
        """Setter method for x"""
        self.__x = x

    def set_y(self, y):
        """Setter method for y"""
        self.__y = y
