# Ventana de la cola de impresión hecha con Tkinter (modo gráfico).
# Usa la misma clase ColaImpresion que la versión de consola.

import tkinter as tk
from tkinter import ttk, messagebox

from cola_impresion import ColaImpresion

ANCHO_CASILLA = 80    # tamaño de cada casilla de la cola en el dibujo
ALTO_CASILLA = 60


class VentanaCola:

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Cola de Impresión - Proyecto 4")
        self.raiz.geometry("720x470")
        self.raiz.resizable(False, False)

        # cola con capacidad máxima de 6 trabajos
        self.impresora = ColaImpresion(6)

        ttk.Label(self.raiz, text="Cola de impresión (FIFO)", font=("Arial", 15, "bold")).pack(pady=(10, 0))
        ttk.Label(self.raiz, text="El primer trabajo que llega es el primero que se imprime.").pack()

        self.dibujo = tk.Canvas(self.raiz, width=690, height=150, bg="white",
                                highlightthickness=1, highlightbackground="#999999")
        self.dibujo.pack(pady=10)

        botones = ttk.Frame(self.raiz)
        botones.pack()
        ttk.Button(botones, text="Agregar trabajo", command=self.agregar).pack(side="left", padx=5)
        ttk.Button(botones, text="Imprimir documento", command=self.imprimir).pack(side="left", padx=5)
        ttk.Button(botones, text="Mostrar cola", command=self.mostrar).pack(side="left", padx=5)
        ttk.Button(botones, text="Salir", command=self.salir).pack(side="left", padx=5)

        ttk.Label(self.raiz, text="Historial:").pack(anchor="w", padx=15, pady=(10, 0))
        self.historial = tk.Text(self.raiz, height=9, width=84, font=("Consolas", 10), state="disabled")
        self.historial.pack(padx=15)

        self.dibujarCola()

    # ---------- botones ----------

    def agregar(self):
        computadora = self.impresora.agregar_trabajo()
        if computadora == None:
            self.escribir("La cola de impresión está LLENA")
            messagebox.showwarning("Cola llena", "La cola de impresión está LLENA")
        else:
            self.escribir("Trabajo agregado desde " + computadora)
        self.dibujarCola()

    def imprimir(self):
        computadora = self.impresora.imprimir_documento()
        if computadora == None:
            self.escribir("La cola de impresión está VACÍA")
            messagebox.showwarning("Cola vacía", "La cola de impresión está VACÍA")
        else:
            self.escribir("Imprimiendo documento de " + computadora + " (" + computadora + " está siendo atendida)")
        self.dibujarCola()

    def mostrar(self):
        if self.impresora.esta_vacia():
            self.escribir("La cola de impresión está VACÍA")
        else:
            self.escribir("Cola de impresión: " + "   ".join(self.impresora.mostrar_cola()))

    def salir(self):
        messagebox.showinfo("Cola de impresión", "Programa finalizado.")
        self.raiz.destroy()

    # ---------- apoyo ----------

    # agrega una línea al final del historial
    def escribir(self, texto):
        self.historial.config(state="normal")
        self.historial.insert("end", texto + "\n")
        self.historial.see("end")                   # baja hasta la última línea
        self.historial.config(state="disabled")     # para que no se pueda escribir encima

    # dibuja la impresora y las 6 casillas de la cola
    def dibujarCola(self):
        self.dibujo.delete("all")

        # impresora a la izquierda: de ahí salen los trabajos
        self.dibujo.create_rectangle(15, 40, 105, 110, fill="#e0e0e0", outline="#555555", width=2)
        self.dibujo.create_text(60, 75, text="Impresora", font=("Arial", 10, "bold"))

        for i in range(self.impresora.capacidad):
            x1 = 130 + i * (ANCHO_CASILLA + 8)
            y1 = 45
            if i < len(self.impresora.cola):
                self.dibujo.create_rectangle(x1, y1, x1 + ANCHO_CASILLA, y1 + ALTO_CASILLA,
                                             fill="#cfe3f7", outline="#1f4e79", width=2)
                self.dibujo.create_text(x1 + ANCHO_CASILLA / 2, y1 + ALTO_CASILLA / 2,
                                        text=self.impresora.cola[i], font=("Arial", 12, "bold"))
            else:
                self.dibujo.create_rectangle(x1, y1, x1 + ANCHO_CASILLA, y1 + ALTO_CASILLA,
                                             outline="#aaaaaa", dash=(4, 3))
            self.dibujo.create_text(x1 + ANCHO_CASILLA / 2, y1 - 12, text=str(i + 1), fill="#666666")

        # flecha que indica cuál se imprime primero
        self.dibujo.create_line(128, 75, 108, 75, arrow="last", width=2)
        if not self.impresora.esta_vacia():
            self.dibujo.create_text(170, 125, text="Siguiente en imprimir", fill="#1f4e79")

        texto = "Trabajos: " + str(len(self.impresora.cola)) + " de " + str(self.impresora.capacidad)
        self.dibujo.create_text(680, 15, text=texto, anchor="e", font=("Arial", 10, "bold"))
