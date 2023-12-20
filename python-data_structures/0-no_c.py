def no_c(my_string):
    result_string = ''
    for char in my_string:
        # Check if the lowercase version of the current character is not 'c'
        # and the original character is not 'C'
        if char.lower() != 'c' and char != 'C':
            # Append the character to the result_string
            result_string += char

    return result_string

# Example usage:
print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
