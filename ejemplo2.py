class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    # Método de instancia
    def maullar(self):
        print(f"{self.nombre} está maullando")

    # Otro método de instancia que llama a 'maullar'
    def maullar2(self):
        self.maullar()

    # Método para obtener el nombre
    def set_name(self):
        return self.nombre


# ---------------- Uso ----------------
objeto1 = Gato("Bombón")

# Llamar métodos correctamente
objeto1.maullar2()   # llama a maullar dentro de maullar2
objeto1.maullar()    # llama directamente a maullar

# Obtener el nombre usando set_name
print(objeto1.set_name())

       
    

