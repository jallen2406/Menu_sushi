import random 

secreto1=random.randint(1,5)
secreto2=random.randint(1,5)
numero_pista=random.randint(1,5)

secreto=(secreto1+secreto2)
intentos=0

intento=int(input("Ingrese un numero: "))
if intentos==3:
    intentos=intentos-1
    print("Adivinaste el numero")
else:
    if secreto<intento:
        print("El numero es menor")
    elif secreto>intento:
        print("El numero es mayor")
    
    intento=int(input("Ingrese un numero: "))

    if intentos==2:
        intentos=intentos-1
        print("Adivinaste el numero")
    else:
        pista=(secreto+numero_pista)
        if secreto<intento:
            print(f"El numero es menor, Pista: Una de las llaves es: {pista}")
        elif secreto>intento:
            print(f"El numero es mayor, Pista: Una de las llaves es: {pista}")

        intento=int(input("Ingrese un numero: "))

        if intentos==1:
            intentos=intentos-1
            print("Adivinaste el numero")
        else: 
            print("Se te acabaron los intentos")

print("-"*50)

print(f"El numero secreto era: {secreto}")