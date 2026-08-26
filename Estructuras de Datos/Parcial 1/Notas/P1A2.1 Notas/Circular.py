class NodoLista:
    def __init__(self, objeto, nodo=None):
        self.datos = objeto
        self.siguienteNodo = nodo

    def obtenerObject(self):
        return self.datos

    def obtenerSiguiente(self):
        return self.siguienteNodo

# Definición de la clase Lista
class Lista:
    def __init__(self, nombreLista="lista"):
        self.nombre = nombreLista
        self.primerNodo = None
        self.ultimoNodo = None

    def insertarAlFrente(self, elementoInsertar):
        if self.estaVacia():
            self.primerNodo = self.ultimoNodo = NodoLista(elementoInsertar)
        else:
            self.primerNodo = NodoLista(elementoInsertar, self.primerNodo)

    def insertarAlFinal(self, elementoInsertar):
        if self.estaVacia():
            self.primerNodo = self.ultimoNodo = NodoLista(elementoInsertar)
        else:
            self.ultimoNodo.siguienteNodo = NodoLista(elementoInsertar)
            self.ultimoNodo = self.ultimoNodo.siguienteNodo

    def eliminarDelFrente(self):
        if self.estaVacia():
            raise Exception("ExcepcionListaVacia")

        elementoEliminado = self.primerNodo.datos

        if self.primerNodo == self.ultimoNodo:
            self.primerNodo = self.ultimoNodo = None
        else:
            self.primerNodo = self.primerNodo.siguienteNodo

        return elementoEliminado

    def eliminarDelFinal(self):
        if self.estaVacia():
            raise Exception("ExcepcionListaVacia")

        elementoEliminado = self.ultimoNodo.datos

        if self.primerNodo == self.ultimoNodo:
            self.primerNodo = self.ultimoNodo = None
        else:
            actual = self.primerNodo
            while actual.siguienteNodo != self.ultimoNodo:
                actual = actual.siguienteNodo

            self.ultimoNodo = actual
            self.ultimoNodo.siguienteNodo = None

        return elementoEliminado

    def estaVacia(self):
        return self.primerNodo is None

    def imprimir(self):
        if self.estaVacia():
            print(f"{self.nombre} vacia")
            return

        print(f"La {self.nombre} es:", end=" ")
        actual = self.primerNodo
        while actual is not None:
            print(actual.datos, end=" ")
            actual = actual.siguienteNodo
        print("\n")

# Definición de la excepción ExcepcionListaVacia
class ExcepcionListaVacia(Exception):
    def __init__(self, nombre="Lista"):
        super().__init__(f"{nombre} esta vacia")


class ListaCircular:
    def __init__(self, nombreLista="lista circular"):
        self.nombre = nombreLista
        self.primerNodo = None
        self.ultimoNodo = None

    def insertarAlFrente(self, elementoInsertar):
        if self.estaVacia():
            self.primerNodo = self.ultimoNodo = NodoLista(elementoInsertar)
            self.ultimoNodo.siguienteNodo = self.primerNodo
        else:
            self.primerNodo = NodoLista(elementoInsertar, self.primerNodo)
            self.ultimoNodo.siguienteNodo = self.primerNodo

    def insertarAlFinal(self, elementoInsertar):
        if self.estaVacia():
            self.primerNodo = self.ultimoNodo = NodoLista(elementoInsertar)
            self.ultimoNodo.siguienteNodo = self.primerNodo
        else:
            nuevoNodo = NodoLista(elementoInsertar, self.primerNodo)
            self.ultimoNodo.siguienteNodo = nuevoNodo
            self.ultimoNodo = nuevoNodo

    def eliminarDelFrente(self):
        if self.estaVacia():
            raise Exception("ExcepcionListaVacia")

        elementoEliminado = self.primerNodo.datos

        if self.primerNodo == self.ultimoNodo:
            self.primerNodo = self.ultimoNodo = None
        else:
            self.primerNodo = self.primerNodo.siguienteNodo
            self.ultimoNodo.siguienteNodo = self.primerNodo

        return elementoEliminado

    def eliminarDelFinal(self):
        if self.estaVacia():
            raise Exception("ExcepcionListaVacia")

        elementoEliminado = self.ultimoNodo.datos

        if self.primerNodo == self.ultimoNodo:
            self.primerNodo = self.ultimoNodo = None
        else:
            actual = self.primerNodo
            while actual.siguienteNodo != self.ultimoNodo:
                actual = actual.siguienteNodo

            self.ultimoNodo = actual
            self.ultimoNodo.siguienteNodo = self.primerNodo

        return elementoEliminado

    def estaVacia(self):
        return self.primerNodo is None

    def imprimir(self):
        if self.estaVacia():
            print(f"{self.nombre} vacia")
            return

        print(f"La {self.nombre} es:", end=" ")
        actual = self.primerNodo
        while True:
            print(actual.datos, end=" ")
            actual = actual.siguienteNodo
            if actual == self.primerNodo:
                break
        print("\n")


class NodoListaDoble:
    def __init__(self, objeto, siguiente=None, anterior=None):
        self.datos = objeto
        self.siguienteNodo = siguiente
        self.anteriorNodo = anterior

    def obtenerObject(self):
        return self.datos

    def obtenerSiguiente(self):
        return self.siguienteNodo

    def obtenerAnterior(self):
        return self.anteriorNodo


# Clase para probar la Lista
class PruebaLista:
    @staticmethod
    def main():
        lista = Lista()

        lista.insertarAlFrente(-1)
        lista.imprimir()
        lista.insertarAlFrente(0)
        lista.imprimir()
        lista.insertarAlFinal(1)
        lista.imprimir()
        lista.insertarAlFinal(5)
        lista.imprimir()

        try:
            objetoEliminado = lista.eliminarDelFrente()
            print(f"{objetoEliminado} eliminado")
            lista.imprimir()

            objetoEliminado = lista.eliminarDelFrente()
            print(f"{objetoEliminado} eliminado")
            lista.imprimir()

            objetoEliminado = lista.eliminarDelFinal()
            print(f"{objetoEliminado} eliminado")
            lista.imprimir()

            objetoEliminado = lista.eliminarDelFinal()
            print(f"{objetoEliminado} eliminado")
            lista.imprimir()
        except ExcepcionListaVacia as excepcionListaVacia:
            print(excepcionListaVacia)

# Llamada al método main de PruebaLista
if __name__ == "__main__":
    PruebaLista.main()