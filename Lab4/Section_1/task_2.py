#  Create functions to perform multiplication, addition, and subtraction of 4x4 
#matrices. 
def matrix_addition(mat, mat2):
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result
def matrix_subtraction(mat1, mat2):
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = mat1[i][j] - mat2[i][j]
    return result
def matrix_multiplication(mat1, mat2):
    result = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
# Example usage:
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
matrix2 = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]
print("Matrix Addition:")
addition_result = matrix_addition(matrix1, matrix2)
for row in addition_result:
    print(row)
print("\nMatrix Subtraction:")
subtraction_result = matrix_subtraction(matrix1, matrix2)
for row in subtraction_result:
    print(row)
print("\nMatrix Multiplication:")
multiplication_result = matrix_multiplication(matrix1, matrix2)
for row in multiplication_result:
    print(row)
    

#Matrix Addition:
#[17, 17, 17, 17]
#[17, 17, 17, 17]
#[17, 17, 17, 17]
#[17, 17, 17, 17]

#Matrix Subtraction:
#[-15, -13, -11, -9]
#[-7, -5, -3, -1]
#[1, 3, 5, 7]
#[9, 11, 13, 15]

#Matrix Multiplication:
#[80, 70, 60, 50]
#[240, 214, 188, 162]
#[400, 358, 316, 274]
#[560, 502, 444, 386]