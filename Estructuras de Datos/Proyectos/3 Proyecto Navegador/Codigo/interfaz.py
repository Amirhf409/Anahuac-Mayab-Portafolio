# interfaz.py
# Ventana del navegador hecha con Tkinter (modo grafico).
# Arriba: botones Atras/Adelante, la URL y el boton Ir.
# En medio: la pagina actual.
# Abajo: el dibujo de las dos pilas (atras y adelante) con su tope.

import tkinter as tk
from tkinter import ttk, messagebox

from navegador import Navegador

ANCHO_CASILLA = 230    # tamano de cada casilla de la pila en el dibujo
ALTO_CASILLA = 34


class VentanaNavegador:

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Navegador Web - Proyecto 3")
        self.raiz.geometry("760x400")
        self.raiz.resizable(False, False)

        # Usamos la misma clase Navegador que la version de consola
        self.navegador = Navegador()

        self.crearBarra()
        self.crearAreaPagina()
        self.crearDibujoPilas()
        self.actualizar()

    # Barra de arriba: botones, caja de la URL, boton Ir y boton Salir
    def crearBarra(self):
        barra = ttk.Frame(self.raiz, padding=8)
        barra.pack(fill="x")

        ttk.Button(barra, text="< Atrás", command=self.irAtras).pack(side="left")
        ttk.Button(barra, text="Adelante >", command=self.irAdelante).pack(side="left", padx=(4, 8))

        # Combobox para poder escribir la URL o escogerla de la lista
        self.cajaUrl = ttk.Combobox(barra, values=self.navegador.sitiosDisponibles())
        self.cajaUrl.pack(side="left", fill="x", expand=True)
        self.cajaUrl.bind("<Return>", self.irAPagina)   # Enter tambien visita

        ttk.Button(barra, text="Ir", command=self.irAPagina).pack(side="left", padx=(8, 0))
        ttk.Button(barra, text="Salir", command=self.salir).pack(side="left", padx=(8, 0))

    # Parte de en medio donde se ve la pagina actual
    def crearAreaPagina(self):
        area = ttk.Frame(self.raiz, padding=(20, 10))
        area.pack(fill="x")

        self.etiquetaTitulo = ttk.Label(area, text="", font=("Arial", 16, "bold"))
        self.etiquetaTitulo.pack(anchor="w")

        self.etiquetaDescripcion = ttk.Label(area, text="")
        self.etiquetaDescripcion.pack(anchor="w", pady=(8, 0))

    # Abajo: el canvas donde se dibujan las pilas y la barra de mensajes
    def crearDibujoPilas(self):
        self.etiquetaEstado = ttk.Label(self.raiz, text="", relief="sunken", padding=4)
        self.etiquetaEstado.pack(fill="x", side="bottom")

        self.dibujo = tk.Canvas(self.raiz, width=740, height=200, bg="white",
                                highlightthickness=1, highlightbackground="#999999")
        self.dibujo.pack(side="bottom", pady=(0, 8))

    # ---------- acciones de los botones ----------

    # Se llama con el boton Ir o con Enter (por eso evento=None)
    def irAPagina(self, evento=None):
        mensaje = self.navegador.visitar(self.cajaUrl.get())
        self.mostrarMensaje(mensaje)

    def irAtras(self):
        mensaje = self.navegador.retroceder()
        self.mostrarMensaje(mensaje)

    def irAdelante(self):
        mensaje = self.navegador.avanzar()
        self.mostrarMensaje(mensaje)

    def salir(self):
        messagebox.showinfo("Navegador", "Saliendo del navegador. Hasta luego.")
        self.raiz.destroy()

    # Los avisos de pila vacia o llena tambien salen en una ventanita
    def mostrarMensaje(self, mensaje):
        self.etiquetaEstado.config(text=mensaje)
        self.actualizar()
        if mensaje.startswith("PILA") or mensaje.startswith("Tienes"):
            messagebox.showwarning("Aviso", mensaje)

    # ---------- dibujo ----------

    def actualizar(self):
        pagina = self.navegador.paginaActual
        if pagina == None:
            self.etiquetaTitulo.config(text="Página en blanco")
            self.etiquetaDescripcion.config(text="Escribe o elige una URL arriba y presiona Ir.")
        else:
            self.etiquetaTitulo.config(text=pagina.titulo)
            self.etiquetaDescripcion.config(text=pagina.verDescripcion())
            self.cajaUrl.set(pagina.url)

        self.dibujo.delete("all")
        self.dibujarPila(self.navegador.pilaAtras, "Pila Atrás", 120)
        self.dibujarPila(self.navegador.pilaAdelante, "Pila Adelante", 500)

    # Dibuja una pila como casillas apiladas: la casilla 1 abajo y el tope arriba
    def dibujarPila(self, pila, titulo, centroX):
        izquierda = centroX - ANCHO_CASILLA / 2 + 20
        abajo = 185
        texto = titulo + "  (" + str(pila.cantidad()) + " de " + str(pila.capacidad) + ")"
        self.dibujo.create_text(izquierda + ANCHO_CASILLA / 2, 18, text=texto, font=("Arial", 11, "bold"))

        elementos = pila.listaElementos()
        for i in range(pila.capacidad):
            y2 = abajo - i * ALTO_CASILLA
            y1 = y2 - ALTO_CASILLA
            if i < len(elementos):
                relleno = "#cfe3f7"
                texto = elementos[i].url.replace("https://", "")
            else:
                relleno = "white"
                texto = ""
            self.dibujo.create_rectangle(izquierda, y1, izquierda + ANCHO_CASILLA, y2,
                                         fill=relleno, outline="#1f4e79")
            self.dibujo.create_text(izquierda + ANCHO_CASILLA / 2, (y1 + y2) / 2, text=texto)

        # flecha que marca el tope (el ultimo que entro)
        if pila.estaVacia():
            self.dibujo.create_text(izquierda + ANCHO_CASILLA / 2, abajo - ALTO_CASILLA / 2,
                                    text="vacía", fill="#888888")
        else:
            yTope = abajo - (len(elementos) - 1) * ALTO_CASILLA - ALTO_CASILLA / 2
            xFlecha = izquierda + ANCHO_CASILLA + 8
            self.dibujo.create_line(xFlecha + 50, yTope, xFlecha, yTope, arrow="last", width=2)
            self.dibujo.create_text(xFlecha + 70, yTope, text="TOPE", font=("Arial", 9, "bold"))
