quintil=int(input("Ingrese su quintil (1/5): "))
print(" ---Menu---")
print("1.- Norte")
print("2.- Centro")
print("3.- Sur")
zona=int(input("Ingrese su zona de vivienda (1/3): "))
integrantes=int(input("Ingrese la cantidad de integrantes: "))

base=0
bono=0

if 1<=quintil<=2 and zona==3:
    base=800000
elif 1<=quintil<=2 and zona==2:
    base=550000
elif quintil==3 and 1 <=zona<= 3:
    base = 300000
elif 4<=quintil<=5 and 1<=zona<=3:
    base = 0

print(f"El subsidio base es: {base}")

if integrantes>5:
    print("Obtiene un bono adicional")
    bono=base * 0.1

total=bono+base

print("-"*50)
print(f"Su quintil: {quintil}")
print(f"Su zona es: {zona}")
print(f"Su integrantes: {integrantes}")
print(f"Su subsidio es: {base}")
print(f"Su total es: {total}")