# carretera.py
# Clase Carretera: es una arista del grafo.
# Guarda a que pueblo llega y cuantos kilometros mide (el peso).


class Carretera:

    def __init__(self, destino, distancia):
        self.destino = destino        # nombre del pueblo al que llega
        self.distancia = distancia    # kilometros
