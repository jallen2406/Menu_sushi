import random

secreto=random.randint(1,50)

intento1=int(input("Ingrese el primer intento(1-50): "))   
if intento1==secreto:
    print(f"Adivinaste, el numero era: {secreto}")
elif intento1<secreto:
    print("Fallaste, el numero es mayor")
else:
    print("Fallaste, el numero es menor")

intento2=int(input("Intente nuevamente(1-50): "))
if intento2==secreto:
    print(f"Adivinaste el numero: {secreto}")
else:
    if secreto %2==0:
        print("El numero es par")
    else:
        print("El numero es impar")

print("-"*50)

print("---Resumen---")
print(f"El numero secreto era: {secreto}")