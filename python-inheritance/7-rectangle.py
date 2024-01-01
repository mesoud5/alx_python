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
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    in this class there are four methods go understand them
    """
    def __init__(self, width, height):
        # Use self.__width and self.__height instead of __width and __height
        self.__width = width
        self.__height = height
        # Validate width and height using integer_validator
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def integer_validator(self, name, value):
        # Validate that value is a positive integer
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
    def area(self):
        return self.__width * self.__height
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}" 