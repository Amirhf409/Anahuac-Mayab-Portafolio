"""Versión con ventana (modo gráfico) del carrito de compras, hecha con Tkinter.

Usa las mismas clases de modelo.py que la versión de consola,
solo cambia la forma de pedir los datos y de mostrar los resultados.

Equipo ProyectoFinal 7 - Proyecto 2
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from modelo import Carrito, CarritoError, catalogo_inicial
from utilidades import filtrar_por_referencia, formatear_dinero

COLOR_FONDO = "#f4f4f4"
COLOR_PRINCIPAL = "#1c71d8"
COLOR_FINALIZAR = "#2ec27e"


class VentanaCarrito:
    """Ventana principal: a la izquierda el catálogo y a la derecha el carrito."""

    def __init__(self):
        """Crea el catálogo, el carrito y todos los controles de la ventana."""
        self.catalogo = catalogo_inicial()
        self.carrito = Carrito()

        self.ventana = tk.Tk()
        self.ventana.title("Carrito de compras · Equipo ProyectoFinal 7")
        self.ventana.geometry("1100x600")
        self.ventana.configure(bg=COLOR_FONDO)

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview", rowheight=26, font=("Segoe UI", 10))
        estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        tk.Label(self.ventana, text="CARRITO DE COMPRAS", font=("Segoe UI", 18, "bold"),
                 fg=COLOR_PRINCIPAL, bg=COLOR_FONDO).pack(pady=10)

        contenedor = tk.Frame(self.ventana, bg=COLOR_FONDO)
        contenedor.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.crear_panel_catalogo(contenedor)
        self.crear_panel_carrito(contenedor)

        self.mostrar_catalogo(self.catalogo.productos)
        self.actualizar_carrito()

    def ejecutar(self):
        """Muestra la ventana y espera a que el usuario haga algo."""
        self.ventana.mainloop()

    # ===================== PANEL DEL CATÁLOGO =====================

    def crear_panel_catalogo(self, contenedor):
        """Arma la parte izquierda: búsqueda, tabla del catálogo y botón de agregar."""
        panel = tk.LabelFrame(contenedor, text=" Catálogo de productos ", bg="white",
                              font=("Segoe UI", 11, "bold"))
        panel.pack(side="left", fill="both", expand=True, padx=(0, 5))

        # búsqueda (opción 2 del menú)
        fila = tk.Frame(panel, bg="white")
        fila.pack(fill="x", padx=10, pady=10)
        tk.Label(fila, text="Buscar (ID o nombre):", bg="white").pack(side="left")
        self.entrada_busqueda = tk.Entry(fila, width=18)
        self.entrada_busqueda.pack(side="left", padx=5)
        tk.Button(fila, text="Buscar", command=self.buscar).pack(side="left", padx=2)
        tk.Button(fila, text="Mostrar todo", command=self.mostrar_todo).pack(side="left", padx=2)

        # tabla del catálogo (opción 1 del menú)
        columnas = ("id", "producto", "categoria", "precio")
        self.tabla_catalogo = ttk.Treeview(panel, columns=columnas, show="headings", height=8)
        self.tabla_catalogo.heading("id", text="ID")
        self.tabla_catalogo.heading("producto", text="Producto")
        self.tabla_catalogo.heading("categoria", text="Categoría")
        self.tabla_catalogo.heading("precio", text="Precio")
        self.tabla_catalogo.column("id", width=40, anchor="center")
        self.tabla_catalogo.column("producto", width=150)
        self.tabla_catalogo.column("categoria", width=130)
        self.tabla_catalogo.column("precio", width=80, anchor="e")
        self.tabla_catalogo.pack(fill="both", expand=True, padx=10)

        # agregar al carrito (opción 3 del menú)
        fila2 = tk.Frame(panel, bg="white")
        fila2.pack(fill="x", padx=10, pady=10)
        tk.Label(fila2, text="Cantidad:", bg="white").pack(side="left")
        self.caja_cantidad = tk.Spinbox(fila2, from_=1, to=99, width=5)
        self.caja_cantidad.pack(side="left", padx=5)
        tk.Button(fila2, text="Agregar al carrito  →", bg=COLOR_PRINCIPAL, fg="white",
                  font=("Segoe UI", 10, "bold"), command=self.agregar).pack(side="left", padx=10)

        self.etiqueta_mensaje = tk.Label(panel, text="Selecciona un producto y presiona Agregar.",
                                         bg="white", fg="gray")
        self.etiqueta_mensaje.pack(pady=(0, 10))

    def mostrar_catalogo(self, productos):
        """Borra la tabla del catálogo y la llena con los productos que recibe."""
        for fila in self.tabla_catalogo.get_children():
            self.tabla_catalogo.delete(fila)
        for producto in productos:
            self.tabla_catalogo.insert("", "end", values=(producto.id, producto.nombre,
                                                          producto.categoria,
                                                          formatear_dinero(producto.precio)))

    def mostrar_todo(self):
        """Vuelve a mostrar todos los productos y limpia la búsqueda."""
        self.entrada_busqueda.delete(0, "end")
        self.mostrar_catalogo(self.catalogo.productos)

    def buscar(self):
        """Busca por ID o por nombre y muestra solo los resultados."""
        texto = self.entrada_busqueda.get().strip()
        if texto == "":
            self.mostrar_todo()
            return
        resultados = filtrar_por_referencia(self.catalogo.productos, texto)
        if len(resultados) == 0:
            messagebox.showinfo("Buscar", f"No se encontraron productos con '{texto}'.")
            return
        self.mostrar_catalogo(resultados)

    def agregar(self):
        """Agrega al carrito el producto seleccionado con la cantidad de la caja."""
        id_producto = self.id_seleccionado(self.tabla_catalogo)
        if id_producto is None:
            messagebox.showwarning("Agregar", "Primero selecciona un producto del catálogo.")
            return

        texto = self.caja_cantidad.get().strip()
        if not texto.isdigit() or int(texto) < 1:
            messagebox.showerror("Cantidad inválida", "Escribe un número entero mayor o igual a 1.")
            return

        producto = self.catalogo.buscar_por_id(id_producto)
        item = self.carrito.agregar(producto, int(texto))
        self.etiqueta_mensaje.config(text=f"Se agregó {producto.nombre}. "
                                          f"En el carrito hay {item.cantidad}.", fg="green")
        self.actualizar_carrito()

    # ===================== PANEL DEL CARRITO =====================

    def crear_panel_carrito(self, contenedor):
        """Arma la parte derecha: tabla del carrito, botones y totales."""
        panel = tk.LabelFrame(contenedor, text=" Mi carrito ", bg="white",
                              font=("Segoe UI", 11, "bold"))
        panel.pack(side="left", fill="both", expand=True, padx=(5, 0))

        # tabla del carrito (opción 4 del menú)
        columnas = ("id", "producto", "precio", "cantidad", "subtotal")
        self.tabla_carrito = ttk.Treeview(panel, columns=columnas, show="headings", height=9)
        self.tabla_carrito.heading("id", text="ID")
        self.tabla_carrito.heading("producto", text="Producto")
        self.tabla_carrito.heading("precio", text="Precio")
        self.tabla_carrito.heading("cantidad", text="Cant.")
        self.tabla_carrito.heading("subtotal", text="Subtotal")
        self.tabla_carrito.column("id", width=40, anchor="center")
        self.tabla_carrito.column("producto", width=150)
        self.tabla_carrito.column("precio", width=80, anchor="e")
        self.tabla_carrito.column("cantidad", width=60, anchor="center")
        self.tabla_carrito.column("subtotal", width=90, anchor="e")
        self.tabla_carrito.pack(fill="both", expand=True, padx=10, pady=10)

        # opciones 5, 6 y 7 del menú
        fila = tk.Frame(panel, bg="white")
        fila.pack(pady=5)
        tk.Button(fila, text="Modificar cantidad", command=self.modificar).pack(side="left", padx=4)
        tk.Button(fila, text="Eliminar producto", command=self.eliminar).pack(side="left", padx=4)
        tk.Button(fila, text="Vaciar carrito", command=self.vaciar).pack(side="left", padx=4)

        self.etiqueta_totales = tk.Label(panel, text="", bg="white", font=("Segoe UI", 11))
        self.etiqueta_totales.pack(pady=5)

        # opción 8 del menú
        tk.Button(panel, text="Finalizar compra", bg=COLOR_FINALIZAR, fg="white",
                  font=("Segoe UI", 11, "bold"), width=20,
                  command=self.finalizar).pack(pady=(0, 10))

    def actualizar_carrito(self):
        """Vuelve a llenar la tabla del carrito y actualiza los totales."""
        for fila in self.tabla_carrito.get_children():
            self.tabla_carrito.delete(fila)
        for item in self.carrito.items:
            self.tabla_carrito.insert("", "end", values=(item.id, item.nombre,
                                                         formatear_dinero(item.precio),
                                                         item.cantidad,
                                                         formatear_dinero(item.subtotal)))
        self.etiqueta_totales.config(
            text=f"Productos: {self.carrito.total_productos}     "
                 f"Artículos: {self.carrito.total_articulos}     "
                 f"TOTAL: {formatear_dinero(self.carrito.total)}")

    def modificar(self):
        """Pide la nueva cantidad del producto seleccionado en el carrito."""
        id_producto = self.id_seleccionado(self.tabla_carrito)
        if id_producto is None:
            messagebox.showwarning("Modificar", "Selecciona un producto del carrito.")
            return
        item = self.carrito.buscar_item(id_producto)
        nueva = simpledialog.askinteger("Modificar cantidad",
                                        f"Nueva cantidad de {item.nombre}:",
                                        initialvalue=item.cantidad, minvalue=1, maxvalue=999,
                                        parent=self.ventana)
        if nueva is None:  # el usuario canceló
            return
        try:
            self.carrito.modificar_cantidad(id_producto, nueva)
        except CarritoError as error:
            messagebox.showerror("Error", str(error))
        self.actualizar_carrito()

    def eliminar(self):
        """Quita del carrito el producto seleccionado, después de confirmar."""
        id_producto = self.id_seleccionado(self.tabla_carrito)
        if id_producto is None:
            messagebox.showwarning("Eliminar", "Selecciona un producto del carrito.")
            return
        item = self.carrito.buscar_item(id_producto)
        if messagebox.askyesno("Eliminar", f"¿Seguro que quieres eliminar {item.nombre}?"):
            self.carrito.eliminar(id_producto)
            self.actualizar_carrito()

    def vaciar(self):
        """Quita todos los productos del carrito, después de confirmar."""
        if self.carrito.esta_vacio():
            messagebox.showinfo("Vaciar", "El carrito ya está vacío.")
            return
        if messagebox.askyesno("Vaciar", "¿Seguro que quieres vaciar el carrito?"):
            self.carrito.vaciar()
            self.actualizar_carrito()

    def finalizar(self):
        """Muestra el resumen de la compra y deja el carrito vacío."""
        if self.carrito.esta_vacio():
            messagebox.showinfo("Finalizar compra", "El carrito está vacío.")
            return

        resumen = "RESUMEN DE COMPRA\n\n"
        for item in self.carrito.items:
            resumen = resumen + f"{item.nombre}  x{item.cantidad}  =  {formatear_dinero(item.subtotal)}\n"
        resumen = resumen + f"\nProductos: {self.carrito.total_productos}"
        resumen = resumen + f"\nArtículos: {self.carrito.total_articulos}"
        resumen = resumen + f"\nTotal a pagar: {formatear_dinero(self.carrito.total)}"
        resumen = resumen + "\n\nGracias por su compra."
        messagebox.showinfo("Finalizar compra", resumen)

        self.carrito.vaciar()  # la compra termina y el carrito se reinicia
        self.actualizar_carrito()

    # ===================== APOYO =====================

    def id_seleccionado(self, tabla):
        """Regresa el ID del renglón seleccionado en una tabla, o None si no hay."""
        seleccion = tabla.selection()
        if len(seleccion) == 0:
            return None
        valores = tabla.item(seleccion[0], "values")
        return int(valores[0])
