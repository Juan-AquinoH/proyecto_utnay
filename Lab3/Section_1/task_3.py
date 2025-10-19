import rando

# Genera un número aleatorio entre 1 y 100
secret_number = random.randint(1, 100)

print(" ¡Bienvenido al juego de adivinar números!")
print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

attempts = 0
guess = 0  # Inicializa la suposición para entrar en el bucle

# Sigue preguntando hasta que el usuario adivine correctamente
while guess != secret_number:
    try:
        guess = int(input("Introduce tu suposición: "))
        attempts += 1

        if guess < secret_number:
            print("El número es más alto. ¡Inténtalo de nuevo!")
        elif guess > secret_number:
            print("El número es más bajo. ¡Inténtalo de nuevo!")
        else:
            print(f" ¡Correcto! Lo adivinaste en {attempts} intentos.")
    except ValueError:
        print(" Por favor, introduzca un número válido.")
        
         #¡Bienvenido al juego de adivinar números!
#Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?
#Introduce tu suposición: 70
#El número es más bajo. ¡Inténtalo de nuevo!
#Introduce tu suposición: 50
#El número es más alto. ¡Inténtalo de nuevo!
#Introduce tu suposición: 60
#El número es más alto. ¡Inténtalo de nuevo!
#Introduce tu suposición: 65
#El número es más bajo. ¡Inténtalo de nuevo!
#Introduce tu suposición: 64
#El número es más bajo. ¡Inténtalo de nuevo!
#Introduce tu suposición: 63
# ¡Correcto! Lo adivinaste en 6 intentos.