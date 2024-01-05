"""
in this module we will import from module rectangle
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    in this class we will inherit from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The side length of the square.
        - x (int, optional): The x-coordinate of the square (default is 0).
        - y (int, optional): The y-coordinate of the square (default is 0).
        - id (int, optional): The ID of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

   