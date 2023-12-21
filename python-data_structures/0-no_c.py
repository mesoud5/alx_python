def no_c(my_string):
    return ''.join(char for char in my_string if char not in 'cC')


print(no_c("holberton school"))
print(no_c("Chicago"))
print(no_c("C is fun!"))