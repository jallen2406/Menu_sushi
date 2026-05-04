import random

secreto=random.randint(1, 10)


intento1=int(input("Intento 1: "))
distancia1=abs(secreto - intento1)

if intento1==secreto:
    print("¡Ganaste en el primer intento!")
else:
   
    intento2=int(input("Intento 2: "))
    distancia2=abs(secreto - intento2)

    if intento2==secreto:
        print("¡Ganaste en el segundo intento!")
    else:
        
        if distancia1<distancia2:
            print("El intento 1 estuvo más cerca")
        elif distancia2<distancia1:
            print("El intento 2 estuvo más cerca")
        else:
            print("Ambos intentos estuvieron igual de cerca")

        intento3=int(input("Intento 3: "))

        if intento3==secreto:
            print("¡Ganaste en el último intento!")
        else:
            print(f"Perdiste, el número era {secreto}")