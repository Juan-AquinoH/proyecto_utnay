# Lab6 - Python Classes Practice

Este laboratorio contiene una serie de tareas (task_1 a task_6) enfocadas en la creación y manejo de clases en Python.  
Cada sección incluye el objetivo, el error presentado (si existe) y la forma correcta de resolverlo.

---

## Task_1: Clase `Car`

###  Objetivo
Crear una clase llamada `Car` con los atributos `brand`, `model` y `color`.  
Agregar un método `show_info()` que imprima toda la información del auto.  
Después, crear dos objetos de la clase y mostrar su información.

###  Código base
```python
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = colors

#def show_info(self):
        print(f"Car Information: Brand: {self.brand}, Model: {self.model}, Color: {self.color}")

    def __str__(self):
        return f"Car(Brand: {self.brand}, Model: {self.model}, Color: {self.color})"

car1 = Car("Mitsubichi", "L200", "White")
car2 = Car("MG", "MG3", "Blue")

car1.show_info()
car2.show_info()
```

###  Error  (se presenta en task_4)
```
AttributeError: 'Car' object has no attribute 'show_info'
```

### Solución
El método `show_info()` está comentado con `#`, por lo que no existe en la clase.  
Debe **descomentarse** y definirse correctamente dentro de la clase.

 **Corrección:**
```python
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):
        print(f"Car Information: Brand: {self.brand}, Model: {self.model}, Color: {self.color}")

    def __str__(self):
        return f"Car(Brand: {self.brand}, Model: {self.model}, Color: {self.color})"
```

---

## Task_2: Clase `Person`

###  Objetivo
Crear una clase llamada `Person` con los atributos `name`, `age` y `city`.  
Agregar un método `greet()` que muestre un saludo con los datos del objeto.

###  Código base
```python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        #self.city = city

    def greet(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.")
```

###  Error( se presenta en task_5)
```
AttributeError: 'Person' object has no attribute 'city'
```

###  Solución
El atributo `self.city` fue comentado en el constructor (`#self.city = city`),  
por lo que no existe al momento de llamarse en el método `greet()`.

 **Corrección:**
```python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
```



##  Task_3: Clase `BankAccount`

###  Objetivo
Crear una clase `BankAccount` con:
- Atributo de clase `bank = "Central Bank"`.
- Método de instancia `show_balance()` que imprima el saldo.
- Método de clase `show_bank()` que imprima el nombre del banco.
- Método estático `convert_currency(value)` que convierta dólares a pesos (1 USD = 20 MXN).

###  Código base
```python
class BankAccount:
    bank = "Central Bank"

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(f"Client's balance: ${#self.balance}")

    @classmethod
    def show_bank(cls):
        print(f"Bank's name: {cls.bank}")

    @staticmethod
    def convert_currency(value):
        exchange_rate = 20
        pesos = value * exchange_rate
        print(f"${value} in dollars is equivalent to ${pesos} in pesos.")
```

###  Error (se presenta en task_6)
```
SyntaxError: f-string: expecting a valid expression after '{'
```

###  Solución
El carácter `#` dentro de una f-string (`f"..."`) no es válido.  
Debe eliminarse para que Python reconozca la expresión correctamente.

 **Corrección:**
---python
def show_balance(self):
    print(f"Client's balance: ${self.balance}")
----



##  Task_4: Creación de objetos y uso de métodos

###  Objetivo
Instanciar objetos de las clases anteriores (`Car`, `Person`, `BankAccount`) y probar sus métodos.

###  Solución esperada
```python
# Car
car1 = Car("Mitsubichi", "L200", "White")
car2 = Car("MG", "MG3", "Blue")
car1.show_info()
car2.show_info()

# Person
person1 = Person("Ana", 25, "Mexico")
person2 = Person("Carlos", 50, "New York")
person3 = Person("Julia", 22, "Paris")
person1.greet()
person2.greet()
person3.greet()

# BankAccount
account = BankAccount(1000)
account.show_balance()
BankAccount.show_bank()
BankAccount.convert_currency(50)
```

---

##  Task_5: Comprobación de errores comunes

###  Objetivo
Identificar errores comunes en la definición de clases:
- Métodos comentados.
- Atributos omitidos.
- Sintaxis inválida en `f-strings`.

###  Recomendaciones
- No comentar (`#`) líneas que definen métodos o atributos esenciales.
- Revisar sangrías y el uso correcto de `self`.
- Validar siempre las f-strings con `f"Texto {variable}"`.

---

## Task_6: Resultado final esperado

###  Objetivo
Demostrar la ejecución correcta de todas las clases.

###  Salida esperada
```
Car Information: Brand: Mitsubichi, Model: L200, Color: White
Car Information: Brand: MG, Model: MG3, Color: Blue
Hi, my name is Ana, I am 25 years old, and I live in Mexico.
Hi, my name is Carlos, I am 50 years old, and I live in New York.
Hi, my name is Julia, I am 22 years old, and I live in Paris.
Client's balance: $1000
Bank's name: Central Bank
$50 in dollars is equivalent to $1000 in pesos.
```

---

##  Conclusión

Este laboratorio refuerza el uso de:
- Constructores (`__init__`)
- Métodos de instancia, clase y estáticos
- Manejo correcto de `self` y `cls`
- Uso apropiado de f-strings en Python
