base=25000

edad=int(input("Ingrese su edad: "))
residente=str(input("¿Es residente de la comuna?(si/no): "))

descuento=0

if residente.lower()=="si" and edad>=60:
    print(f"Obtiene un 70% de descuento")
    descuento=(base*0.70)
elif residente.lower()=="si" and edad<60:
    print(f"Obtiene un 30% de descuento")
    descuento=(base*0.30)
elif residente.lower()=="no":
    print("No obtiene descuento")

total=(base-descuento)

print("-"*50)

print(f"Su edad: {edad}")
print(f"¿Es residente?: {residente}")
print(f"El total a pagar es: {total}")