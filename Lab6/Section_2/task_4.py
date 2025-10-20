 class Car:
        def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    #def show_info(self):
        print(f"Car Information: Brand: {self.brand}, Model: {self.model}, Color: {self.color}")
 
 Se comenta def show_inf(self) y se tiene el siguiente error
 
 
  File "c:\Users\Lenovo\Desktop\proyecto_utnay\Lab6\Sesction_1\task_1.py", line 23, in <module>
    car1.show_info()
    ^^^^^^^^^^^^^^
AttributeError: 'Car' object has no attribute 'show_info'

