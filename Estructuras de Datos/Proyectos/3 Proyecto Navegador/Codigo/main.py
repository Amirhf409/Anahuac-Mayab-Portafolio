# main.py
# Proyecto 3 - Navegador web con pilas (LIFO)
# Abre la ventana del navegador (modo grafico).
# La version de consola sigue disponible en consola.py
#
# Para correrlo:  python main.py

import tkinter as tk

from interfaz import VentanaNavegador

raiz = tk.Tk()
VentanaNavegador(raiz)
raiz.mainloop()
