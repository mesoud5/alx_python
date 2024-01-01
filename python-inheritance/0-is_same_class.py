"""
In this module we will write a function that returns true
if the object is exactly an instance of the specified class
otherwise it will return false
"""
def is_same_class(obj, specified_class):
    """
    this function will check if object is exactlt instance of 
    a specified class
    
    """
    return type(obj) == specified_class


