edad=int(input("Ingrese su edad: "))
print("-"*50)
print("---MENU---")
print("1- Sedan")
print("2- Camioneta")
print("-"*50)
vehiculo=int(input("Tipo de vehiculo: "))
accidente=str(input("¿Has tenido algun accidente?(si/no): "))

base=0
descuento=0

if 18<=edad<=25 and vehiculo==1:
    base+=45000
elif 18<=edad<=25 and vehiculo==2:
    base+=60000
elif edad>25 and vehiculo==1:
    base+=30000
elif edad>25 and vehiculo==2:
    base+=40000

if accidente.lower()=="no":
    print("Obtiene un 15% de descuento")
    descuento=base * 0.15

total=(base-descuento)

print("-"*50)

print(f"Edad: {edad}")
print(f"Vehiculo: {vehiculo}")
print(f"¿Ha tenido accidente?: {accidente}")
print(f"Precio con descuento: {total}")