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

    def __str__(self):
        """String representation of Rectangle object"""
        return f"Rectangle({self.width}, {self.height}) at ({self.x}, {self.y})"

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
        if not isinstance(width, int):
            raise TypeError(f"{width}must be an integer")
        if width <= 0:
            raise ValueError(f"{width} must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter method for height"""
        if not isinstance(height, int):
            raise TypeError(f"{height} must be an integer")
        if height <= 0:
            raise ValueError(f"{height} must be > 0")   
        self.__height = height

    @x.setter
    def x(self, x):
        """Setter method for x"""
        if x < 0:
            raise ValueError(f"{x} must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter method for y"""
        if y < 0:
            raise ValueError(f"{y} must be >= 0")
        self.__y = y
#object creation
r = Rectangle(20, 5)
print(r)
