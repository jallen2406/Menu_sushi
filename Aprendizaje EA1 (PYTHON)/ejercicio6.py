inferior = int(input("Ingrese el límite inferior: "))
superior = int(input("Ingrese el límite superior: "))

if inferior > superior:
    inferior, superior = superior, inferior
    print("Se ingresaron mal los limites, seran invertidos para poder jugar")

import random

numero_secreto = random.randint(inferior, superior)

intento = int(input("Adivina el número: "))

if intento == numero_secreto:
    print("¡Felicidades! Adivinaste el número")
else:
    print(f"No acertaste, El número era {numero_secreto}")