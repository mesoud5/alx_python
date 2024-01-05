"""
Module that defines the Rectangle class.

This module provides a Rectangle class with attributes such as width, height, x, and y.
It also includes methods to validate and set these attributes.
"""

class Rectangle():
    """
    This class represents a rectangle.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - x (int): The x-coordinate of the rectangle.
    - y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id = 0):
     """
    Initializes a new Rectangle instance.

    Parameters:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - x (int, optional): The x-coordinate of the rectangle (default is 0).
    - y (int, optional): The y-coordinate of the rectangle (default is 0).
     """
     self.integer("width", width)
     self.integer("height", height)
     self.integer("x", x)
     self.integer("y", y)
    
     self.positive("width", width)
     self.positive("height", height)
     self.non_negative("x", x)
     self.non_negative("y", y)
    
     if width <= 0:
        raise ValueError("width must be > 0")
    
     self.__width = width
     self.__height = height
     self.__x = x
     self.__y = y

    

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, new_width):
        """
        Setter method for the width attribute.

        Parameters:
        new_width (int): The new width value.

        Raises:
        - TypeError: If new_width is not an integer.
        - ValueError: If new_width is not greater than 0.
        """
        self.integer("width", new_width)
        self.positive("width", new_width)
        self.__width = new_width

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, new_height):
        """
        Setter method for the height attribute.

        Parameters:
        new_height (int): The new height value.

        Raises:
        - TypeError: If new_height is not an integer.
        - ValueError: If new_height is not greater than 0.
        """
        self.integer("height", new_height)
        self.positive("height", new_height)
        self.__height = new_height

    @property
    def x(self):
        """
        Getter method for the x attribute.

        Returns:
        int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, new_x):
        """
        Setter method for the x attribute.

        Parameters:
        new_x (int): The new x-coordinate value.

        Raises:
        - TypeError: If new_x is not an integer.
        - ValueError: If new_x is not greater than or equal to 0.
        """
        self.integer("x", new_x)
        self.non_negative("x", new_x)
        self.__x = new_x

    @property
    def y(self):
        """
        Getter method for the y attribute.

        Returns:
        int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, new_y):
        """
        Setter method for the y attribute.

        Parameters:
        new_y (int): The new y-coordinate value.

        Raises:
        - TypeError: If new_y is not an integer.
        - ValueError: If new_y is not greater than or equal to 0.
        """
        self.integer("y", new_y)
        self.non_negative("y", new_y)
        self.__y = new_y

    def integer(self, attribute_name, value):
        """
        Validates that the given value is an integer.

        Parameters:
        - attribute_name (str): The name of the attribute being validated.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")

    def positive(self, attribute_name, value):
        """
        Validates that the given value is positive (greater than 0).

        Parameters:
        - attribute_name (str): The name of the attribute being validated.
        - value: The value to be validated.

        Raises:
        - ValueError: If the value is not greater than 0.
        """
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def non_negative(self, attribute_name, value):
        """
        Validates that the given value is non-negative (greater than or equal to 0).

        Parameters:
        - attribute_name (str): The name of the attribute being validated.
        - value: The value to be validated.

        Raises:
        - ValueError: If the value is not greater than or equal to 0.
        """
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
    def area(self):
        """
        in this method we will calculate the area of rectangle
        """
        return self.__width * self.__height
    def display(self):
        """
        in this method we will print the rectangle in character #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        str method
        """
        fixed_id = 1
        return f"[Rectangle] ({fixed_id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
      
        """
        Assigns arguments to attributes in a specific order.

        Parameters:
        - *args: No-keyword arguments in the order: id, width, height, x, y.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]