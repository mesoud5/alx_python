class a_class:
    pass

def is_same_class(obj, specified_class):
    return type(obj) == specified_class

# Creating an instance of 'a_class'
obj = a_class()

# Checking if 'obj' is exactly an instance of 'a_class' using 'is_same_class'
result = is_same_class(obj, a_class)
print(result)  # Output: True

