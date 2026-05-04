print("---MENU---")
print("1-. Moto")
print("2-. Auto")
print("3-. Camion")
vehiculo=int(input("Ingrese el tipo de vehiculo(1/3): "))
hora=int(input("Ingrese la hora del dia(1/23): "))
finde=str(input("¿Es finde de semana?(Si/No): "))

recargo2=0
recargo=0


if vehiculo==1:
        base=1000
        vehiculo="Moto"
elif vehiculo==2:
        base=2500
        vehiculo="Auto"
elif vehiculo==3:
        base=5000
        vehiculo="Camion"
        

if hora>=7 and hora<=9 or hora>=18 and hora<=20:
    recargo=(base*0.50)

if finde.lower()=="si":
    recargo2=500

total=(base+recargo+recargo2)

print("-"*50)
print(f"Vehiculo: {vehiculo}")
print(f"Hora: {hora}")
print(f"¿Finde de semana: {finde}")

print("-"*50)

print(f"Resultado: Base ${base} + Recargo Hora Punta ${recargo} + Mantenimiento ${recargo2}")
print(f"Total Peaje: ${total}")