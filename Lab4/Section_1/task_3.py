 #Create one module containing the area functions from Task 1, and another 
#module containing the matrix functions from Task 2. 
#Then, test them in a script by calling the functions from their respective modules.


import task
import task
# Testing area functions from task_1 module
print("Testing Area Functions:")
print("Area of Circle:", task_1.area_circle())
print("Area of Square:", task_1.area_square())
print("Area of Triangle:", task_1.area_triangle())
print("Area of Hexagon:", task_1.area_hexagon())
print("Area of Circle with radius 5:", task_1.area_circle(5))
print("Area of Square with side 10:", task_1.area_square(10))
print("Area of Triangle with base 6 and height 9:", task_1.area_triangle(6, 9))
print("----------------------------------------")
# Testing matrix functions from task_2 module
print("Testing Matrix Functions:")
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
addition_result = task_2.matrix_addition(matrix1, matrix2)
for row in addition_result:
    print(row)
print("\nMatrix Subtraction:")
subtraction_result = task_2.matrix_subtraction(matrix1, matrix2)
for row in subtraction_result:
    print(row)
print("\nMatrix Multiplication:")
for row in task_2.matrix_multiplication(matrix1, matrix2):
    print(row)
    
#Testing Area Functions:
#Using default radius of 4
#Area of Circle: 50.26548245743669
#Using default side length of 7
#Area of Square: 49
#Using default base of 4 and height of 13
#Area of Triangle: 26.0
#Using default side length of 8
#Area of Hexagon: 166.27687752661222
#Area of Circle with radius 5: 78.53981633974483
#Area of Square with side 10: 100
#Area of Triangle with base 6 and height 9: 27.0
#----------------------------------------
#Testing Matrix Functions:
#Matrix Addition:
#[17, 17, 17, 17]
#[17, 17, 17, 17]
#[17, 17, 17, 17]
#[17, 17, 17, 17]

#Matrix Subtraction:
#[-15, -13, -11, -9]
#[-7, -5, -3, -1]
#[-15, -13, -11, -9]
#[-7, -5, -3, -1]
#[-7, -5, -3, -1]
#[1, 3, 5, 7]
#[9, 11, 13, 15]

#Matrix Multiplication:
#[80, 70, 60, 50]
#[240, 214, 188, 162]
#[400, 358, 316, 274]
#[560, 502, 444, 386]  