def square_matrtix_simple(matrix=[]):
    squared_matrtix = [[x**2 for x in row]for row in matrix]
    return squared_matrtix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = square_matrtix_simple(matrix)
print(new_matrix)
print(matrix)