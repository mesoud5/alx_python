def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < len(matrix[i]) - 1:
                print("{}".format(matrix[i][j]), end = " ")
            else:
                print("{}".format(matrix[1][j]), end = "")  
                print("")  
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]                
print_matrix_integer(matrix)