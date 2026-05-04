descuento=0
distancia=int(input("Ingrese la distancia del colegio con su casa: "))
ingreso=int(input("Registre sus ingresos: "))

if distancia>10 and ingreso<500000:
    print("Obtiene un bono de $50.000")
    descuento=50000
elif distancia>10 and ingreso>=500000:
    print("Obtiene un bono de $20.000")
    descuento=20000
elif distancia<=10:
    print("No obtiene ningun bono")
