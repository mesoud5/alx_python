from models.rectangle import Rectangle
class square(Rectangle):
    def __init__(self, id, x, y, size):
        super().__init__(id, x, y, size, size)
    def __str__(self):
        return f"[square] ({id(self)}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
