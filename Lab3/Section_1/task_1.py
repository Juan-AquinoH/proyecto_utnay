# Programa para multiplicar dos matrices 4x4 sin librerías
# 1. Ingreso de las matrices A y B
print("Ingrese los elementos de la matriz A (4x4):")
A = []
for i in range(4):
    fila = []
    for j in range(4):
        valor = int(input(f"A[{i}][{j}]: "))
        fila.append(valor)
    A.append(fila)
print("Ingrese los elementos de la matriz B (4x4):")
B = []
for i in range(4):
    fila = []
    for j in range(4):
        valor = int(input(f"B[{i}][{j}]: "))
        fila.append(valor)
    B.append(fila)
    # 2. Inicializar la matriz resultado C con ceros
C = []
for i in range(4):
    fila = [0]*4
    C.append(fila)

# 3. Multiplicación de matrices
for i in range(4):              # filas de A
    for j in range(4):          # columnas de B
        for k in range(4):      # columnas de A / filas de B
            C[i][j] += A[i][k] * B[k][j]
            # 4. Mostrar la matriz resultado
print("Matriz Resultado (AB=C):")
for i in range(4):
    for j in range(4):
        print(C[i][j], end="\t")
    print()
    
    #Ingrese los elementos de la matriz A (4x4):
#A[0][0]: 1
#A[0][1]: 4
#A[0][2]: 5
#A[0][3]: 3
#A[1][0]: -2
#A[1][1]: 0
#A[1][2]: 9
#A[1][3]: 3
#A[2][0]: 8
#A[2][1]: 11 
#A[2][2]: -9
#A[2][3]: 2
#A[3][0]: 3
#A[3][1]: -8
#A[3][2]: -9
#A[3][3]: 1
#Ingrese los elementos de la matriz B (4x4):
#B[0][0]: 1
#B[0][1]: 2
#B[0][2]: 8
#B[0][3]: 10
#B[1][0]: 2
#B[1][1]: 44
#B[1][2]: 66
#B[1][3]: 3
#B[2][0]: -5
#B[2][1]: 0
#B[2][2]: 2
#B[2][3]: -3
#B[3][0]: 10
#B[3][1]: 23
#B[3][2]: 5
#B[3][3]: 7
#Matriz Resultado (AB=C):
#14      247     297     28
#-17     65      17      -26
#95      546     782     154
#42      -323    -517    40