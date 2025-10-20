#. Create a class named Car with the following attributes: brand, model, and 
#color. Add a method called show_info() that prints the full information of the car. 
#Then, create two objects of the Car class with different values and call the method 
#to display their information. 
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):
        print(f"Car Information: Brand: {self.brand}, Model: {self.model}, Color: {self.color}")

    def __str__(self):
        return f"Car(Brand: {self.brand}, Model: {self.model}, Color: {self.color})"


#  Crear objetos 
car1 = Car("Mitsubichi", "L200", "White")
car2 = Car("MG", "MG3", "Blue")

# Usar show_info()
car1.show_info()
car2.show_info()

#  imprimir con  a __str__
print(car1)
print(car2)

   # Resultados
   #Car Information: Brand: Mitsubichi, Model: L200, Color: White
   #Car Information: Brand: MG, Model: MG3, Color: Blue
   #Car(Brand: Mitsubichi, Model: L200, Color: White)
   #Car(Brand: MG, Model: MG3, Color: Blue)
