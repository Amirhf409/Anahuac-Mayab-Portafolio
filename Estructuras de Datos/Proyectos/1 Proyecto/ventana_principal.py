import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import resistencia as modulo_resistencia
from arreglo_paralelo import ArregloParalelo
from arreglo_serie import ArregloSerie
from codigo_colores import CodigoColores
from resistencia import Resistencia

# Medidas de la ventana y del dibujo
ANCHO_VENTANA = 900
ALTO_VENTANA = 640
MAXIMO_RESISTENCIAS = 1000

# Colores de la ventana
COLOR_FONDO = "#f4f4f4"
COLOR_TITULO = "#e85d04"
COLOR_CUERPO = "#e3c08d"
COLOR_ALAMBRE = "#9a9996"
COLOR_AVISO = "#c01c28"

# Donde empieza cada banda dentro del cuerpo de la resistencia (en pixeles)
POSICIONES_BANDAS = [60, 130, 200, 300]
ANCHO_BANDA = 30
ETIQUETAS = ["1er díg.", "2do díg.", "multip.", "toler."]


# Convierte un color [r, g, b] al formato que usa tkinter, ej. [255, 0, 0] -> "#ff0000"
def rgb_a_hex(rgb):
    return "#%02x%02x%02x" % (rgb[0], rgb[1], rgb[2])


# Decide si el texto encima de un color se ve mejor en negro o en blanco
def color_de_texto(rgb):
    brillo = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000
    if brillo > 140:
        return "#000000"
    return "#ffffff"


# Ventana principal del programa, tiene una pestaña por cada opción del menú
class VentanaPrincipal:
    # Crea la ventana, los objetos que usa y las 3 pestañas
    def __init__(self):
        self.codigo = CodigoColores()
        self.arreglo_serie = ArregloSerie("Dorado")
        self.arreglo_paralelo = ArregloParalelo("Dorado")

        self.ventana = tk.Tk()
        self.ventana.title("Resistencia eléctrica · Proyecto de arreglos")
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.ventana.configure(bg=COLOR_FONDO)

        # uso el tema clam para que la tabla sí muestre los colores de fondo
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview", rowheight=24)

        titulo = tk.Label(self.ventana, text="RESISTENCIA ELÉCTRICA  ·  Proyecto de arreglos",
                          font=("Segoe UI", 16, "bold"), fg=COLOR_TITULO, bg=COLOR_FONDO)
        titulo.pack(pady=10)

        pestanas = ttk.Notebook(self.ventana)
        pestanas.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.pestana_colores = tk.Frame(pestanas, bg="white")
        self.pestana_arreglos = tk.Frame(pestanas, bg="white")
        self.pestana_tabla = tk.Frame(pestanas, bg="white")

        pestanas.add(self.pestana_colores, text="  1. Colores de una resistencia  ")
        pestanas.add(self.pestana_arreglos, text="  2. Serie y paralelo  ")
        pestanas.add(self.pestana_tabla, text="  3. Tabla de colores  ")

        self.crear_pestana_colores()
        self.crear_pestana_arreglos()
        self.crear_pestana_tabla()

    # Muestra la ventana y espera a que el usuario haga algo
    def ejecutar(self):
        self.ventana.mainloop()

    # ===================== PESTAÑA 1: COLORES =====================

    # Arma los controles de la opción 1
    def crear_pestana_colores(self):
        marco = tk.Frame(self.pestana_colores, bg="white")
        marco.pack(pady=15)

        tk.Label(marco, text="Valor de la resistencia (Ω):", bg="white",
                 font=("Segoe UI", 11)).grid(row=0, column=0, padx=5)
        self.entrada_valor = tk.Entry(marco, width=15, font=("Segoe UI", 11))
        self.entrada_valor.grid(row=0, column=1, padx=5)

        tk.Label(marco, text="Tolerancia:", bg="white",
                 font=("Segoe UI", 11)).grid(row=0, column=2, padx=5)

        # lleno la lista con los colores que sirven para la cuarta banda
        tolerancias = self.codigo.obtener_tolerancias()
        self.nombres_tolerancia = []
        opciones = []
        for i in range(len(tolerancias)):
            self.nombres_tolerancia.append(tolerancias[i].nombre)
            opciones.append(f"{tolerancias[i].nombre} (± {tolerancias[i].tolerancia} %)")

        self.lista_tolerancia = ttk.Combobox(marco, values=opciones, state="readonly", width=18)
        self.lista_tolerancia.current(0)  # Dorado por defecto
        self.lista_tolerancia.grid(row=0, column=3, padx=5)

        boton = tk.Button(marco, text="Calcular colores", bg=COLOR_TITULO, fg="white",
                          font=("Segoe UI", 10, "bold"), command=self.calcular_colores)
        boton.grid(row=0, column=4, padx=10)

        texto_rango = (f"Valores permitidos: de {modulo_resistencia.VALOR_MINIMO} "
                       f"a {modulo_resistencia.VALOR_MAXIMO} ohmios")
        tk.Label(self.pestana_colores, text=texto_rango, bg="white", fg="gray").pack()

        # aquí se dibuja la resistencia
        self.lienzo = tk.Canvas(self.pestana_colores, width=560, height=190, bg="white",
                                highlightthickness=0)
        self.lienzo.pack(pady=10)

        self.etiqueta_resultado = tk.Label(self.pestana_colores, text="", bg="white",
                                           font=("Consolas", 11), justify="left")
        self.etiqueta_resultado.pack()

        self.etiqueta_aviso = tk.Label(self.pestana_colores, text="", bg="white",
                                       fg=COLOR_AVISO, font=("Segoe UI", 10, "bold"),
                                       wraplength=750)
        self.etiqueta_aviso.pack(pady=5)

    # Lee el valor, revisa que sea válido y muestra el dibujo con sus colores
    def calcular_colores(self):
        texto = self.entrada_valor.get().strip()

        if texto.isdigit() == False:
            messagebox.showerror("Dato no válido", "Escribe un número entero, sin letras ni puntos.")
            return

        valor = int(texto)
        if modulo_resistencia.valor_valido(valor) == False:
            messagebox.showerror("Fuera de rango",
                                 f"El valor debe estar entre {modulo_resistencia.VALOR_MINIMO} "
                                 f"y {modulo_resistencia.VALOR_MAXIMO} ohmios.")
            return

        tolerancia = self.nombres_tolerancia[self.lista_tolerancia.current()]
        pieza = Resistencia(valor, tolerancia)

        self.dibujar_resistencia(pieza)

        colores = pieza.obtener_colores()
        rango = pieza.rango_tolerancia()
        resultado = (f"Valor       : {pieza.valor} Ω  ({pieza.valor_formateado()})\n"
                     f"Colores     : {colores[0]} → {colores[1]} → {colores[2]}\n"
                     f"Tolerancia  : {pieza.tolerancia.nombre} (± {pieza.tolerancia.tolerancia} %)\n"
                     f"Rango real  : {round(rango[0], 2)} Ω a {round(rango[1], 2)} Ω")
        self.etiqueta_resultado.config(text=resultado)

        if pieza.es_exacta() == False:
            self.etiqueta_aviso.config(text="El código de 4 bandas solo admite dos cifras "
                                            f"significativas, por eso {pieza.valor} Ω se "
                                            f"representa como {pieza.valor_representado()} Ω.")
        else:
            self.etiqueta_aviso.config(text="")

    # Dibuja los alambres, el cuerpo y las 4 bandas de colores
    def dibujar_resistencia(self, pieza):
        self.lienzo.delete("all")  # borro el dibujo anterior

        x_inicio = 100   # donde empieza el cuerpo
        x_fin = 460      # donde termina el cuerpo
        y_arriba = 30
        y_abajo = 110

        # alambres de cada lado
        self.lienzo.create_line(10, 70, x_inicio, 70, width=5, fill=COLOR_ALAMBRE)
        self.lienzo.create_line(x_fin, 70, 550, 70, width=5, fill=COLOR_ALAMBRE)

        # cuerpo de la resistencia
        self.lienzo.create_rectangle(x_inicio, y_arriba, x_fin, y_abajo,
                                     fill=COLOR_CUERPO, outline="#b8956a", width=2)

        bandas = pieza.obtener_bandas()
        for i in range(len(bandas)):
            x = x_inicio + POSICIONES_BANDAS[i]

            # el color Ninguno significa que no hay cuarta banda, así que no la pinto
            if bandas[i].nombre != "Ninguno":
                self.lienzo.create_rectangle(x, y_arriba, x + ANCHO_BANDA, y_abajo,
                                             fill=rgb_a_hex(bandas[i].rgb), outline="")

            # rayita y nombre debajo de cada banda
            centro = x + ANCHO_BANDA / 2
            self.lienzo.create_line(centro, y_abajo + 5, centro, y_abajo + 20, fill="gray")
            self.lienzo.create_text(centro, y_abajo + 32, text=ETIQUETAS[i], fill="gray",
                                    font=("Segoe UI", 9))
            self.lienzo.create_text(centro, y_abajo + 50, text=bandas[i].nombre,
                                    font=("Segoe UI", 10, "bold"))

    # ===================== PESTAÑA 2: SERIE Y PARALELO =====================

    # Arma los controles de la opción 2
    def crear_pestana_arreglos(self):
        marco = tk.Frame(self.pestana_arreglos, bg="white")
        marco.pack(pady=15)

        tk.Label(marco, text="Cantidad de resistencias (n):", bg="white",
                 font=("Segoe UI", 11)).grid(row=0, column=0, padx=5)
        self.entrada_cantidad = tk.Entry(marco, width=10, font=("Segoe UI", 11))
        self.entrada_cantidad.grid(row=0, column=1, padx=5)

        boton = tk.Button(marco, text="Generar y calcular", bg=COLOR_TITULO, fg="white",
                          font=("Segoe UI", 10, "bold"), command=self.calcular_arreglos)
        boton.grid(row=0, column=2, padx=10)

        texto = (f"Cada resistencia recibe un valor aleatorio entre {modulo_resistencia.VALOR_MINIMO} "
                 f"y {modulo_resistencia.VALOR_MAXIMO} ohmios (máximo {MAXIMO_RESISTENCIAS} resistencias).")
        tk.Label(self.pestana_arreglos, text=texto, bg="white", fg="gray").pack()

        # tabla con las resistencias generadas
        marco_tabla = tk.Frame(self.pestana_arreglos, bg="white")
        marco_tabla.pack(fill="both", expand=True, padx=15, pady=10)

        columnas = ("num", "valor", "equivalente", "colores")
        self.tabla_arreglo = ttk.Treeview(marco_tabla, columns=columnas, show="headings", height=9)
        self.tabla_arreglo.heading("num", text="#")
        self.tabla_arreglo.heading("valor", text="Valor (Ω)")
        self.tabla_arreglo.heading("equivalente", text="Equivalente")
        self.tabla_arreglo.heading("colores", text="Colores de las bandas")
        self.tabla_arreglo.column("num", width=50, anchor="center")
        self.tabla_arreglo.column("valor", width=150, anchor="e")
        self.tabla_arreglo.column("equivalente", width=130, anchor="e")
        self.tabla_arreglo.column("colores", width=330)

        barra = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla_arreglo.yview)
        self.tabla_arreglo.configure(yscrollcommand=barra.set)
        self.tabla_arreglo.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        self.etiqueta_totales = tk.Label(self.pestana_arreglos, text="", bg="white",
                                         fg=COLOR_TITULO, font=("Segoe UI", 13, "bold"),
                                         justify="left")
        self.etiqueta_totales.pack()

        self.etiqueta_formulas = tk.Label(self.pestana_arreglos, text="", bg="white", fg="gray",
                                          font=("Consolas", 9), justify="left")
        self.etiqueta_formulas.pack(pady=(0, 10))

    # Genera n resistencias al azar y calcula el total en serie y en paralelo
    def calcular_arreglos(self):
        texto = self.entrada_cantidad.get().strip()

        if texto.isdigit() == False or int(texto) < 1 or int(texto) > MAXIMO_RESISTENCIAS:
            messagebox.showerror("Dato no válido",
                                 f"Escribe un número entero entre 1 y {MAXIMO_RESISTENCIAS}.")
            return

        cantidad = int(texto)
        resistencias = self.arreglo_serie.generar_aleatorias(cantidad)

        # uso las mismas resistencias para los dos cálculos
        self.arreglo_paralelo.limpiar()
        for i in range(len(resistencias)):
            self.arreglo_paralelo.agregar(resistencias[i])

        # borro las filas anteriores y pongo las nuevas
        for fila in self.tabla_arreglo.get_children():
            self.tabla_arreglo.delete(fila)

        for i in range(len(resistencias)):
            pieza = resistencias[i]
            colores = pieza.obtener_colores()
            texto_colores = colores[0] + ", " + colores[1] + ", " + colores[2]
            self.tabla_arreglo.insert("", "end", values=(i + 1, pieza.valor,
                                                         pieza.valor_formateado(), texto_colores))

        totales = (f"Valor total en SERIE      :  {self.arreglo_serie.total_formateado()}\n"
                   f"Valor total en PARALELO :  {self.arreglo_paralelo.total_formateado()}")
        self.etiqueta_totales.config(text=totales)

        formulas = (self.resumir(self.arreglo_serie.obtener_formula()) + "\n" +
                    self.resumir(self.arreglo_paralelo.obtener_formula()))
        self.etiqueta_formulas.config(text=formulas)

    # Corta la fórmula si es muy larga para que quepa en la ventana
    def resumir(self, formula):
        if len(formula) <= 90:
            return formula
        return formula[0:90] + " ..."

    # ===================== PESTAÑA 3: TABLA DE COLORES =====================

    # Muestra la tabla del código de colores, cada fila pintada de su color
    def crear_pestana_tabla(self):
        tk.Label(self.pestana_tabla, text="Código de colores de 4 bandas", bg="white",
                 font=("Segoe UI", 12, "bold")).pack(pady=10)

        columnas = ("color", "digito", "multiplicador", "tolerancia")
        tabla = ttk.Treeview(self.pestana_tabla, columns=columnas, show="headings", height=13)
        tabla.heading("color", text="Color")
        tabla.heading("digito", text="1ra y 2da banda (dígito)")
        tabla.heading("multiplicador", text="3ra banda (multiplicador)")
        tabla.heading("tolerancia", text="4ta banda (tolerancia)")
        for columna in columnas:
            tabla.column(columna, width=190, anchor="center")
        tabla.pack(padx=15)

        for i in range(len(self.codigo.tabla)):
            color = self.codigo.tabla[i]

            digito = "—"
            if color.digito != None:
                digito = str(color.digito)

            multiplicador = "—"
            if color.multiplicador != None:
                multiplicador = "x " + str(color.multiplicador)

            tolerancia = "—"
            if color.tolerancia != None:
                tolerancia = "± " + str(color.tolerancia) + " %"

            # cada fila tiene una etiqueta con su color de fondo
            etiqueta = "fila" + str(i)
            tabla.insert("", "end", values=(color.nombre, digito, multiplicador, tolerancia),
                         tags=(etiqueta,))
            tabla.tag_configure(etiqueta, background=rgb_a_hex(color.rgb),
                                foreground=color_de_texto(color.rgb))
