import random

intentos=int(input("Ingresa la cantidad de intentos: "))

numero_secreto=random.randint(1, 100)

for num in range(intentos):
    intento=int(input(f"intento {num+1} de {intentos}: "))
    diferencia=abs(numero_secreto-intento)

    if intento == numero_secreto:
        print("Felicidades, adivinaste el numero")
        break
    
    else:
        print("Incorrecto")
        if diferencia<5:
            print("¡Estas caliente!")
        elif diferencia>20:
            print("Estas frio")
        
else:
    print("-"*40)
    print("Se acabaron los intentos")

print(f"El numero era: {numero_secreto}")