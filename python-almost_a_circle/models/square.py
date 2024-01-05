"""
in this module we will import from module rectangle
"""
# models/square.py
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    in this class we will inherit from class rectangle Rectangle
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

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        int: The side length of the square.
        """
        return self.width

    @size.setter
    def size(self, new_size):
        """
        Setter method for the size attribute.

        Parameters:
        new_size (int): The new size value.

        Raises:
        - TypeError: If new_size is not an integer.
        - ValueError: If new_size is not greater than 0.
        """
        self.integer("size", new_size)
        self.positive("size", new_size)
        self.width = new_size
        self.height = new_size

    def update(self, *args, **kwargs):
        """
        Updates the Square instance attributes.

        Parameters:
        - args: Variable length argument list.
        - kwargs: Arbitrary keyword arguments.

        Note:
        *args will be skipped if **kwargs is present and not empty.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square.

        Returns:
        dict: Dictionary representation of the Square attributes.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

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
