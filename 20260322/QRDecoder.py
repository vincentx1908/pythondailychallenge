def rotate_matrix(matrix):
        row = len(matrix)
        col = len(matrix[0])
        new_matrix = []
        for i in range(col):
            new_row = []
            for j in range(row):
                new_row.append(matrix[row - j - 1][i])
            new_matrix.append("".join(new_row))
        return new_matrix
    
def valid(m):
    return (
        m[0][0:2] == "11" and
        m[1][0:2] == "11" and
        m[0][4:6] == "11" and
        m[1][4:6] == "11" and
        m[4][0:2] == "11" and
        m[5][0:2] == "11"
    )

def read_data(m):
    result = ""
    for r in range(6):
        for c in range(6):
            if (r < 2 and c < 2) or (r < 2 and c >= 4) or (r >= 4 and c < 2):
                continue
            result += m[r][c]
    return result

def decode_qr(qr_code):
    for _ in range(4):
        if valid(qr_code):
            return read_data(qr_code)
        qr_code = rotate_matrix(qr_code)


# This challenge is very interesting and also thought-provoking. 
# There are several steps needed so that several independent functions were created with 
# each focusing on one specific step.
# 1. First of all the input matrix needs to be checked if it is in the right orientation.
# So the valid() function checks for this and returns the result as a boolean.
# 2. The input matrix needs to be rotated if it's not in the right orientation.
# The rotate_matrix() function does the job and returns a matrix with exactly the same format.
# 3. The read_data() function decodes a QR code, gets rid of the orientation marks and return a string.
# 4. Lastly the decode_qr() function combines all the independent functions together with a loop:
# it takes the input matrix, checks for valid orientation, if yes, output the QR code info, if not, 
# it rotates the input matrix until it's valid and then output the QR code info.
