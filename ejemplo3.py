# ---------------- Clase base ----------------
class Animal:
    habitad = "Terrestre"

    def __init__(self, name, especie, edad):
        self.name = name
        self.especie = especie
        self.edad = edad

    def comer(self):
        print(f"{self.name} está comiendo.")


# ---------------- Clase hija ----------------
class Perro(Animal):
    def __init__(self, name, especie, color, tamaño, edad):
        # Llamar al constructor de la clase base
        super().__init__(name, especie, edad)
        self.color = color
        self.tamaño = tamaño

    # Sobrescribir el método comer
    def comer(self):
        super().comer()  # Llama al método comer de Animal
        print("y ya le dio el mal del puerco.")


# ---------------- Crear objeto ----------------
objeto1 = Perro("Firulais", "Canina", "Marrón", "Mediano", 5)

# Llamar métodos
print(f"Nombre: {objeto1.name}")
print(f"Especie: {objeto1.especie}")
print(f"Edad: {objeto1.edad}")
print(f"Color: {objeto1.color}")
print(f"Tamaño: {objeto1.tamaño}")
print(f"Habitad: {objeto1.habitad}")

objeto1.comer()



    
        