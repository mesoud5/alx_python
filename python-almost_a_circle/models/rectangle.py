from base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    def get_width(self):
        return self.__width
    def set_width(self, new_width):
        self.__width = new_width