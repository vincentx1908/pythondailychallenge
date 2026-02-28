def shift_matrix(matrix, shift):
    rows = len(matrix)
    cols = len(matrix[0])
    total = rows * cols

    flat = [num for row in matrix for num in row]

    shift %= total
    shifted = flat[-shift:] + flat[:-shift]
    
    new_matrix = []
    for i in range(0, total, cols):
        new_matrix.append(shifted[i:i+cols])

    return new_matrix

# tests:
# passed:1. shift_matrix([[1, 2, 3], [4, 5, 6]], 1) should return [[6, 1, 2], [3, 4, 5]].
# Passed:2. shift_matrix([[1, 2, 3], [4, 5, 6]], -1) should return [[2, 3, 4], [5, 6, 1]].
# Passed:3. shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) should return [[5, 6, 7], [8, 9, 1], [2, 3, 4]].
# Passed:4. shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6) should return [[7, 8, 9], [1, 2, 3], [4, 5, 6]].
# Passed:5. shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7) should return [[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]].
# Passed:6. shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54) should return [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]].
