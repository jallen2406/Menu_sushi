num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

pares=0
impar=0

for num in [num1, num2, num3]:
    if num%2==0:
        pares+=1
    else:
        impar+=1

print(f"La cantidad de numeros pares es: {pares}")
print(f"La cantidad de numeros pares es: {impar}")

suma=(num1+num2+num3)

if suma>100:
    print("La suma es mayor a 100")
else: 
    print("La suma no es mayor a 100")