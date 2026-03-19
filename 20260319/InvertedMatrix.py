def invert_matrix(matrix):
    values = set()
    for row in matrix:
        for v in row:
            values.add(v)
    a, b = values
    new_matrix = []

    for row in matrix:
        new_row = []
        for v in row:
            if v == a:
                new_row.append(b)
            else:
                new_row.append(a)
        new_matrix.append(new_row)

    return new_matrix

# As the challenge suggested, there are only two distinct values in the matrix,
# and the purpose is to swap the values in the matrix.
# So the first step is to simply find the two distinct values.
# Then the two distinct values are assigned to a and b.
# Next a new matrix is created.
# By looping through all the values in matrix, the values are swapped from a to b or from b to a and 
# saved into the new matrix.


# ChatGPT also provided another "more pythonic" method with fewer lines.
# But the logic behind the method is the same as the longer version.

def invert_matrix(matrix):
    values = list({v for row in matrix for v in row})
    a, b = values

    return [[b if v == a else a for v in row] for row in matrix]
