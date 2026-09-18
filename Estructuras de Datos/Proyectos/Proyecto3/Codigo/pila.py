# pila.py
# Estructura de datos Pila (LIFO) hecha con un arreglo y un indice llamado tope,
# igual al modelo que vimos en clase con la clase Stack de Java.

CAPACIDAD_MAXIMA = 4


class Pila:
    # Tope = -1 -> vacia.  Tope = capacidad - 1 -> llena.

    def __init__(self, capacidad=CAPACIDAD_MAXIMA):
        self.capacidad = capacidad
        # El arreglo se crea completo desde el inicio y nunca cambia de tamano.
        # Por eso esta pila si se puede llenar, a diferencia de una lista normal.
        self.elementos = [None] * capacidad
        self.tope = -1

    def estaVacia(self):
        return self.tope == -1

    def estaLlena(self):
        return self.tope == self.capacidad - 1

    def apilar(self, dato):
        if self.estaLlena():        # sin esto habria desbordamiento
            return False

        self.tope = self.tope + 1
        self.elementos[self.tope] = dato
        return True

    def desapilar(self):
        if self.estaVacia():        # subdesbordamiento
            return None

        dato = self.elementos[self.tope]
        self.elementos[self.tope] = None    # se limpia para no dejar la referencia vieja
        self.tope = self.tope - 1
        return dato

    def verTope(self):
        if self.estaVacia():
            return None

        return self.elementos[self.tope]

    def cantidad(self):
        return self.tope + 1

    def vaciar(self):
        self.elementos = [None] * self.capacidad
        self.tope = -1

    # Regresa solo las casillas ocupadas. Sirve para imprimir la pila en pantalla.
    def listaElementos(self):
        return self.elementos[0:self.tope + 1]
