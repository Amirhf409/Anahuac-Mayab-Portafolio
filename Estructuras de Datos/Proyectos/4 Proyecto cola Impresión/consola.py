# Versión de consola del proyecto (menú con print e input).
# Para correrla: python consola.py

from cola_impresion import ColaImpresion


def mostrar_menu():
    # Muestra las opciones disponibles para el usuario.
    print("\n----- COLA DE IMPRESIÓN -----")
    print("1. Agregar trabajo de impresión")
    print("2. Imprimir documento")
    print("3. Mostrar cola de impresión")
    print("4. Salir")


def imprimirCola(impresora):
    # Imprime la cola o el aviso de que está vacía.
    if impresora.esta_vacia():
        print("\nLa cola de impresión está VACÍA")
    else:
        print("\nCola de impresión:")
        for linea in impresora.mostrar_cola():
            print(linea)


def main():
    # Crea una cola con capacidad máxima de 6 trabajos.
    impresora = ColaImpresion(6)

    opcion = ""

    while opcion != "4":

        mostrar_menu()

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            computadora = impresora.agregar_trabajo()
            if computadora == None:
                print("\nLa cola de impresión está LLENA")
            else:
                print(f"\nTrabajo agregado desde {computadora}")
                imprimirCola(impresora)

        elif opcion == "2":
            computadora = impresora.imprimir_documento()
            if computadora == None:
                print("\nLa cola de impresión está VACÍA")
            else:
                print(f"\nImprimiendo documento de {computadora}")
                print(f"{computadora} está siendo atendida")
                imprimirCola(impresora)

        elif opcion == "3":
            imprimirCola(impresora)

        elif opcion == "4":
            print("\nPrograma finalizado.")

        else:
            print("\nOpción no válida.")


main()
