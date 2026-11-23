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
        # Regresa la PC que mandó el trabajo, o None si la cola está llena.
        if self.esta_llena():
            return None

        computadora = random.choice(["PC1", "PC2", "PC3", "PC4", "PC5"])
        self.cola.append(computadora)
        return computadora

    def imprimir_documento(self):
        # Quita el primer trabajo de la cola respetando el principio FIFO.
        # Regresa la PC que se atendió, o None si la cola está vacía.
        if self.esta_vacia():
            return None

        return self.cola.pop(0)

    def mostrar_cola(self):
        # Regresa los trabajos pendientes en el orden en que serán atendidos.
        lista = []
        for posicion in range(len(self.cola)):
            lista.append(str(posicion + 1) + ". " + self.cola[posicion])
        return lista
