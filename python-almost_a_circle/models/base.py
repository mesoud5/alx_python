class base:
    """
    in this class we have
    private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        this function checks if id is not none id if it's not
        it will pass the value that is given
        otherwise it will increment the variable __nb_objects by one
        and set that as id
        """
        if id is not None:
         self.id = id
        else:
           base.__nb_objects += 1
           self.id = base.__nb_objects