import random

intentos=3
pista=False

numero_secreto=random.randint(1, 50)

for num in range(intentos):
    intento=int(input(f"intento {num+1} de {intentos}: "))

    if intento == numero_secreto:
        print("Felicidades, adivinaste el numero")
        break
    
    else:
        print("Incorrecto")
        if numero_secreto % 2 == 0:
            print("El numero es PAR")
        else:
            print("El numero es IMPAR") 

else:
    print("Se acabaron los intentos")

print(f"El numero era: {numero_secreto}")