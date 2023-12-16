def safe_print_division(a, b):
     result = None

     try:
           result = a / b
     except ZeroDivisionError:
           print("Division by zero is not allowed.")
     finally:
           print("Inside Finally:")
           print("{}".format(result))
     
safe_print_division(10, 2)
    