#Given a list or tuple, identify the element with the maximum value, the 
#element with the minimum value, and the length of the list. 
#Note: You may only use the list methods covered in class; using len(), min(), max(), 
#or any control structures is prohibited. 
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