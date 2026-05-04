nota=float(input("Ingrese su promedio de notas: "))
tramo=str(input("Ingrese su tramo (A/B): "))

base=0

if nota>6.5 and tramo.lower()=="a":
    base=60000
elif nota>6.5 and tramo.lower()=="b":
    base=40000
elif 5.5<=nota<=6.5 and tramo.lower()=="a":
    base=30000
elif 5.5<=nota<=6.5 and tramo.lower()=="a":
    base=20000
else:
    print("No obtienes el beneficio")

print("-"*50)

print(f"Promedio: {nota}")
print(f"Tramo (A/B): {tramo}")
print(f"Recibe un bono de: {base}")