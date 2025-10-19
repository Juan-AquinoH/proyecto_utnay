 #Create a package that includes the modules created in the previous tasks. 
#Finally, in a script, import the package and display: the result of the matrix 
#multiplication and the calculation of the area of a hexagon using the functions from 
#the package.

#importar desde el paquete
from matrix_hexagon_package import matrix_multiplication, area_hexagon



A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7]
]

B = [
    [7, 6, 5, 4],
    [3, 2, 1, 0],
    [1, 3, 5, 7],
    [9, 8, 6, 4]
]

# Matrix multiplication
product = matrix_multiplication(A, B)

print("Matrix Multiplication Result (A x B):")
for row in product:
    print(row)

# Hexagon area
side_length = 6
area = area_hexagon(side_length)
print(f"\nArea of a hexagon with side length {side_length} is: {area:.2f}")
#Matrix Multiplication Result (A x B):
#[52, 51, 46, 41]
#[132, 127, 114, 101]
#[95, 86, 74, 62]
#[112, 108, 97, 86]

#Area of a hexagon with side length 6 is: 93.53