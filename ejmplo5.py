# ---------------- Clase base ----------------
class Animal:
    # Atributo de clase
    reino = "Animalia"

    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo de instancia
        self.edad = edad      # atributo de instancia

    # Método de instancia
    def comer(self):
        print(f"{self.nombre} está comiendo.")

    # Método de clase
    @classmethod
    def reino_animal(cls):
        print(f"Todos los animales pertenecen al reino {cls.reino}.")

    # Método estático
    @staticmethod
    def informacion():
        print("Los animales son seres vivos que se alimentan y se reproducen.")


# ---------------- Herencia simple ----------------
class Gato(Animal):
    def dormir(self):
        print(f"{self.nombre} está durmiendo.")


# ---------------- Otra clase base ----------------
class Mascota:
    def jugar(self):
        print("La mascota está jugando.")

    # Método estático
    @staticmethod
    def cuidados():
        print("Las mascotas requieren alimentación, ejercicio y cariño.")


# ---------------- Herencia múltiple ----------------
class Perro(Animal, Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # inicializa Animal
        self.raza = raza               # atributo propio

    def comer(self):
        super().comer()  # llama al método de Animal
        print(f"{self.nombre} de raza {self.raza} también ha comido su comida favorita.")


# ---------------- Uso ----------------
# Herencia simple
mi_gato = Gato("Michi", 3)
mi_gato.comer()
mi_gato.dormir()
Gato.reino_animal()
Gato.informacion()

print("\n----------------\n")

# Herencia múltiple
mi_perro = Perro("Firulais", 5, "Labrador")
mi_perro.comer()       # método sobreescrito
mi_perro.jugar()       # método de Mascota
Perro.reino_animal()   # método de clase heredado
Perro.informacion()    # método estático heredado
Perro.cuidados()       # método estático de Mascota


