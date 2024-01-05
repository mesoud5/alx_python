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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, new_size):
        """Setter method for the size attribute."""
        self.integer("size", new_size)
        self.positive("size", new_size)
        self.__width = new_size
        self.__height = new_size

    def integer(self, attribute_name, value):
        """Validates that the given value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")

    def positive(self, attribute_name, value):
        """Validates that the given value is positive (greater than 0)."""
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")
