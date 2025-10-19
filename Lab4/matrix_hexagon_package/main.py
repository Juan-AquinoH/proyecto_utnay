import sys
import os
# Añadir la carpeta 'Lab4' al path para importar el paquete

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

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

# Multiplicación de matrices
product = matrix_multiplication(A, B)
print("Matrix Multiplication Result (A x B):")
for row in product:
    print(row)

# Área del hexágono
side_length = 6
area = area_hexagon(side_length)
print(f"\nArea of a hexagon with side length {side_length} is: {area:.2f}")
