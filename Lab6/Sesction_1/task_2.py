#Create a class named Person with a constructor that receives the 
#parameters name, age, and city. Add a method called greet() that displays a 
#message such as: "Hi, my name is Ana, I am 25 years old, and I live in Mexico." 
#Create three objects of the Person class and make each one call the greet() 
#method.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

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
# Resultados
#Hi, my name is Ana, I am 25 years old, and I live in Mexico.
#Hi, my name is Carlos, I am 50 years old, and I live in New York.
#Hi, my name is Julia, I am 22 years old, and I live in Paris.
 