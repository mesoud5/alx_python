def raise_exception_msg(mesoud):
    raise NameError(mesoud.capitalize())
try:
    raise_exception_msg("cs is fun")
except NameError as ne:
    print(f"{ne}")
