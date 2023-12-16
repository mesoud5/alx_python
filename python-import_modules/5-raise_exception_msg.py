def raise_exception_msg(message=""):
    raise NameError(message)

# Example usage
try:
    raise_exception_msg("This is a custom NameError message.")
except NameError as ne:
    print(f"Caught a NameError: {ne}")
