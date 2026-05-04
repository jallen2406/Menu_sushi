promedio=float(input("Ingrese su promedio(1.0/7.0): "))
quintil=int(input("Ingrese su quintil(1/5): "))

if promedio>6.5 and quintil<=2:
    print("Usted obtiene un computador")
elif promedio>6.5 and 3<=quintil<=5:
    print("Usted recibe una tablet")
elif promedio<=6.5:
    print("Recibe un diploma")