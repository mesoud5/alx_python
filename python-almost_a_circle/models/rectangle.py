"""
in this module we will create a class which will inherit from 
base class and in this class we will have a constructer method 
    we have already inherited from base but now we will override it
    but first we will call the super to initialize the base constructer
    then as i said earlier we will override it giving it a new 
       private instance attributes
"""
from models.base import Base
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
    def width(self, new_width):
        """Setter method for width"""
        self.positive("width", new_width)
        self.integer("width", new_width)
    @height.setter
    def height(self, new_height):
        """Setter method for height"""
        self.integer("height", new_height)
        self.positive("height", new_height)
    @x.setter
    def x(self, new_x):
        """Setter method for x"""
        self.non_negative("x", new_x)
    @y.setter
    def y(self, new_y):
        """Setter method for y"""
        self.non_negative("y", new_y)


    #methods
    def integer(self, attribute_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
    def positive(self, attribute_name, value):
        if value <= 0:
            raise ValueError(f"{attribute_name} must be >0 ")
    def non_negative(self, attribute_name, value):
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
r = Rectangle(10, 9 ,8 ,7)
