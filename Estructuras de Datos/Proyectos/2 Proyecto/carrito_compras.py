"""Versión de consola del carrito de compras (menú de texto).

Es la interfaz original del proyecto. La lógica ahora está en modelo.py,
así que este archivo solo pide datos y muestra resultados en la terminal.
Para la versión con ventana usar main.py.

Equipo ProyectoFinal 7 - Proyecto 2
"""

import os
import sys

from modelo import Carrito, CarritoError, catalogo_inicial
from utilidades import filtrar_por_referencia, formatear_dinero, normalizar


def construir_tabla(encabezados, filas, alineacion):
    """Arma una tabla de texto y la regresa como lista de líneas.

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
        """Crea el catálogo con los productos de la tienda y un carrito vacío."""
        self.catalogo = catalogo_inicial()
        self.carrito = Carrito()

    # entrada / salida 
    @staticmethod
    def limpiar_pantalla():
        """Borra la pantalla de la terminal (cls en Windows, clear en Linux/Mac)."""
        if sys.stdout.isatty():
            os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def pausar(mensaje="Presione ENTER para continuar..."):
        """Espera a que el usuario presione ENTER."""
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
        """Imprime un título centrado, por ejemplo === CARRITO DE COMPRAS ===."""
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
        """Imprime solo ID y nombre, se usa cuando hay varias coincidencias."""
        for linea in construir_tabla(
            ["ID", "Producto"], [[e.id, e.nombre] for e in elementos], "id"
        ):
            print(linea)

    # ----- pantallas -----
    def imprimir_catalogo(self, productos, titulo="CATÁLOGO DE PRODUCTOS"):
        """Imprime una tabla con los productos que recibe."""
        filas = [[p.id, p.nombre, p.categoria, formatear_dinero(p.precio)] for p in productos]
        tabla = construir_tabla(["ID", "Producto", "Categoría", "Precio"], filas, "iiid")
        self.titulo(titulo, len(tabla[0]))
        for linea in tabla:
            print(linea)

    def imprimir_carrito(self, titulo="CARRITO DE COMPRAS", con_precio=True):
        """Imprime el carrito en una tabla y regresa el ancho de la tabla."""
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
        """Limpia la pantalla e imprime las 9 opciones del menú."""
        self.limpiar_pantalla()
        self.titulo("CARRITO DE COMPRAS")
        print()
        for numero, texto in enumerate(self.OPCIONES_MENU, start=1):
            print(f"{numero}. {texto}")
        print()

    def opcion_mostrar_catalogo(self):
        """Opción 1: muestra todos los productos."""
        self.imprimir_catalogo(self.catalogo.productos)
        self.pausar("Presione ENTER para volver al menú...")

    def opcion_buscar(self):
        """Opción 2: busca productos por ID o por nombre."""
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
            # misma búsqueda que al agregar: primero nombre exacto y luego parcial
            resultados = filtrar_por_referencia(self.catalogo.productos, texto)
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
        """Opción 3: pide un producto y una cantidad y lo agrega al carrito."""
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
        """Opción 4: muestra el carrito con su total."""
        if self.carrito_vacio():
            return
        ancho = self.imprimir_carrito()
        print(f"TOTAL: {formatear_dinero(self.carrito.total)}".rjust(ancho))
        self.pausar("Presione ENTER para volver al menú...")

    def opcion_modificar(self):
        """Opción 5: cambia la cantidad de un producto del carrito."""
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
        """Opción 6: quita un producto del carrito (pide confirmación)."""
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
        """Opción 7: quita todos los productos (pide confirmación)."""
        if self.carrito_vacio():
            return
        if self.confirmar("¿Está seguro que desea vaciar el carrito?"):
            self.carrito.vaciar()
            print("\n¡Carrito vaciado!")
        else:
            print("\nOperación cancelada.")
        self.pausar()

    def opcion_finalizar(self):
        """Opción 8: muestra el resumen de la compra y vacía el carrito."""
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
        """Repite el menú hasta que el usuario elige 9 (Salir)."""
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
    """Inicia la versión de consola."""
    # Evita que un carácter no soportado por la consola detenga el programa.
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(errors="replace")
        except (AttributeError, ValueError):
            pass
    AplicacionCarrito().ejecutar()


if __name__ == "__main__":
    main()