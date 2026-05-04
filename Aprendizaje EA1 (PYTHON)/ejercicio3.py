descuento=0
matricula=90000
mes=int(input("Ingrese el mes de pago(1/12): "))

if mes<3:
    print("Obtiene un descuento del 15%")
    descuento=0.15
    total=matricula-(matricula*descuento)
elif mes>3:
    print("Se le agrega un 5% por el retraso")
    descuento=1.05
    total=(matricula*descuento)
else:
    print("Debera pagar el valor real")
    descuento=1
    total=(matricula*descuento)

print(f"Debera pagar: {total}")