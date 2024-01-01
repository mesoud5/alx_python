"""
in this module we will Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) 
from the specified class otherwise False.

"""
def inheritance_from(obj, a_class):
    """
    this function returns True if the object is an instance of a class that inherited (directly or indirectly) 
    from the specified class ; otherwise False.
    """
    if issubclass(type(obj), a_class):
        return True
    for base_class in type(obj).__base__:
        if issubclass(base_class, a_class):
            return True
    
    return False