def raise_type_error():
    raise TypeError("This is a deliberate type error.")

# Example usage
try:
    raise_type_error()
except TypeError as te:
    print(f"Caught a TypeError: {te}")
