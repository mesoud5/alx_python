def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]           
print_matrix_integer(matrix)
