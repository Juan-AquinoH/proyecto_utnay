int= "123"
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

#se cambia el valor por int y el resultado de Error

Traceback (most recent call last):
  File "c:\Users\Lenovo\Desktop\proyecto_utnay\Lab2\task_9.py", line 2, in <module>
    print(f"Valor inicial: {valor} (tipo: {type(valor)})")
                            ^^^^^
NameError: name 'valor' is not defined