# matrix_functions.py

def matrix_multiplication(mat1, mat2):
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
