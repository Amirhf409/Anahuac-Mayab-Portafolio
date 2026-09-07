class Hanoi:
    def __init__(self, n=3):
        self.discos = n

        #Crear las 3 torres
        self.torre1 = Pila()
        self.torre2 = Pila()
        self.torre3 = Pila()

        #Insertar los discos en una de las torres
        for i in range (n, 0, -1):
            self.torre1.push(i)
        
        self.mostrarTorres()

        #invocar el método recursivo de Hanoi
        self.hanoi(n, 1, 2, 3)

    def mostrarTorres(self):
        print("\nTorre 1:", end=" ")
        self.torre1.mostrar()

        print("\nTorre 2:", end=" ")
        self.torre2.mostrar()

        print("\nTorre 3:", end=" ")
        self.torre3.mostrar()

        print("\n---------------------------------")

    def hanoi(self, n, origen, destino, auxiliar):
        if n > 0:
            self.hanoi(n-1, origen, auxiliar, destino)

            torreOrigen = self.obtenerTorre(origen)
            torreDestino = self.obtenerTorre(destino)

            disco = torreOrigen.pop() #Se extrae el disco de la torre origen
            torreDestino.push(disco) #Se inserta el disco extraido en la torre destino

            self.mostrarTorres()

            self.hanoi(n-1, auxiliar, destino, origen)

    def obtenerTorre(self, num):
        if num == 1:
            return self.torre1
        elif num == 2:
            return self.torre2
        else: return self.torre3

class Nodo:
    """Nodo para la lista enlazada utilizada en la pila."""

    def __init__(self, valor, siguiente=None):
        self.elemento = valor
        self.sgte = siguiente

    def obtener_elemento(self):
        return self.elemento

    def obtener_sgte(self):
        return self.sgte


class Pila:
    """Implementación de una pila usando nodos enlazados."""

    def __init__(self):
        self.tope = None
        self.nDatos = 0

    def esta_vacia(self):
        return self.tope is None

    def vaciar(self):
        self.tope = None
        self.nDatos = 0

    def tamanio(self):
        return self.nDatos

    def top(self):
        return None if self.esta_vacia() else self.tope.elemento

    def pop(self):
        if self.esta_vacia():
            return None

        dato = self.tope.elemento
        self.tope = self.tope.sgte
        self.nDatos -= 1
        return dato

    def push(self, x):
        self.tope = Nodo(x, self.tope)
        self.nDatos += 1

    def mostrar(self):
        actual = self.tope

        while actual is not None:
            print(actual.elemento, end=" ")
            actual = actual.sgte