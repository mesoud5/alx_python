def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Parameters:
    - matrix (list of lists): The input matrix containing integers.

    Returns:
    - list of lists: A new matrix with each integer squared.
    """
    # Create a new matrix with the same size as the input matrix
    new_matrix = []

    # Iterate over rows in the input matrix
    for row in matrix:
        # Create a new row for the squared values
        squared_row = []
        
        # Iterate over elements in the current row and square each element
        for element in row:
            squared_row.append(element ** 2)
        
        # Add the squared row to the new matrix
        new_matrix.append(squared_row)

    return new_matrix

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)

    # Display the result
    print(new_matrix)
    print(matrix)
