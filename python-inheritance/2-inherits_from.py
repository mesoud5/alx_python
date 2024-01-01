"""
Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

"""
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    """
    # Check if the specified class itself is in the object's inheritance hierarchy
    if issubclass(type(obj), a_class):
        return True

    # Check if any of the object's base classes are inherited from the specified class
    for base_class in type(obj).__bases__:
        if issubclass(base_class, a_class):
            return True
    else:
        return False
