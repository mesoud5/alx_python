class a_class:
    pass
def is_same_class(obj, a_class):
    return isinstance(obj, a_class)
obj = a_class()
print(is_same_class(obj, a_class))
