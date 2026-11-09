"""Pruebas del carrito de compras.

Revisan que la lógica siga funcionando igual después de separar el código
en archivos. Se corren con: python pruebas.py

Equipo ProyectoFinal 7 - Proyecto 2
"""

from modelo import Carrito, CarritoError, Producto, catalogo_inicial
from utilidades import filtrar_por_referencia, formatear_dinero, normalizar

# Aquí voy guardando True o False por cada prueba
resultados = []


def verificar(nombre, obtenido, esperado):
    """Compara lo que salió contra lo esperado y lo guarda en resultados."""
    if obtenido == esperado:
        resultados.append(True)
        print(f"  [OK]    {nombre}")
    else:
        resultados.append(False)
        print(f"  [FALLA] {nombre}")
        print(f"          esperado: {esperado}")
        print(f"          obtenido: {obtenido}")


def lanza_error(funcion):
    """Regresa True si la función lanza un CarritoError."""
    try:
        funcion()
    except CarritoError:
        return True
    return False


def probar_utilidades():
    """Pruebas de normalizar, formatear_dinero y filtrar_por_referencia."""
    print("\nUtilidades")
    verificar("normalizar quita acentos y mayúsculas", normalizar("Audífonos"), "audifonos")
    verificar("dinero entero", formatear_dinero(450), "$450")
    verificar("dinero con centavos", formatear_dinero(450.5), "$450.50")

    productos = catalogo_inicial().productos
    verificar("buscar por ID 3", filtrar_por_referencia(productos, "3")[0].nombre, "Monitor")
    verificar("buscar por nombre sin acento", filtrar_por_referencia(productos, "audifonos")[0].id, 4)
    verificar("buscar por parte del nombre", filtrar_por_referencia(productos, "mem")[0].id, 5)
    verificar("búsqueda sin resultados", filtrar_por_referencia(productos, "laptop"), [])
    verificar("buscar 'mo' da 3 productos", len(filtrar_por_referencia(productos, "mo")), 3)


def probar_catalogo():
    """Pruebas del catálogo."""
    print("\nCatálogo")
    catalogo = catalogo_inicial()
    verificar("el catálogo tiene 5 productos", len(catalogo.productos), 5)
    verificar("buscar_por_id(2)", catalogo.buscar_por_id(2).nombre, "Mouse")
    verificar("buscar_por_id inexistente", catalogo.buscar_por_id(99), None)
    verificar("no deja repetir un ID", lanza_error(lambda: catalogo.agregar(Producto(1, "X", "Y", 10))), True)
    verificar("no deja precio negativo", lanza_error(lambda: Producto(9, "X", "Y", -5)), True)


def probar_carrito():
    """Pruebas de agregar, modificar, eliminar, vaciar y los totales."""
    print("\nCarrito")
    catalogo = catalogo_inicial()
    carrito = Carrito()
    verificar("empieza vacío", carrito.esta_vacio(), True)

    carrito.agregar(catalogo.buscar_por_id(1), 2)   # 2 teclados de $450
    carrito.agregar(catalogo.buscar_por_id(4), 1)   # 1 audífonos de $800
    verificar("total 2x450 + 1x800", carrito.total, 1700)
    verificar("total de artículos", carrito.total_articulos, 3)
    verificar("total de productos", carrito.total_productos, 2)

    carrito.agregar(catalogo.buscar_por_id(1), 1)
    verificar("agregar uno repetido suma la cantidad", carrito.buscar_item(1).cantidad, 3)
    verificar("y no crea otro renglón", carrito.total_productos, 2)
    teclado = catalogo.buscar_por_id(1)
    verificar("no deja agregar cantidades negativas", lanza_error(lambda: carrito.agregar(teclado, -1)), True)
    verificar("y la cantidad no cambia", carrito.buscar_item(1).cantidad, 3)

    carrito.modificar_cantidad(4, 2)
    verificar("modificar cantidad", carrito.total, 3 * 450 + 2 * 800)
    verificar("cantidad 0 no se permite", lanza_error(lambda: carrito.modificar_cantidad(4, 0)), True)
    verificar("modificar algo que no está", lanza_error(lambda: carrito.modificar_cantidad(5, 1)), True)

    carrito.eliminar(1)
    verificar("eliminar producto", carrito.total_productos, 1)
    verificar("eliminar algo que no está", lanza_error(lambda: carrito.eliminar(1)), True)

    carrito.vaciar()
    verificar("vaciar carrito", carrito.esta_vacio(), True)
    verificar("total del carrito vacío", carrito.total, 0)


def main():
    """Corre todas las pruebas y muestra cuántas salieron bien."""
    print("PRUEBAS DEL PROYECTO 2 - CARRITO DE COMPRAS")
    probar_utilidades()
    probar_catalogo()
    probar_carrito()

    correctas = 0
    for resultado in resultados:
        if resultado:
            correctas = correctas + 1

    print()
    print(f"Pruebas correctas: {correctas} de {len(resultados)}")
    if correctas == len(resultados):
        print("Todas las pruebas se ejecutaron correctamente.")


if __name__ == "__main__":
    main()
