 class Person:
        def __init__(self, name, age, city):
        self.name = name
        self.age = age
        #self.city = city

    def greet(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.")
# Crear objetos
person1 = Person("Ana", 25, "Mexico")
person2 = Person("Carlos", 50, "New York")
person3 = Person("Julia", 22, "Paris")
# Llamar al método greet()
person1.greet()
person2.greet()
person3.greet()

se comenta un atributo y se obtiene el siguiente error
 
 
 File "c:\Users\Lenovo\Desktop\proyecto_utnay\Lab6\Sesction_1\task_2.py", line 13, in greet 
    print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.")
                                                                                  ^^^^^^^^^  
AttributeError: 'Person' object has no attribute 'city'