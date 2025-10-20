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