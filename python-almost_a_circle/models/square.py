"""
in this module we will import from models,rectangle class rectangle
"""
from .rectangle import Rectangle
class square(Rectangle):
    """
    in this class we have inherited from class rectangle so 
    we have everything class rectangle have
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        this is a constructer method
        """
        super().__init__(id, x, y, size, size)
    def __str__(self):
        """
        this is the str method
        """
        return f"[square] ({id(self)}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
