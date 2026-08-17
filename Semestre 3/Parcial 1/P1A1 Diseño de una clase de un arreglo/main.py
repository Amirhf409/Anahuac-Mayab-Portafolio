from vector import Vector


def menu():
    capacidad = int(input("Capacidad del vector: "))
    v = Vector(capacidad)
    v.seleccion_numero()

    while True:
        print("\n1) Recorrer")
        print("2) Insertar")
        print("3) Eliminar")
        print("4) Ordenar ascendente")
        print("5) Ordenar descendente")
        print("6) Buscar")
        print("0) Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            v.recorrer()
        elif opcion == "2":
            valor = int(input("Valor a insertar: "))
            indice = int(input("En que indice: "))
            v.insertar(valor, indice)
            v.recorrer()
        elif opcion == "3":
            indice = int(input("Indice a eliminar: "))
            v.eliminar(indice)
            v.recorrer()
        elif opcion == "4":
            v.ordenar_ascendente()
            v.recorrer()
        elif opcion == "5":
            v.ordenar_descendente()
            v.recorrer()
        elif opcion == "6":
            valor = int(input("Que valor buscas? "))
            idx = v.buscar(valor)
            print(f"Encontrado en el indice {idx}" if idx != -1 else "No encontrado")
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")


menu()