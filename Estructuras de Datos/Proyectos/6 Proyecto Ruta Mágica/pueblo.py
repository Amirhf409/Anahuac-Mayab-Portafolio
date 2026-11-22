# pueblo.py
# Clase Pueblo: es un vertice del grafo (un Pueblo Magico).


class Pueblo:

    def __init__(self, nombre, x, y):
        self.nombre = nombre
        # x, y solo se usan para dibujar el pueblo en el mapa de la ventana
        self.x = x
        self.y = y
