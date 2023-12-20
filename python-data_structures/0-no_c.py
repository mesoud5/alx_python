def no_c(my_string):
    result_string = ''
    for char in my_string:
        if char.lower() not in ['c', 'C']:
            result_string += char
    return result_string


print(no_c("holberton school"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
