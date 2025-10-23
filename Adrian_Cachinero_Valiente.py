#Prueba Evaluable 1-1T-DAM1-GETAFE
# Adrian Cachinero Valiente
#Tipo B

viaje = []
catalogo = ("Francia":50,4"Italia":20,4 "Alemania":45,9"Inglaterra":70,3)
opcion = ""

print("\n Catalago\n")
print("opcion 1: Añadir viaje al catálogo")
print("opcion 2: Mostrar catálogo")
print("opcion 3: Reservar un destino")
print("opcion 4: Ver reservas")
print("opcion 5: Resumen de coste y días")
print("opcion 6: Salir")

opcion = int(input("Que opcion desea (o 'salir' para terminar): "))


while opcion < 6:
    match opcion:
        case 1:
            print(f"{catalogo}")
            destino = (str(input("Confirma para que destino desea ir (o 'salir' para terminar):")))  
        case 6:
            print("Fin de catalogo")
        case _:
            print("Opcion no valida")


# Pedir la siguiente seleccion
    print("\n Catalago\n")
    print("opcion 1: Añadir viaje al catálogo")
    print("opcion 2: Mostrar catálogo")
    print("opcion 3: Reservar un destino")
    print("opcion 4: Ver reservas")
    print("opcion 5: Resumen de coste y días")
    print("opcion 6: Salir")

    opcion = int(input("Que opcion desea (o 'salir' para terminar): "))