def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg("c is fun")
except NameError as ne:
    print(f"{ne}")
