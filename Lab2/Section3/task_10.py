 #Perform operations (addition, subtraction, multiplication, and division) 
#using int and float numbers. Print the results and check the data type of each result. 
num_int = 1500
num_int = 234.90
print(f"\nNúmero entero: {num_int} (tipo: {type(num_int)})")
addition = num_int + num_float
print(f"Suma: {addition} (tipo: {type(addition)})")
subtraction = num_int - num_float
print(f"Resta: {subtraction} (tipo: {type(subtraction)})")
multiplication = num_int * num_float
print(f"Multiplicación: {multiplication} (tipo: {type(multiplication)})")
division= num_int / num_float
print(f"División: {division} (tipo: {type(division)})")

#se cambia el valor  float por int


Número entero: 234.9 (tipo: <class 'float'>)
Traceback (most recent call last):
  File "c:\Users\Lenovo\Desktop\proyecto_utnay\Lab2\task_10.py", line 6, in <module>
    addition = num_int + num_float
                         ^^^^^^^^^
NameError: name 'num_float' is not defined