#  REMEND.md  
**Práctica de Fundamentos de Python**
**Autor:** Juan Carlos Aquino Hernández  
**Archivo:** `REMEND.md`  
**Lenguaje:** Python  
**Propósito:** práctica integral de tipos, estructuras y métodos básicos.
---

##  task_1 — Conversiones de tipo

```python
#Create a string variable with the value "123" and convert it to integer, float, 
##boolean, list, and tuple. Make sure to check that each conversion is successful. 
#Then, change the value of the variable to "hello". What happens with the 
#conversions? Explain the outcome. 

valor = "123"
print(f"Valor inicial: {valor} (tipo: {type(valor)})")

# Convertir a entero
entero = int(valor)
print(f"Convertido a entero: {entero} (tipo: {type(entero)})")

# Convertir a flotante
flotante = float(valor)
print(f"Convertido a flotante: {flotante} (tipo: {type(flotante)})")

# Convertir a booleano
booleano = bool(valor)
print(f"Convertido a booleano: {booleano} (tipo: {type(booleano)})")

# Convertir a lista
lista = list(valor)
print(f"Convertido a lista: {lista} (tipo: {type(lista)})")

# Convertir a tupla
tupla = tuple(valor)
print(f"Convertido a tupla: {tupla} (tipo: {type(tupla)})")

#Resultados esperados:
#Valor inicial: 123 (tipo: <class 'str'>)
#Convertido a entero: 123 (tipo: <class 'int'>)
#Convertido a flotante: 123.0 (tipo: <class 'float'>)
#Convertido a booleano: True (tipo: <class 'bool'>)
#Convertido a lista: ['1', '2', '3'] (tipo: <class 'list'>)
#Convertido a tupla: ('1', '2', '3') (tipo: <class 'tuple'>)

valor = "hello"
print(f"\nNuevo valor: {valor} (tipo: {type(valor)})")

try:
    entero = int(valor)
    print(f"Convertido a entero: {entero}")
except ValueError as e:
    print(f"Error al convertir a entero: {e}")

try:
    flotante = float(valor)
    print(f"Convertido a flotante: {flotante}")
except ValueError as e:
    print(f"Error al convertir a flotante: {e}")

booleano = bool(valor)
print(f"Convertido a booleano: {booleano}")

lista = list(valor)
print(f"Convertido a lista: {lista}")

tupla = tuple(valor)
print(f"Convertido a tupla: {tupla}")

# Resultados esperados:
#Nuevo valor: hello (tipo: <class 'str'>)
#Error al convertir a entero: invalid literal for int() with base 10: 'hello'
#Error al convertir a flotante: could not convert string to float: 'hello'
#Convertido a booleano: True
#Convertido a lista: ['h', 'e', 'l', 'l', 'o']
#Convertido a tupla: ('h', 'e', 'l', 'l', 'o')

 **Objetivo:** practicar conversiones entre tipos de datos básicos (`str`, `int`, `float`, `bool`, `list`, `tuple`).

---

##  task_2 — Manejo de errores en conversiones

```python
 #Perform operations (addition, subtraction, multiplication, and division) 
#using int and float numbers. Print the results and check the data type of each result. 
num_int = 1500
num_float = 234.90
print(f"\nNúmero entero: {num_int} (tipo: {type(num_int)})")
addition = num_int + num_float
print(f"Suma: {addition} (tipo: {type(addition)})")
subtraction = num_int - num_float
print(f"Resta: {subtraction} (tipo: {type(subtraction)})")
multiplication = num_int * num_float
print(f"Multiplicación: {multiplication} (tipo: {type(multiplication)})")
division= num_int / num_float
print(f"División: {division} (tipo: {type(division)})")

#Resultados esperados:
#Número entero: 1500 (tipo: <class 'int'>)
#Suma: 1734.9 (tipo: <class 'float'>)
#Resta: 1265.1 (tipo: <class 'float'>)
#Multiplicación: 352350.0 (tipo: <class 'float'>)
#División: 6.385696040868455 (tipo: <class 'float'>)
```

 **Objetivo:** Realizar operaciones aritméticas entre números enteros int y float.

---

##  task_3 — Given a list or tuple, identify the element with the maximum value, the element with the minimum value, and the length of the list. 

```python
num_int = 80
num_float = 25.6

datos = [13, 3, 16, 22, 10]
print(f"\nDatos: {datos}")

copia = datos.copy()
copia.sort()
print(f"Datos ordenados: {copia}")

print(f"Mínimo: {copia[0]}")
print(f"Máximo: {copia[-1]}")

texto_lista = str(datos)[1:-1]
longitud = 0 if texto_lista.strip() == "" else texto_lista.count(",") + 1
print(f"Longitud: {longitud}")

# Resultados esperados:
#Datos: [13, 3, 16, 22, 10]
#Datos ordenados: [3, 10, 13, 16, 22]
#Mínimo: 3
#Máximo: 22
#Longitud: 5
```

 **Objetivo:** comprender operaciones aritméticas entre ` maximum value` , `minimum valuet` , length of the list.

---

##  task_4 — Listas y sus métodos

```python
# The following dictionary shows the grades of all subjects for each student. 
#Create a new dictionary that contains only the student's name and their average 
#grade.  
#Note: You may use the sum() function, which takes a list or tuple and returns the 
#sum of its elements. 
grades = {
    "Guillermo Arroyo": {"Matematicas": 85, "Fisica": 90, "English": 78},
    "Francisco Carrillo": {"Matematicas": 75, "Fisica": 80, "English": 88},
    "Gilberto Escamilla": {"Matematicas": 92, "Fisica": 87, "English": 85}
}

average_grades = {}

for student, subjects in grades.items():
    total = sum(subjects.values())
    average = total / len(subjects)
    average_grades[student] = average
    print(f"{student}: {average:.2f}")

print("Average Grades:", average_grades)

#resultados esperados:
#Guillermo Arroyo: 84.33
#Francisco Carrillo: 81.00
#Gilberto Escamilla: 88.00
#Average Grades: {'Guillermo Arroyo': 84.33333333333333, 'Francisco Carrillo': 81.0, 'Gilberto Escamilla': 88.0#
```

**Objetivo:** Calcular el promedio de calificaciones de cada estudiante y crear un nuevo diccionario que contenga únicamente el nombre del estudiante y su promedio.

---

##  task_5 —  Explain in detail, with examples, the .sort() method applied to lists. 

```python
#Explain in detail, with examples, the .sort() method applied to lists. 
datos = [13, 3, 16, 22, 10]
print(f"\nDatos originales: {datos}")
datos.sort()
print(f"Datos ordenados: {datos}")

frutas = ["naranja", "manzana", "kiwi", "pera"]
frutas.sort()
print(f"Frutas ordenadas: {frutas}")
```

 **Objetivo:** Comprender y aplicar el método .sort() para ordenar listas de números y cadenas



##  task_6 — Explain in detail, with examples, the .replace() method applied to strings (str.replace()). 

# Explain in detail, with examples, the .replace() method applied to strings 
string = "gato perro loro pez gallo"
print(f"\nOriginal: {string}")
new_string = string.replace("gato", "tortuga")
print(f"Reemplazado: {new_string}")

text = "I like apples and blueberry are tasty."
new_text = text.replace("apples", "mango").replace("tasty", "delicious")
print(new_text)


# Resultados esperados:
#Original: gato perro loro pez gallo
#Reemplazado: tortuga perro loro pez gallo
#I like mango and blueberry are delicious.
```

 **Objetivo:** usar `.replace()` para modificar listas 

---

## task_7 —Explain in detail the expression s *= n, where s is a mutable sequence 
and n is a number between 0 and 255.


 ##Explain in detail the expression s *= n, where s is a mutable sequence 
#and n is a number between 0 and 255. 
s = [1, 2, 3]
s *= 5
print(f"\n{s}")

s = bytearray([65, 66, 67])
s *= 4
print(s)

s1 = ["a", "b", "c", "d", "f"]
s1 *= 3
print(s1)

s2 = [230, 235, 240, 245, 250]
s2 *= 2
print(s2)

#Resultados esperados
#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
#bytearray(b'ABCABCABCABC')
#'a', 'b', 'c', 'd', 'f', 'a', 'b', 'c', 'd', 'f', 'a', 'b', 'c', 'd', 'f']
#[230, 235, 240, 245, 250, 230, 235, 240, 245, 250]

**Objetivo:** comprender cómo el operador `*=` multiplica secuencias (listas, `bytearray`) repitiendo sus elementos.

---

##  task_8 Explain in detail, with examples, how the input() function works. 



variable = input("\nPrompt message: ")
print(variable)

name = input("Nombre: ")
print("Hello", name)

num1 = int(input("Primer base: "))
num2 = int(input("Segunda altura: "))
total = num1 * num2 / 2
print("El área del triángulo es:", total)

#resultados esperados:

#Prompt message: hola
#hola
#Nombre: Juan Carlos
#Hello Juan Carlos
#Primer base: 56
#Segunda altura: 90
#El área del triángulo es: 2520.0

 **Objetivo:** aplicar el método `input()` para interactuar con el usuario.

---

## task_9-task_12 se simulan errores y se mencinan los resultados





