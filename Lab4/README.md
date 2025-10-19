

Elaboro: Juan Carlos Aquino Hernández
##  Descripción de las Tareas

###  `task_1.py` — Cálculo de áreas

- Contiene funciones para calcular el área de:
  - Círculo
  - Cuadrado
  - Triángulo
  - Hexágono
- Cada función tiene **valores por defecto**, y muestra un mensaje si se usan.
#Using default side length of 7
#Area of Square: 49
#Using default base of 4 and height of 13
#Area of Triangle: 26.0
#Using default side length of 8
#Area of Hexagon: 166.27687752661222
#Area of Circle with radius 5: 78.53981633974483
#Area of Square with side 10: 100
#Area of Triangle with base 6 and height 9: 27.0
#Area of Hexagon with side 12: 374.1229744348775
**Funciones principales:**
- `area_circle(radius=4)`
- `area_square(side=7)`
- `area_triangle(base=4, height=13)`
- `area_hexagon(side=8)`


###  `task_2.py` — Operaciones con matrices 4x4

- Define funciones para:
  - Suma de matrices 4x4
  - Resta de matrices 4x4
  - Multiplicación de matrices 4x4

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
**Funciones principales:**
- `matrix_addition(mat1, mat2)`
- `matrix_subtraction(mat1, mat2)`
- `matrix_multiplication(mat1, mat2)`


### 📄 `task_3.py` *(opcional según práctica)*



Posteriormente, se creó un script de prueba que:

Importa ambos módulos.

Ejecuta y muestra los resultados de las funciones de área.

Ejecuta y muestra las operaciones con matrices.

Resultado esperado:

-Cálculo correcto de áreas con valores por defecto y personalizados.

-Operaciones matriciales mostrando la suma, resta y multiplicación de dos matrices 4x4.

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

### 📄 `task_4.py` — Script principal 🧠

- Importa funciones desde el **paquete `matrix_hexagon_package`**.
- Realiza:
  - Multiplicación de dos matrices de ejemplo `A` y `B`.
  - Cálculo del área de un hexágono con lado 6.
- Muestra resultados en consola.

´python
from matrix_hexagon_package import matrix_multiplication, area_hexagon

# Ejemplo de matrices
A = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]]
B = [[7,6,5,4],[3,2,1,0],[1,3,5,7],[9,8,6,4]]

# Multiplicación de matrices
product = matrix_multiplication(A, B)
for row in product:
    print(row)

# Área de hexágono
print("Área del hexágono:", area_hexagon(6))

#Matrix Multiplication Result (A x B):
#[52, 51, 46, 41]
#[132, 127, 114, 101]
#[95, 86, 74, 62]
#[112, 108, 97, 86]

# se elaboro una carpeta de matrix_hexagon_packe/ para posterior llamar arxhivos  o funciones de task_4

# Contenido
matrix_hexagon_package/
├── __init__.py
├── area_functions.py
└── matrix_functions.py
-area_functions.py → contiene la función area_hexagon() para calcular el área de un hexágono.

-matrix_functions.py → contiene funciones para suma, resta y multiplicación de matrices 4x4.

- __init__.py → permite importar fácilmente desde el paquete:

# se utilizo  para llamar a area_hexagon y matrix_multiplication de matrix_hexagon_packege
from matrix_hexagon_package import area_hexagon, matrix_multiplication

# quese tiene
 ->Código ordenado y modular

->Reutilización en múltiples scripts

->Facilidad de mantenimiento y lectura

->Mejores prácticas de desarrollo en Python


