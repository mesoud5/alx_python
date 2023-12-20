def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
             if j < len(matrix[i]) - 1:
                 print("{:d}".format(matrix[i][j]), end=" ")
             else:
                 print("{:d}".format(matrix[i][j]), end="")
        print("")     
# Example usage:
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix_example)
