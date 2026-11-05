# main.py
# Menu de consola del navegador y las funciones que imprimen la pagina actual
# y las dos pilas. Toda la logica del historial esta en la clase Navegador.
#
# Para correrlo:  python main.py

from navegador import Navegador


def mostrarPaginaActual(navegador):
    print("PAGINA ACTUAL:")

    # Al abrir el programa todavia no hay ninguna pagina cargada
    if navegador.paginaActual == None:
        print("   (ninguna, visita una pagina para empezar)")
    else:
        print("   " + navegador.paginaActual.titulo)
        print("   " + navegador.paginaActual.verDescripcion())


def mostrarPila(nombre, pila):
    print(nombre + "  (" + str(pila.cantidad()) + " de " +
          str(pila.capacidad) + ")")

    if pila.estaVacia():
        print("   [vacia]")
        return

    elementos = pila.listaElementos()
    posicion = len(elementos) - 1

    # Se recorre al reves para que en pantalla se vea como una pila de verdad,
    # con el ultimo que entro hasta arriba
    while posicion >= 0:
        if posicion == len(elementos) - 1:
            etiqueta = " <- TOPE"
        else:
            etiqueta = ""

        print("   " + str(posicion + 1) + ". " + str(elementos[posicion]) +
              etiqueta)
        posicion = posicion - 1


def mostrarEstado(navegador):
    print("")
    print("=" * 60)
    print("            NAVEGADOR WEB - PILAS (LIFO)")
    print("=" * 60)
    mostrarPaginaActual(navegador)
    print("-" * 60)
    mostrarPila("PILA ATRAS (Back stack)", navegador.pilaAtras)
    print("-" * 60)
    mostrarPila("PILA ADELANTE (Forward stack)", navegador.pilaAdelante)
    print("=" * 60)


def mostrarSitios(navegador):
    print("")
    print("Sitios que conoce el navegador:")

    sitios = navegador.sitiosDisponibles()
    numero = 1

    for sitio in sitios:
        print("   " + str(numero) + ") " + sitio)
        numero = numero + 1

    print("   (cualquier otra direccion sale como error 404)")


def mostrarMenu():
    print("")
    print("1. Visitar una pagina nueva")
    print("2. Back    (regresar a la pagina anterior)")
    print("3. Forward (avanzar a la pagina siguiente)")
    print("4. Exit    (salir del navegador)")


def main():
    navegador = Navegador()
    salir = False

    print("Bienvenido al navegador web hecho con pilas.")

    while salir == False:
        # Se reimprime en cada vuelta para que la pagina actual y las pilas
        # se vean en todo momento
        mostrarEstado(navegador)
        mostrarMenu()

        opcion = input("Elige una opcion (1-4): ").strip()

        if opcion == "1":
            mostrarSitios(navegador)
            url = input("Escribe la URL: ")
            mensaje = navegador.visitar(url)
            print(">> " + mensaje)

        elif opcion == "2":
            mensaje = navegador.retroceder()
            print(">> " + mensaje)

        elif opcion == "3":
            mensaje = navegador.avanzar()
            print(">> " + mensaje)

        elif opcion == "4":
            salir = True
            print(">> Saliendo del navegador. Hasta luego.")

        else:
            print(">> Opcion no valida, escribe un numero del 1 al 4.")


# Solo arranca el menu si se ejecuta este archivo y no si se importa
if __name__ == "__main__":
    main()
