# grafo.py
# Clase Grafo: guarda los pueblos y las carreteras con una lista de adyacencia.
# La lista de adyacencia es un diccionario donde cada pueblo tiene
# la lista de carreteras que salen de el.

from pueblo import Pueblo
from carretera import Carretera


class Grafo:

    def __init__(self):
        self.pueblos = {}       # nombre -> objeto Pueblo
        self.adyacencia = {}    # nombre -> lista de objetos Carretera

    def agregarPueblo(self, pueblo):
        self.pueblos[pueblo.nombre] = pueblo
        self.adyacencia[pueblo.nombre] = []

    # El grafo es no dirigido: si hay carretera de A a B tambien hay de B a A
    def agregarCarretera(self, origen, destino, distancia):
        self.adyacencia[origen].append(Carretera(destino, distancia))
        self.adyacencia[destino].append(Carretera(origen, distancia))

    def vecinos(self, nombre):
        return self.adyacencia[nombre]

    def nombresPueblos(self):
        return list(self.pueblos.keys())

    # Regresa los km de la carretera directa entre a y b, o None si no hay
    def distanciaDirecta(self, a, b):
        for carretera in self.adyacencia[a]:
            if carretera.destino == b:
                return carretera.distancia
        return None

    # Lista de carreteras sin repetir (A-B y B-A cuentan como una). Sirve para dibujarlas.
    def listaCarreteras(self):
        lista = []
        for origen in self.adyacencia:
            for carretera in self.adyacencia[origen]:
                if [carretera.destino, origen, carretera.distancia] not in lista:
                    lista.append([origen, carretera.destino, carretera.distancia])
        return lista

    # Lee el archivo de pueblos. Cada linea: nombre x y
    def cargarPueblos(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "" or linea.startswith("#"):    # saltamos comentarios
                    continue
                datos = linea.split()
                self.agregarPueblo(Pueblo(datos[0], int(datos[1]), int(datos[2])))

    # Lee el archivo de carreteras. Cada linea: pueblo pueblo km
    def cargarCarreteras(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "" or linea.startswith("#"):
                    continue
                datos = linea.split()
                self.agregarCarretera(datos[0], datos[1], int(datos[2]))
