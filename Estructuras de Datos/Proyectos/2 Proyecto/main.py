"""Inicio del programa del carrito de compras en modo gráfico.

Para la versión de consola usar: python carrito_compras.py

Equipo ProyectoFinal 7 - Proyecto 2
"""

from ventana_carrito import VentanaCarrito


def main():
    """Abre la ventana del carrito de compras."""
    ventana = VentanaCarrito()
    ventana.ejecutar()


if __name__ == "__main__":
    main()
