import random

secreto=random.randint(1, 100)

intento=int(input("Adivina el número (1-100): "))

diferencia=abs(secreto-intento)

if intento==secreto:
    print("Ganador")
elif diferencia<=2:
    print("Casi, Ganaste el premio de consuelo")
else:
    print("Perdiste")

print(f"(El número secreto era: {secreto})")