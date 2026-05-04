import random

inferior=int(input("Ingrese un numero inferior: "))
superior=int(input("Ingrese un numero superior: "))

intentos=3
numero=random.randint(inferior, superior)
secreto=numero*2

print("-"*10,"COMIENZA EL JUEGO", "-"*10)

for i in range(intentos):
    intento=int(input("Ingrese el numero: "))
    if intento==secreto:
        print(f"Has adivinado: {secreto}")
    elif secreto>intento:
        print("El numero es mayor")
    elif secreto<intento:
        print("El numero es menor")
else:
    print("-"*50)
    print("---Juego terminado---")
    print(f"El numero secreto era: {secreto}")