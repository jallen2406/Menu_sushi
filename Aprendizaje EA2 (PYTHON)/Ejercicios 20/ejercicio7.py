presupuesto=int(input("Ingrese su presupuesto: "))

import random

dado1=random.randint(1,6)
dado2=random.randint(1,6)

jugador1=dado1
jugador2=dado2

if jugador1>jugador2:
    print("Ganas $10.000")
    print(f"Tu numero es: {dado1} y el de tu oponente fue: {dado2}")
    dinero=10000
    total=(presupuesto+dinero)
elif jugador1==jugador2:
    print("Nadie gana, tu presupuesto es el mismo")
    print(f"Tu numero es: {dado1} y el de tu oponente fue: {dado2}")
    dinero=0
    total=(presupuesto-dinero)
elif jugador2>jugador1:
    print("Perdiste y te quedan $5.000")
    print(f"Tu numero es: {dado1} y el de tu oponente fue: {dado2}")
    dinero=5000
    total=(presupuesto-dinero)

print("-"*50)

print("---RESUMEN---")
print(f"Tu monto final es: ${total}")