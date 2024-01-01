def inheritance_from(obj, a_class):
    if issubclass(type(obj), a_class):
        return True
    for base_class in type(obj).__base__:
        if issubclass(base_class, a_class):
            return True
    else:
        return False