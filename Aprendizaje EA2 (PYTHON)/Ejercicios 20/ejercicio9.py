limitea=int(input("Ingrese el primer limite: "))
print(f"El limite A seria: {limitea}")
limiteb=int(input("Ingrese el segundo limite: "))
print(f"El limite B seria: {limiteb}")

if limitea>limiteb:
    print("¡Advertencia!, se han invertido los limites")
    limitea, limiteb=limiteb, limitea

import random

secreto=random.randint(limitea, limiteb)
intentos=3

for i in range(intentos):
    intento=int(input("Intente adivinar: "))
    if intento==secreto:
        print(f"Adivinaste, el numero era: {secreto}")
        break
    else:    
        if intento>secreto:
            print("El numero es mayor")
        elif secreto>intento:
            print("El numero es menor")