pikachu_roll = 0
otaku_roll = 0
pulpo_roll = 0
anguila_roll = 0
Eleccion = 0 
productos = 0
total = 0
descuento = 0
cantidad_productos = 0
total_compra = 0
menu = 0

while True:
    print("---Menu---")
    print("1-.Pikachu Roll ($4500)")
    print("2-.Otaku Roll ($5000)")
    print("3-.Pulpo venenoso Roll ($5200)")
    print("4-.Anguila electrica Roll ($4800)")
    print("5-. Salir")
    Eleccion = int(input("Ingrese una opcion: "))
      
    if Eleccion == 1:
        print("Agregaste un Pikachu Roll")
        pikachu_roll += 1
        total += 4500
    elif Eleccion == 2:
        print("Agregaste un Otaku Roll")
        otaku_roll += 1
        total += 5000
    elif Eleccion == 3:
        print("Agregaste Un Pulpo Venenoso Roll")
        pulpo_roll += 1
        total += 5200
    elif Eleccion == 4:
        print("Agregaste un Anguila electrica Roll")
        anguila_roll += 1
        total += 4800
    elif Eleccion == 5:
        if total > 0:
            while True:
                print("---Codigo---")
                print("1-.codigo promocional")
                print("2-.Salir")
                menu = int(input("Ingrese la eleccion(1/2): "))
                if menu == 1:
                    while True:
                        codigo = str(input("Ingrese el codigo (Si quiere volver ingrese X): "))

                        if codigo.lower() == "soyotaku":
                            descuento = (total*0.10)
                            total_compra = (total-descuento)
                            break
                        elif codigo.upper() == "X":
                            print("Volviendo al menu")
                            break
                        else:
                            print("Codigo incorrecto")
                elif menu == 2:
                    break
                else:
                    print("Ingrese una de las opciones")
        break    
    else: 
        print("Opcion invalida")

cantidad_productos = (pikachu_roll + otaku_roll + pulpo_roll + anguila_roll)

if descuento > 0:
    print("-"*40)
    print(f"Total de productos: {cantidad_productos}")
    print("-"*40)
    print(f"Pikachu Roll: {pikachu_roll}")
    print(f"Otaku Roll: {otaku_roll}")
    print(f"Pulpo Venenoso Roll: {pulpo_roll}")
    print(f"Anguila Electrica Roll: {anguila_roll}")
    print("-"*40)
    print(f"Subtotal por pagar: {total}")
    print(f"Descuento por codigo: {descuento}")
    print(f"Total: {total_compra}")
else:
    print("-"*40)
    print(f"Total de productos: {cantidad_productos}")
    print("-"*40)
    print(f"Pikachu Roll: {pikachu_roll}")
    print(f"Otaku Roll: {otaku_roll}")
    print(f"Pulpo Venenoso Roll: {pulpo_roll}")
    print(f"Anguila Electrica Roll: {anguila_roll}")
    print("-"*40)
    print(f"Total: {total}")


