class Mascota:
    #  Atributos de clase (compartidos por todas las instancias)
    especie = "Animal doméstico"
    total_mascotas = 0

    # Constructor con atributos de instancia
    def __init__(self, nombre, edad):
        self.nombre = nombre      # atributo de instancia
        self.edad = edad          # atributo de instancia
        Mascota.total_mascotas += 1  # incrementa el contador de mascotas

    # Método de instancia
    def saludar(self):
        return f"Presentacion, soy {self.nombre} y tengo {self.edad} años."

    #  Método de clase
    @classmethod
    def cantidad_mascotas(cls):
        return f"Actualmente hay {cls.total_mascotas} mascotas registradas."

    #  Método estático
    @staticmethod
    def info():
        return "Las mascotas son animales que viven con los humanos."


# --------------------  uso y aplicación--------------------
# Crear instancias
m1 = Mascota("persy", 15)
m2 = Mascota("Mila", 5)

# Usar método de instancia
print(m1.saludar())  

# Usar método de clase
print(Mascota.cantidad_mascotas())

# Usar método estático
print(Mascota.info())
