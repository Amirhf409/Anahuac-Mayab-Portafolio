"""Carrito de compras 
Equipo 7 - Proyecto final 
"""

import os
import sys
import unicodedata



# Utilidades

class CarritoError(Exception):
    """Error de negocio (producto inexistente, cantidad inválida, etc.)."""


def normalizar(texto):
    """Minúsculas y sin acentos, para comparar nombres ('Audífonos' == 'audifonos')."""
    sin_acentos = unicodedata.normalize("NFD", texto)
    sin_acentos = "".join(c for c in sin_acentos if not unicodedata.combining(c))
    return sin_acentos.casefold().strip()


def formatear_dinero(monto):
    """450 -> '$450'; 450.5 -> '$450.50'."""
    if float(monto).is_integer():
        return f"${int(monto)}"
    return f"${monto:.2f}"


def construir_tabla(encabezados, filas, alineacion):
    """Devuelve la tabla como lista de líneas de texto.

    alineacion: una letra por columna, 'i' (izquierda) o 'd' (derecha).
    """
    filas_txt = [[str(celda) for celda in fila] for fila in filas]
    anchos = [len(h) for h in encabezados]
    for fila in filas_txt:
        for i, celda in enumerate(fila):
            anchos[i] = max(anchos[i], len(celda))

    def formatear(fila):
        celdas = [
            celda.ljust(anchos[i]) if alineacion[i] == "i" else celda.rjust(anchos[i])
            for i, celda in enumerate(fila)
        ]
        return " | ".join(celdas)

    encabezado = formatear(encabezados)
    linea = "-" * len(encabezado)
    return [linea, encabezado, linea] + [formatear(f) for f in filas_txt] + [linea]


def filtrar_por_referencia(elementos, referencia):
    """Busca en una lista de elementos con .id y .nombre.

    Si la referencia es un número se busca por ID; si no, por nombre
    (coincidencia exacta primero y, si no hay, coincidencia parcial).
    """
    ref = referencia.strip()
    if not ref:
        return []
    if ref.isascii() and ref.isdigit():
        return [e for e in elementos if e.id == int(ref)]
    ref_norm = normalizar(ref)
    exactos = [e for e in elementos if normalizar(e.nombre) == ref_norm]
    if exactos:
        return exactos
    return [e for e in elementos if ref_norm in normalizar(e.nombre)]



# Modelo

class Producto:
    """Producto del catálogo: ID, nombre, categoría y precio."""

    def __init__(self, id_producto, nombre, categoria, precio):
        if precio < 0:
            raise CarritoError("El precio de un producto no puede ser negativo.")
        self.id = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def como_lista(self):
        return [self.id, self.nombre, self.precio]


class ItemCarrito:
    """Línea del carrito: un producto y la cantidad que se desea comprar."""

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    @property
    def id(self):
        return self.producto.id

    @property
    def nombre(self):
        return self.producto.nombre

    @property
    def precio(self):
        return self.producto.precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if not isinstance(valor, int) or valor < 1:
            raise CarritoError("La cantidad debe ser un número entero mayor o igual a 1.")
        self._cantidad = valor

    @property
    def subtotal(self):
        return self.precio * self.cantidad

    def como_lista(self):
        return [self.id, self.nombre, self.precio, self.cantidad]


class Catalogo:
    """Catálogo de productos, almacenado en una lista."""

    def __init__(self, productos=None):
        self.productos = list(productos) if productos else []

    def agregar(self, producto):
        if self.buscar_por_id(producto.id) is not None:
            raise CarritoError(f"Ya existe un producto con ID {producto.id}.")
        self.productos.append(producto)

    def buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None

    def buscar_por_nombre(self, texto):
        """Productos cuyo nombre contiene el texto (sin distinguir acentos ni mayúsculas)."""
        texto_norm = normalizar(texto)
        if not texto_norm:
            return []
        return [p for p in self.productos if texto_norm in normalizar(p.nombre)]


class Carrito:
    """Carrito de compras, almacenado en una lista de ItemCarrito."""

    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def buscar_item(self, id_producto):
        for item in self.items:
            if item.id == id_producto:
                return item
        return None

    def agregar(self, producto, cantidad):
        """Agrega el producto; si ya estaba en el carrito suma la cantidad."""
        item = self.buscar_item(producto.id)
        if item is None:
            item = ItemCarrito(producto, cantidad)
            self.items.append(item)
        else:
            item.cantidad = item.cantidad + cantidad
        return item

    def modificar_cantidad(self, id_producto, nueva_cantidad):
        item = self.buscar_item(id_producto)
        if item is None:
            raise CarritoError("Ese producto no está en el carrito.")
        item.cantidad = nueva_cantidad
        return item

    def eliminar(self, id_producto):
        item = self.buscar_item(id_producto)
        if item is None:
            raise CarritoError("Ese producto no está en el carrito.")
        self.items.remove(item)
        return item

    def vaciar(self):
        self.items.clear()

    @property
    def total(self):
        return sum(item.subtotal for item in self.items)

    @property
    def total_articulos(self):
        return sum(item.cantidad for item in self.items)

    @property
    def total_productos(self):
        return len(self.items)


def catalogo_inicial():
    """Catálogo precargado de la tienda."""
    return Catalogo([
        Producto(1, "Teclado", "Accesorios", 450),
        Producto(2, "Mouse", "Accesorios", 250),
        Producto(3, "Monitor", "Electrónica", 3200),
        Producto(4, "Audífonos", "Audio", 800),
        Producto(5, "Memoria USB", "Almacenamiento", 180),
    ])


# Interfaz de consola

class AplicacionCarrito:
    """Menú de consola que conecta al usuario con el catálogo y el carrito."""

    OPCIONES_MENU = [
        "Mostrar catálogo",
        "Buscar producto",
        "Agregar producto al carrito",
        "Ver carrito",
        "Modificar cantidad",
        "Eliminar producto",
        "Vaciar carrito",
        "Finalizar compra",
        "Salir",
    ]

    def __init__(self):
        self.catalogo = catalogo_inicial()
        self.carrito = Carrito()

    # entrada / salida 
    @staticmethod
    def limpiar_pantalla():
        if sys.stdout.isatty():
            os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def pausar(mensaje="Presione ENTER para continuar..."):
        print()
        input(mensaje)

    @staticmethod
    def leer_entero_positivo(mensaje):
        """Pide un entero >= 1. Devuelve None si el usuario deja la entrada vacía."""
        while True:
            texto = input(mensaje).strip()
            if not texto:
                return None
            if texto.isascii() and texto.isdigit() and int(texto) >= 1:
                return int(texto)
            print("Entrada inválida: escriba un número entero mayor o igual a 1 "
                  "(ENTER para cancelar).")

    @staticmethod
    def confirmar(mensaje):
        """Pregunta (s/n) hasta recibir una respuesta válida."""
        while True:
            respuesta = normalizar(input(f"{mensaje} (s/n): "))
            if respuesta in ("s", "si"):
                return True
            if respuesta in ("n", "no"):
                return False
            print("Responda 's' para sí o 'n' para no.")

    @staticmethod
    def titulo(texto, ancho=0):
        print()
        print(f"=== {texto} ===".center(ancho))

    def elegir(self, elementos, mensaje):
        """Pide un ID o nombre y devuelve el elemento elegido (None si se cancela)."""
        while True:
            referencia = input(mensaje).strip()
            if not referencia:
                return None
            coincidencias = filtrar_por_referencia(elementos, referencia)
            if len(coincidencias) == 1:
                return coincidencias[0]
            if not coincidencias:
                print(f"No se encontró ningún producto con '{referencia}' "
                      "(ENTER para cancelar).")
            else:
                print("Hay varias coincidencias, indique el ID del producto:")
                self.imprimir_lista_corta(coincidencias)

    @staticmethod
    def imprimir_lista_corta(elementos):
        for linea in construir_tabla(
            ["ID", "Producto"], [[e.id, e.nombre] for e in elementos], "id"
        ):
            print(linea)

    # ----- pantallas -----
    def imprimir_catalogo(self, productos, titulo="CATÁLOGO DE PRODUCTOS"):
        filas = [[p.id, p.nombre, p.categoria, formatear_dinero(p.precio)] for p in productos]
        tabla = construir_tabla(["ID", "Producto", "Categoría", "Precio"], filas, "iiid")
        self.titulo(titulo, len(tabla[0]))
        for linea in tabla:
            print(linea)

    def imprimir_carrito(self, titulo="CARRITO DE COMPRAS", con_precio=True):
        if con_precio:
            encabezados = ["ID", "Producto", "Precio", "Cant.", "Subtotal"]
            filas = [[i.id, i.nombre, formatear_dinero(i.precio), i.cantidad,
                      formatear_dinero(i.subtotal)] for i in self.carrito.items]
            alineacion = "iiddd"
        else:
            encabezados = ["ID", "Producto", "Cant.", "Subtotal"]
            filas = [[i.id, i.nombre, i.cantidad, formatear_dinero(i.subtotal)]
                     for i in self.carrito.items]
            alineacion = "iidd"
        tabla = construir_tabla(encabezados, filas, alineacion)
        self.titulo(titulo, len(tabla[0]))
        for linea in tabla:
            print(linea)
        return len(tabla[0])

    def carrito_vacio(self):
        """Avisa si el carrito está vacío. Devuelve True en ese caso."""
        if self.carrito.esta_vacio():
            print("\nEl carrito está vacío.")
            self.pausar()
            return True
        return False

    # ----- opciones del menú -----
    def mostrar_menu(self):
        self.limpiar_pantalla()
        self.titulo("CARRITO DE COMPRAS")
        print()
        for numero, texto in enumerate(self.OPCIONES_MENU, start=1):
            print(f"{numero}. {texto}")
        print()

    def opcion_mostrar_catalogo(self):
        self.imprimir_catalogo(self.catalogo.productos)
        self.pausar("Presione ENTER para volver al menú...")

    def opcion_buscar(self):
        print("\nBuscar producto")
        print("1. Por ID")
        print("2. Por nombre")
        modo = input("Seleccione una opción (ENTER para cancelar): ").strip()
        if modo == "1":
            id_producto = self.leer_entero_positivo("ID del producto: ")
            if id_producto is None:
                return
            producto = self.catalogo.buscar_por_id(id_producto)
            resultados = [producto] if producto else []
        elif modo == "2":
            texto = input("Nombre del producto: ").strip()
            if not texto:
                return
            resultados = self.catalogo.buscar_por_nombre(texto)
        elif modo == "":
            return
        else:
            print("Opción inválida. Elija 1 o 2.")
            self.pausar()
            return

        if resultados:
            self.imprimir_catalogo(resultados, "RESULTADOS DE LA BÚSQUEDA")
        else:
            print("\nNo se encontraron productos.")
        self.pausar()

    def opcion_agregar(self):
        producto = self.elegir(self.catalogo.productos,
                               "ID o nombre del producto (ENTER para cancelar): ")
        if producto is None:
            return
        print(f"Producto: {producto.nombre}")
        print(f"Precio unitario: {formatear_dinero(producto.precio)}")
        cantidad = self.leer_entero_positivo("Cantidad: ")
        if cantidad is None:
            return
        item = self.carrito.agregar(producto, cantidad)
        print("\n¡Producto agregado al carrito!")
        if item.cantidad != cantidad:
            print(f"(Ya estaba en el carrito: ahora lleva {item.cantidad} unidades.)")
        self.pausar()

    def opcion_ver_carrito(self):
        if self.carrito_vacio():
            return
        ancho = self.imprimir_carrito()
        print(f"TOTAL: {formatear_dinero(self.carrito.total)}".rjust(ancho))
        self.pausar("Presione ENTER para volver al menú...")

    def opcion_modificar(self):
        if self.carrito_vacio():
            return
        item = self.elegir(self.carrito.items,
                           "ID o nombre del producto a modificar (ENTER para cancelar): ")
        if item is None:
            return
        print(f"Producto: {item.nombre}")
        print(f"Cantidad actual: {item.cantidad}")
        nueva = self.leer_entero_positivo("Nueva cantidad: ")
        if nueva is None:
            return
        self.carrito.modificar_cantidad(item.id, nueva)
        print("\n¡Cantidad actualizada!")
        print(f"Nuevo subtotal: {formatear_dinero(item.subtotal)}")
        print(f"Total del carrito: {formatear_dinero(self.carrito.total)}")
        self.pausar()

    def opcion_eliminar(self):
        if self.carrito_vacio():
            return
        item = self.elegir(self.carrito.items,
                           "ID o nombre del producto a eliminar (ENTER para cancelar): ")
        if item is None:
            return
        print(f"Producto: {item.nombre}")
        if self.confirmar("¿Está seguro que desea eliminar este producto?"):
            self.carrito.eliminar(item.id)
            print("\n¡Producto eliminado del carrito!")
        else:
            print("\nOperación cancelada.")
        self.pausar()

    def opcion_vaciar(self):
        if self.carrito_vacio():
            return
        if self.confirmar("¿Está seguro que desea vaciar el carrito?"):
            self.carrito.vaciar()
            print("\n¡Carrito vaciado!")
        else:
            print("\nOperación cancelada.")
        self.pausar()

    def opcion_finalizar(self):
        if self.carrito_vacio():
            return
        self.imprimir_carrito("RESUMEN DE COMPRA", con_precio=False)
        print()
        print(f"Productos:     {self.carrito.total_productos}")
        print(f"Artículos:     {self.carrito.total_articulos}")
        print(f"Total a pagar: {formatear_dinero(self.carrito.total)}")
        print("\nGracias por su compra.")
        self.carrito.vaciar()  # la compra termina y el carrito se reinicia
        self.pausar("Presione ENTER para volver al menú...")

    # ----- ciclo principal -----
    def ejecutar(self):
        acciones = {
            "1": self.opcion_mostrar_catalogo,
            "2": self.opcion_buscar,
            "3": self.opcion_agregar,
            "4": self.opcion_ver_carrito,
            "5": self.opcion_modificar,
            "6": self.opcion_eliminar,
            "7": self.opcion_vaciar,
            "8": self.opcion_finalizar,
        }
        try:
            while True:
                self.mostrar_menu()
                opcion = input("Seleccione una opción: ").strip()
                if opcion == "9":
                    break
                accion = acciones.get(opcion)
                if accion is None:
                    print("Opción inválida. Ingrese un número del 1 al 9.")
                    self.pausar()
                    continue
                try:
                    accion()
                except CarritoError as error:
                    print(f"\nError: {error}")
                    self.pausar()
        except (KeyboardInterrupt, EOFError):
            print()
        print("\nGracias por usar el programa.")
        print("¡Hasta pronto!")
        print("\nPrograma finalizado.")


def main():
    # Evita que un carácter no soportado por la consola detenga el programa.
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(errors="replace")
        except (AttributeError, ValueError):
            pass
    AplicacionCarrito().ejecutar()


if __name__ == "__main__":
    main()