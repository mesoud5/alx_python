def raise_exception_msg(mesoud):
    raise NameError(mesoud)
try:
    raise_exception_msg("c is fun")
except NameError as ne:
    print(f"{ne}")
