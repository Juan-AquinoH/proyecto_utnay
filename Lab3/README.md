
---

##  Archivo 2: `Lab3.py`

# Lab3:  Programa para multiplicar dos matrices 4x4 sin librerías,Diccionario con palabras que contienen la letra a,Genera un número aleatorio entre 1 y 100, de Tipos en y Create a program that allows the user to create a new password, which must be at least 8 characters long, contain no spaces, and not include any of the following characters: &, #, %, @.Python
# Autor: Juan Carlos Aquino Hernández
# Fecha: Octubre 2025

# ===============================================================
# task_1 — Multiplicación de matrices 4x4 sin librerías
# ===============================================================

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

#Matriz Resultado (AB=C):
#14      247     297     28
#-17     65      17      -26
#95      546     782     154
#42      -323    -517    40

# ===============================================================
#  task_2: #Diccionario con palabras que contienen la letra a
# ===============================================================

# Diccionario original con animales
animals = {
    1: "ferret",
    2: "boar",
    3: "jaguar",
    4: "giraffe",
    5: "lizard",
    6: "locust",
    7: "lion",
    8: "wolf",
    9: "parrot",
    10: "raccoon",
    11: "butterfly",
    12: "jellyfish",
    13: "fly",
    14: "gnat",
    15: "bat",
    16: "otter",
    17: "bear",
    18: "polar bear",
    19: "oyster",
    20: "sheep",
    21: "bee",
    22: "eagle",
    23: "antelope",
    24: "spider",
    25: "squirrel",
    26: "tuna",
    27: "ostrich",
    28: "wasp",
    29: "whale",
    30: "bison",
    31: "buffalo",
    32: "owl",
    33: "donkey",
    34: "horse",
    35: "goat",
    36: "squid",
    37: "chameleon",
    38: "camel",
    39: "crab",
    40: "kangaroo",
    41: "cat",
    42: "dog"
}

print("Diccionario con la letra 'a':")
a_dict = {}
for key, value in animals.items():
    if "a" in value:
        a_dict[key] = value1
print(a_dict)
#Diccionario con palabras que contienen la letra b
print("Diccionario con la letra 'b':")
b_dict = {}
for key, value in animals.items():
    if "b" in value:
        b_dict[key] = value
print(b_dict)
        
        # c. Diccionario con palabras que contienen la letra "y"
print("Diccionario con la letra 'y':")
y_dict = {}
for key, value in animals.items():
    if "y" in value:
        y_dict[key] = value
print(y_dict)

# Nuevo diccionario con palabras que contienen 'y' y 'b'
yb_dict = {}

for key, value in animals.items():
    if "y" in value and "b" in value:
        yb_dict[key] = value

print("Diccionario con palabras que contienen 'y' y 'b':")
print(yb_dict)

#Diccionario con la letra 'a':
#{2: 'boar', 3: 'jaguar', 4: 'giraffe', 5: 'lizard', 9: 'parrot', 10: 'raccoon', 14: 'gnat', 15: 'bat', 17: 'bear', 18: 'polar bear', 22: 'eagle', 23: 'antelope', 26: 'tuna', 28: 'wasp', 29: 'whale', 31: 'buffalo', 35: 'goat', 37: 'chameleon', 38: 'camel', 39: 'crab', 40: 'kangaroo', 41: 'cat'}
#Diccionario con la letra 'b':
#{2: 'boar', 11: 'butterfly', 15: 'bat', 17: 'bear', 18: 'polar bear', 21: 'bee', 30: 'bison', 31: 'buffalo', 39: 'crab'}
#Diccionario con la letra 'y':
#{11: 'butterfly', 12: 'jellyfish', 13: 'fly', 19: 'oyster', 33: 'donkey'}
#Diccionario con palabras que contienen 'y' y 'b':
#{11: 'butterfly'}

# ===============================================================
#  task_3: # Genera un número aleatorio entre 1 y 100
secret_number = random.randint(1, 100)
# ===============================================================
import rando

# Genera un número aleatorio entre 1 y 100
secret_number = random.randint(1, 100)

print(" ¡Bienvenido al juego de adivinar números!")
print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

attempts = 0
guess = 0  # Inicializa la suposición para entrar en el bucle

# Sigue preguntando hasta que el usuario adivine correctamente
while guess != secret_number:
    try:
        guess = int(input("Introduce tu suposición: "))
        attempts += 1

        if guess < secret_number:
            print("El número es más alto. ¡Inténtalo de nuevo!")
        elif guess > secret_number:
            print("El número es más bajo. ¡Inténtalo de nuevo!")
        else:
            print(f" ¡Correcto! Lo adivinaste en {attempts} intentos.")
    except ValueError:
        print(" Por favor, introduzca un número válido.")

       //    Resultados //
        
         #¡Bienvenido al juego de adivinar números!
#Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?
#Introduce tu suposición: 70
#El número es más bajo. ¡Inténtalo de nuevo!
#Introduce tu suposición: 50
#El número es más alto. ¡Inténtalo de nuevo!
#Introduce tu suposición: 60
#El número es más alto. ¡Inténtalo de nuevo!
#Introduce tu suposición: 65
#El número es más bajo. ¡Inténtalo de nuevo!
#Introduce tu suposición: 64
#El número es más bajo. ¡Inténtalo de nuevo!
#Introduce tu suposición: 63
# ¡Correcto! Lo adivinaste en 6 intentos.

# ===============================================================
#  task_4: # Create a program that allows the user to create a new password, which must be at least 8 characters long, contain no spaces, and not include any of the following characters: &, #, %, @.
# ===============================================================

password = input('Intoduce el new_password: ')
   
if password == 'aHt37gh8':
    print('Acceso autorizado')
     
        
    print('Acceso autorizado')
if password != 'aHt37gh8':
     print('Acceso denegado')
     print('Fin')
     
     
    # Intoduce el new_password: aHt37gh8
    # Acceso autorizado
    # Acceso autorizado
    
    #Intoduce el new_password: aht37gh8
    #Acceso denegado
    #Fin

# ===============================================================
#  task_5: error task_1
# ===============================================================
#Error 
Ingrese los elementos de la matriz A (4x4):
A[0][0]: 1
A[0][1]: 4
A[0][2]: 5
A[0][3]: 
Traceback (most recent call last):
  File "C:\Users\Lenovo\Desktop\pythoncore2025\class_5\Section_3Error Detection\Lab3\Section_1 Programming Practice\task_1.py", line 9, in <module>
    valor = int(input(f"A[{i}][{j}]: "))
ValueError: invalid literal for int() with base 10: ''
PS C:\Users\Lenovo\Desktop\pythoncore2025\class_5> 7
7

# ===============================================================
#  task_6: error tas_2
# ===============================================================
Diccionario con la letra 'a':
Traceback (most recent call last):
  File "C:\Users\Lenovo\Desktop\pythoncore2025\class_5\Section_3Error Detection\Lab3\Section_1 Programming Practice\task_2.py", line 52, in <module>
    a_dict[key] = value1
                  ^^^^^^
NameError: name 'value1' is not defined. Did you mean: 'value'?

# ===============================================================
#  task_7: Error en task_3
# ===============================================================
Traceback (most recent call last):
  File "C:\Users\Lenovo\Desktop\pythoncore2025\class_5\Section_3Error Detection\Lab3\Section_1 Programming Practice\task_3.py", line 1, in <module>
    import rando
ModuleNotFoundError: No module named 'rando'
PS C:\Users\Lenovo\Desktop\pythoncore2025\class_5> 

# ===============================================================
#  task_8: Error en tas_4
# ===============================================================
Intoduce el new_password: aHt37gh8
Acceso autorizado
Acceso autorizado
Traceback (most recent call last):
  File "C:\Users\Lenovo\Desktop\pythoncore2025\class_5\Section_3Error Detection\Lab3\Section_1 Programming Practice\task_4.py", line 11, in <module>
    if passwod != 'aHt37gh8':
       ^^^^^^^
NameError: name 'passwod' is not defined. Did you mean: 'password'?