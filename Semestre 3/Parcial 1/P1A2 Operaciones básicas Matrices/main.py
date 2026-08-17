from matriz import Matriz


def menu():
    print("--- Matriz 1 ---")
    filas1 = int(input("Filas de la matriz 1: "))
    columnas1 = int(input("Columnas de la matriz 1: "))
    m1 = Matriz(filas1, columnas1)
    m1.llenar()

    print("--- Matriz 2 ---")
    filas2 = int(input("Filas de la matriz 2: "))
    columnas2 = int(input("Columnas de la matriz 2: "))
    m2 = Matriz(filas2, columnas2)
    m2.llenar()

    while True:
        print("")
        print("1) Mostrar matriz 1")
        print("2) Mostrar matriz 2")
        print("3) Sumar matriz 1 mas matriz 2")
        print("4) Restar matriz 1 menos matriz 2")
        print("5) Multiplicar matriz 1 por un escalar")
        print("6) Multiplicar matriz 2 por un escalar")
        print("0) Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            m1.mostrar()
        elif opcion == "2":
            m2.mostrar()
        elif opcion == "3":
            resultado = m1.sumar(m2)
            if resultado != None:
                resultado.mostrar()
        elif opcion == "4":
            resultado = m1.restar(m2)
            if resultado != None:
                resultado.mostrar()
        elif opcion == "5":
            escalar = int(input("Escalar: "))
            resultado = m1.multiplicar_escalar(escalar)
            resultado.mostrar()
        elif opcion == "6":
            escalar = int(input("Escalar: "))
            resultado = m2.multiplicar_escalar(escalar)
            resultado.mostrar()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")


menu()