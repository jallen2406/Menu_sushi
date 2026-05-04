import random
aciertos=0

numeros=random.sample(range(1,11),3)

print("Adivina los numeros entre 1 y 10 (3 intentos)")

for num in range(3):
    intento=int(input(f"intento {num+1}: "))
    if intento in numeros: 
        print("Le diste a uno")
    else:
        print("Fallaste")

print("Los numeros secretos eran: ", numeros)

if aciertos == 1:
    print("Ganaste premio menor")
elif aciertos == 2:
    print("Ganaste premio medio")
elif aciertos == 3:
    print("¡Premio mayor!")
else:
    print("No acertaste ninguno")