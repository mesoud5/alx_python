def square_matrtix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        squared_row = []
        for element in row:
            squared_row.append(element**2)
        new_matrix.append(squared_row)
    return new_matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
new_matrix = square_matrtix_simple(matrix)
print(new_matrix)
print(matrix)
