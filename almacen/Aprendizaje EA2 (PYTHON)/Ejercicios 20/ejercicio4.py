edad=int(input("Ingrese su edad: "))
sueldo=int(input("Ingrese su sueldo bruto: "))

descuento=0
base=0

if 18<=edad<=24 and sueldo<450000:
    descuento=(sueldo*0.20)
    base=descuento
    print(f"Recibe un 20% del sueldo como subsidio: {descuento}")
elif 18<=edad<=24 and 450000<=sueldo<=600000:
    print("Recibe un monto de $80.000 ")
    base=80000


print("-"*50)

print(f"Edad: {edad}")
print(f"Sueldo: {sueldo}")
print(f"El subsidio calculado es: {base}")