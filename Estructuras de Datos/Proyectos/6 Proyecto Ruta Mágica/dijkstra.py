# dijkstra.py
# Clase Dijkstra: calcula la ruta mas corta entre dos pueblos.
# Idea: empezamos en el origen y siempre visitamos el pueblo no visitado
# que este mas cerca. Cada vez que encontramos un camino mas corto
# a un vecino, actualizamos su distancia y guardamos de donde venimos.

from ruta import Ruta

INFINITO = float("inf")    # distancia de un pueblo al que todavia no sabemos llegar


class Dijkstra:

    def __init__(self, grafo):
        self.grafo = grafo

    def calcular(self, origen, destino):
        distancia = {}    # distancia mas corta conocida desde el origen
        anterior = {}     # pueblo del que venimos para llegar a cada pueblo
        visitados = []

        for nombre in self.grafo.nombresPueblos():
            distancia[nombre] = INFINITO
            anterior[nombre] = None
        distancia[origen] = 0

        while len(visitados) < len(self.grafo.pueblos):
            actual = self.masCercano(distancia, visitados)
            if actual == None:      # ya no hay pueblos a los que se pueda llegar
                break
            visitados.append(actual)

            # revisamos si pasando por "actual" llegamos mas rapido a cada vecino
            for carretera in self.grafo.vecinos(actual):
                nueva = distancia[actual] + carretera.distancia
                if nueva < distancia[carretera.destino]:
                    distancia[carretera.destino] = nueva
                    anterior[carretera.destino] = actual

        return self.armarRuta(anterior, distancia, origen, destino)

    # Busca, entre los no visitados, el pueblo con menor distancia
    def masCercano(self, distancia, visitados):
        mejor = None
        for nombre in distancia:
            if nombre not in visitados and distancia[nombre] != INFINITO:
                if mejor == None or distancia[nombre] < distancia[mejor]:
                    mejor = nombre
        return mejor

    # Recorre "anterior" desde el destino hasta el origen para sacar el camino
    def armarRuta(self, anterior, distancia, origen, destino):
        if distancia[destino] == INFINITO:
            return Ruta([], [], 0)     # no hay camino

        pueblos = []
        actual = destino
        while actual != None:
            pueblos.insert(0, actual)  # se inserta al inicio para que quede en orden
            actual = anterior[actual]

        tramos = []
        for i in range(len(pueblos) - 1):
            km = self.grafo.distanciaDirecta(pueblos[i], pueblos[i + 1])
            tramos.append([pueblos[i], pueblos[i + 1], km])

        return Ruta(pueblos, tramos, distancia[destino])
