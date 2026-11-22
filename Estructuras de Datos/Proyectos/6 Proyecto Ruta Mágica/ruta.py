# ruta.py
# Clase Ruta: guarda el resultado que regresa Dijkstra.


class Ruta:

    def __init__(self, pueblos, tramos, distanciaTotal):
        self.pueblos = pueblos                # lista de nombres en orden, del origen al destino
        self.tramos = tramos                  # lista de [desde, hasta, km]
        self.distanciaTotal = distanciaTotal

    def encontrada(self):
        return len(self.pueblos) > 0

    # Ejemplo: "Sisal -> Motul -> Izamal"
    def textoRuta(self):
        return " -> ".join(self.pueblos)
