beca=0
puntaje=int(input("Ingrese su puntaje: "))
ranking=int(input("Ingrese su ranking: "))

if puntaje>800 and ranking>900:
    print("Obtiene una beca del 100%")
elif puntaje>700 and ranking>850:
    print("Obtiene una beca del 50%")
else:
    print("Debe redir el examen de admision")