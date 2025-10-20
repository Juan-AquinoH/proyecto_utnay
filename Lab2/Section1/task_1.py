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