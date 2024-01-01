"""
This module contains the definition of the BaseGeometry class.
"""

class BaseGeometry:
    """
    This is an empty class that serves as a base for geometry-related classes.
    """
    def area(self):
        """
        This is a method that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle with given width and height.
        """
        # Use self.__width and self.__height instead of __width and __height
        self.__width = width
        self.__height = height
        # Validate width and height using integer_validator
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Provides a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    This class represents a square and inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes the square with the given size.
        """
        # Validate size using integer_validator from the base class
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size
