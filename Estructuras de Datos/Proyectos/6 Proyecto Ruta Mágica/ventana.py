# ventana.py
# Ventana del programa hecha con Tkinter (modo grafico).
# Pestana 1: mapa del grafo, se escoge origen y destino y se dibuja la ruta.
# Pestana 2: matriz de adyacencia con las distancias.

import tkinter as tk
from tkinter import ttk, messagebox

from dijkstra import Dijkstra

RADIO = 22    # tamano de los circulos de los pueblos


class VentanaRutaMagica:

    def __init__(self, raiz, grafo):
        self.raiz = raiz
        self.grafo = grafo
        self.dijkstra = Dijkstra(grafo)

        self.raiz.title("Ruta Mágica - Pueblos Mágicos de Yucatán")
        self.raiz.geometry("1000x560")
        self.raiz.resizable(False, False)

        pestanas = ttk.Notebook(self.raiz)
        pestanas.pack(fill="both", expand=True, padx=8, pady=8)

        self.pestanaRuta = ttk.Frame(pestanas, padding=10)
        self.pestanaMatriz = ttk.Frame(pestanas, padding=10)
        pestanas.add(self.pestanaRuta, text="Buscar ruta")
        pestanas.add(self.pestanaMatriz, text="Matriz de adyacencia")

        self.crearMapa()
        self.crearPanel()
        self.crearMatriz()
        self.dibujarGrafo()

    # ---------- Pestana 1 ----------

    def crearMapa(self):
        self.mapa = tk.Canvas(self.pestanaRuta, width=640, height=420, bg="white",
                              highlightthickness=1, highlightbackground="#999999")
        self.mapa.pack(side="left")

    def crearPanel(self):
        panel = ttk.Frame(self.pestanaRuta, padding=(15, 0, 0, 0))
        panel.pack(side="left", fill="both", expand=True)

        ttk.Label(panel, text="Ruta Mágica - Yucatán", font=("Arial", 14, "bold")).pack(anchor="w")
        ttk.Label(panel, text="Algoritmo utilizado: Dijkstra").pack(anchor="w", pady=(0, 12))

        nombres = self.grafo.nombresPueblos()

        ttk.Label(panel, text="Pueblo de origen:").pack(anchor="w")
        self.cajaOrigen = ttk.Combobox(panel, values=nombres, state="readonly")
        self.cajaOrigen.pack(fill="x", pady=(0, 8))

        ttk.Label(panel, text="Pueblo de destino:").pack(anchor="w")
        self.cajaDestino = ttk.Combobox(panel, values=nombres, state="readonly")
        self.cajaDestino.pack(fill="x", pady=(0, 12))

        botones = ttk.Frame(panel)
        botones.pack(fill="x")
        ttk.Button(botones, text="Calcular ruta", command=self.calcularRuta).pack(side="left")
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=8)

        ttk.Label(panel, text="Resultado:").pack(anchor="w", pady=(15, 2))
        self.textoResultado = tk.Text(panel, height=12, width=36, font=("Consolas", 10), wrap="word", state="disabled")
        self.textoResultado.pack(fill="both", expand=True)

    # Dibuja todas las carreteras y pueblos. "ruta" es la lista de pueblos a pintar en rojo.
    def dibujarGrafo(self, ruta=[]):
        self.mapa.delete("all")

        for carretera in self.grafo.listaCarreteras():
            a = self.grafo.pueblos[carretera[0]]
            b = self.grafo.pueblos[carretera[1]]
            color = "#bbbbbb"
            grosor = 2
            if self.estaEnRuta(carretera[0], carretera[1], ruta):
                color = "red"
                grosor = 4
            self.mapa.create_line(a.x, a.y, b.x, b.y, fill=color, width=grosor)

            # los km se escriben a la mitad de la linea
            mitadX = (a.x + b.x) / 2
            mitadY = (a.y + b.y) / 2
            self.mapa.create_rectangle(mitadX - 22, mitadY - 9, mitadX + 22, mitadY + 9, fill="white", outline="")
            self.mapa.create_text(mitadX, mitadY, text=str(carretera[2]) + " km", font=("Arial", 9))

        for nombre in self.grafo.pueblos:
            p = self.grafo.pueblos[nombre]
            relleno = "#cfe3f7"
            if nombre in ruta:
                relleno = "#f7b2b2"
            self.mapa.create_oval(p.x - RADIO, p.y - RADIO, p.x + RADIO, p.y + RADIO,
                                  fill=relleno, outline="#1f4e79", width=2)
            self.mapa.create_text(p.x, p.y + RADIO + 10, text=nombre, font=("Arial", 10, "bold"))

    # Una carretera es parte de la ruta si sus dos pueblos van seguidos en la lista
    def estaEnRuta(self, a, b, ruta):
        for i in range(len(ruta) - 1):
            if (ruta[i] == a and ruta[i + 1] == b) or (ruta[i] == b and ruta[i + 1] == a):
                return True
        return False

    def calcularRuta(self):
        origen = self.cajaOrigen.get()
        destino = self.cajaDestino.get()

        if origen == "" or destino == "":
            messagebox.showwarning("Faltan datos", "Selecciona el pueblo de origen y el de destino.")
            return
        if origen == destino:
            messagebox.showwarning("Mismo pueblo", "El origen y el destino deben ser pueblos diferentes.")
            return

        ruta = self.dijkstra.calcular(origen, destino)

        if not ruta.encontrada():
            self.escribirResultado("No existe una ruta entre " + origen + " y " + destino + ".")
            self.dibujarGrafo()
            return

        texto = "[OK] RUTA ENCONTRADA\n\n"
        for tramo in ruta.tramos:
            texto = texto + tramo[0] + " --(" + str(tramo[2]) + " km)--> " + tramo[1] + "\n"
        texto = texto + "\nRuta completa:\n" + ruta.textoRuta() + "\n"
        texto = texto + "\nDistancia total: " + str(ruta.distanciaTotal) + " km"

        self.escribirResultado(texto)
        self.dibujarGrafo(ruta.pueblos)

    def escribirResultado(self, texto):
        self.textoResultado.config(state="normal")
        self.textoResultado.delete("1.0", "end")
        self.textoResultado.insert("end", texto)
        self.textoResultado.config(state="disabled")    # para que no se pueda escribir encima

    def limpiar(self):
        self.cajaOrigen.set("")
        self.cajaDestino.set("")
        self.escribirResultado("")
        self.dibujarGrafo()

    # ---------- Pestana 2 ----------

    def crearMatriz(self):
        nombres = self.grafo.nombresPueblos()
        ttk.Label(self.pestanaMatriz, text="Distancias en km (∞ = no hay carretera directa)").pack(anchor="w", pady=(0, 8))

        columnas = ["pueblo"] + nombres
        tabla = ttk.Treeview(self.pestanaMatriz, columns=columnas, show="headings", height=len(nombres))
        tabla.heading("pueblo", text="")
        tabla.column("pueblo", width=100, anchor="w")
        for nombre in nombres:
            tabla.heading(nombre, text=nombre)
            tabla.column(nombre, width=95, anchor="center")

        for fila in nombres:
            valores = [fila]
            for columna in nombres:
                if fila == columna:
                    valores.append(0)
                else:
                    km = self.grafo.distanciaDirecta(fila, columna)
                    if km == None:
                        valores.append("∞")
                    else:
                        valores.append(km)
            tabla.insert("", "end", values=valores)
        tabla.pack(anchor="w")
