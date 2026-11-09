import random


class ColaImpresion:

    def __init__(self, capacidad):
        # Guarda los trabajos pendientes y la capacidad máxima de la cola.
        self.cola = []
        self.capacidad = capacidad

    def esta_vacia(self):
        # Devuelve True si no existen trabajos pendientes.
        return len(self.cola) == 0

    def esta_llena(self):
        # Devuelve True si la cola alcanzó su capacidad máxima.
        return len(self.cola) >= self.capacidad

    def agregar_trabajo(self):
        # Agrega al final de la cola un trabajo enviado por una PC aleatoria.
        if self.esta_llena():
            print("\nLa cola de impresión está LLENA")

        else:
            computadora = random.choice(
                ["PC1", "PC2", "PC3", "PC4", "PC5"]
            )

            self.cola.append(computadora)

            print(f"\nTrabajo agregado desde {computadora}")

            self.mostrar_cola()

    def imprimir_documento(self):
        # Elimina el primer trabajo de la cola respetando el principio FIFO.
        if self.esta_vacia():
            print("\nLa cola de impresión está VACÍA")

        else:
            computadora = self.cola.pop(0)

            print(f"\nImprimiendo documento de {computadora}")
            print(f"{computadora} está siendo atendida")

            self.mostrar_cola()

    def mostrar_cola(self):
        # Muestra los trabajos pendientes en el orden en que serán atendidos.
        if self.esta_vacia():
            print("\nLa cola de impresión está VACÍA")

        else:
            print("\nCola de impresión:")

            for posicion in range(len(self.cola)):
                print(f"{posicion + 1}. {self.cola[posicion]}")


def mostrar_menu():
    # Muestra las opciones disponibles para el usuario.
    print("\n----- COLA DE IMPRESIÓN -----")
    print("1. Agregar trabajo de impresión")
    print("2. Imprimir documento")
    print("3. Mostrar cola de impresión")
    print("4. Salir")


def main():
    # Crea una cola con capacidad máxima de 6 trabajos.
    impresora = ColaImpresion(6)

    opcion = ""

    while opcion != "4":

        mostrar_menu()

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            impresora.agregar_trabajo()

        elif opcion == "2":
            impresora.imprimir_documento()

        elif opcion == "3":
            impresora.mostrar_cola()

        elif opcion == "4":
            print("\nPrograma finalizado.")

        else:
            print("\nOpción no válida.")


main()
