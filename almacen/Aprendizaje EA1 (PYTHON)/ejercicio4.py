print("Ingrese la cantidad solicitada de lo contrario finalizara el proceso")
print("-"*60)
quintil=int(input("Ingresa tu quintil (1/5): "))
promedio=float(input("Ingresa el promedio(1.0/7.0): "))
print("-"*60)

if 1<=quintil<=5 and 1<=promedio<=7:
    print("---Quintil registrado---")
    print("---Promedio registrado---")
else:
    print("Error: datos no valido, vuelva a ingresar..")
