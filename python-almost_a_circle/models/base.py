class Base:
    """
     Base class for managing id attribute in all other classes.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects created.

    Methods:
        __init__(self, id=None): Constructor for Base class.
            If id is not None, assign the public instance attribute id with this argument value.
            Otherwise, increment __nb_objects and assign the new value to the public instance attribute id.
    
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.
        If id is not None, assign the public instance attribute id with this argument value.
        Otherwise, increment __nb_objects and assign the new value to the public instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
