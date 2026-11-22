# main.py
# Proyecto 6 - Ruta Magica (grafos)
# Carga los pueblos y las carreteras desde los archivos de texto y abre la ventana.
# Para correrlo: python main.py

import os
import tkinter as tk

from grafo import Grafo
from ventana import VentanaRutaMagica

# carpeta donde esta este archivo, para encontrar los .txt aunque se corra desde otro lado
carpeta = os.path.dirname(os.path.abspath(__file__))

grafo = Grafo()
grafo.cargarPueblos(os.path.join(carpeta, "pueblos.txt"))
grafo.cargarCarreteras(os.path.join(carpeta, "carreteras.txt"))

raiz = tk.Tk()
VentanaRutaMagica(raiz, grafo)
raiz.mainloop()
