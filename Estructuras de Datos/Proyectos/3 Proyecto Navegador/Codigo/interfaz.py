# interfaz.py
# Ventana del navegador hecha con Tkinter (modo grafico).
# AVANCE: por ahora solo se puede escribir una URL y visitarla.
# Los botones Atras y Adelante y el dibujo de las pilas se conectan despues.

import tkinter as tk
from tkinter import ttk

from navegador import Navegador


class VentanaNavegador:

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Navegador Web - Proyecto 3")
        self.raiz.geometry("640x360")

        # Usamos la misma clase Navegador que la version de consola
        self.navegador = Navegador()

        self.crearBarra()
        self.crearAreaPagina()

    # Barra de arriba: botones, caja de la URL y boton Ir
    def crearBarra(self):
        barra = ttk.Frame(self.raiz, padding=8)
        barra.pack(fill="x")

        # Todavia no hacen nada, se conectan en el siguiente avance
        self.botonAtras = ttk.Button(barra, text="<", width=3, state="disabled")
        self.botonAtras.pack(side="left")
        self.botonAdelante = ttk.Button(barra, text=">", width=3, state="disabled")
        self.botonAdelante.pack(side="left", padx=(4, 8))

        # Combobox para poder escribir la URL o escogerla de la lista
        self.cajaUrl = ttk.Combobox(barra, values=self.navegador.sitiosDisponibles())
        self.cajaUrl.pack(side="left", fill="x", expand=True)
        self.cajaUrl.bind("<Return>", self.irAPagina)   # Enter tambien visita

        ttk.Button(barra, text="Ir", command=self.irAPagina).pack(side="left", padx=(8, 0))

    # Parte de en medio donde se ve la pagina actual
    def crearAreaPagina(self):
        area = ttk.Frame(self.raiz, padding=20)
        area.pack(fill="both", expand=True)

        self.etiquetaTitulo = ttk.Label(area, text="Pagina en blanco", font=("Arial", 16, "bold"))
        self.etiquetaTitulo.pack(anchor="w")

        self.etiquetaDescripcion = ttk.Label(area, text="Escribe una URL arriba y presiona Ir.")
        self.etiquetaDescripcion.pack(anchor="w", pady=(10, 0))

        # Abajo se muestra el mensaje que regresa el navegador
        self.etiquetaEstado = ttk.Label(self.raiz, text="", relief="sunken", padding=4)
        self.etiquetaEstado.pack(fill="x", side="bottom")

    # Se llama con el boton Ir o con Enter (por eso evento=None)
    def irAPagina(self, evento=None):
        mensaje = self.navegador.visitar(self.cajaUrl.get())
        self.etiquetaEstado.config(text=mensaje)
        self.actualizarPagina()

    def actualizarPagina(self):
        pagina = self.navegador.paginaActual
        if pagina == None:
            return
        self.etiquetaTitulo.config(text=pagina.titulo)
        self.etiquetaDescripcion.config(text=pagina.verDescripcion())


# Para probar la ventana sola: python interfaz.py
if __name__ == "__main__":
    raiz = tk.Tk()
    VentanaNavegador(raiz)
    raiz.mainloop()
