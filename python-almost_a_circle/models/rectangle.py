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
        if not isinstance(new_width, int):
            raise TypeError(f"{new_width}must be an integer")
        if new_width <= 0:
            raise ValueError(f"{new_width} must be > 0")
        self.__width = new_width

    @height.setter
    def height(self, new_height):
        """Setter method for height"""
        if not isinstance(new_height, int):
            raise TypeError(f"{new_height} must be an integer")
        if new_height <= 0:
            raise ValueError(f"{new_height} must be > 0")   
        self.__height = new_height

    @x.setter
    def x(self, new_x):
        """Setter method for x"""
        if new_x < 0:
            raise ValueError(f"{new_x} must be >= 0")
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        """Setter method for y"""
        if new_y < 0:
            raise ValueError(f"{new_y} must be >= 0")
        self.__y = new_y
#object creation
r = Rectangle(20, 5, 4, 7)
print(r)



if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))