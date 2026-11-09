"""Clases del carrito de compras: productos, catálogo y carrito.

Aquí está toda la lógica del programa. No usa print() ni input(),
por eso la pueden usar igual la versión de consola y la ventana.

Equipo ProyectoFinal 7 - Proyecto 2
"""


class CarritoError(Exception):
    """Error del carrito, por ejemplo una cantidad inválida o un producto que no existe."""


class Producto:
    """Un producto del catálogo.

    Atributos:
        id (int): número que identifica al producto.
        nombre (str): nombre del producto.
        categoria (str): categoría a la que pertenece.
        precio (float): precio por unidad, no puede ser negativo.
    """

    def __init__(self, id_producto, nombre, categoria, precio):
        """Crea el producto y revisa que el precio no sea negativo.

        Lanza:
            CarritoError: si el precio es menor que 0.
        """
        if precio < 0:
            raise CarritoError("El precio de un producto no puede ser negativo.")
        self.id = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio


class ItemCarrito:
    """Un renglón del carrito: un producto y cuántas unidades se quieren comprar.

    id, nombre y precio se toman del producto, así no se guardan dos veces.
    """

    def __init__(self, producto, cantidad):
        """Guarda el producto y la cantidad (la cantidad se valida en su setter)."""
        self.producto = producto
        self.cantidad = cantidad

    @property
    def id(self):
        """ID del producto."""
        return self.producto.id

    @property
    def nombre(self):
        """Nombre del producto."""
        return self.producto.nombre

    @property
    def precio(self):
        """Precio por unidad del producto."""
        return self.producto.precio

    @property
    def cantidad(self):
        """Cantidad de unidades de este producto en el carrito."""
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        """Cambia la cantidad solo si es un entero mayor o igual a 1.

        Lanza:
            CarritoError: si la cantidad no es válida.
        """
        if not isinstance(valor, int) or valor < 1:
            raise CarritoError("La cantidad debe ser un número entero mayor o igual a 1.")
        self._cantidad = valor

    @property
    def subtotal(self):
        """Precio por cantidad de este renglón."""
        return self.precio * self.cantidad


class Catalogo:
    """Lista de productos que vende la tienda."""

    def __init__(self, productos=None):
        """Crea el catálogo, vacío o con una lista de productos inicial."""
        self.productos = []
        if productos:
            for producto in productos:
                self.productos.append(producto)

    def agregar(self, producto):
        """Agrega un producto al catálogo.

        Lanza:
            CarritoError: si ya existe un producto con el mismo ID.
        """
        if self.buscar_por_id(producto.id) is not None:
            raise CarritoError(f"Ya existe un producto con ID {producto.id}.")
        self.productos.append(producto)

    def buscar_por_id(self, id_producto):
        """Regresa el producto con ese ID, o None si no existe."""
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None


class Carrito:
    """Carrito de compras, guarda una lista de ItemCarrito."""

    def __init__(self):
        """Crea el carrito vacío."""
        self.items = []

    def esta_vacio(self):
        """Regresa True si el carrito no tiene productos."""
        return len(self.items) == 0

    def buscar_item(self, id_producto):
        """Regresa el renglón del carrito con ese ID, o None si no está."""
        for item in self.items:
            if item.id == id_producto:
                return item
        return None

    def agregar(self, producto, cantidad):
        """Agrega un producto. Si ya estaba en el carrito, le suma la cantidad.

        Parámetros:
            producto (Producto): producto que se va a agregar.
            cantidad (int): unidades a agregar, mayor o igual a 1.

        Regresa:
            ItemCarrito: el renglón que se agregó o que se actualizó.

        Lanza:
            CarritoError: si la cantidad no es un entero mayor o igual a 1.
        """
        # revisamos la cantidad antes de sumar, para no aceptar negativos
        if not isinstance(cantidad, int) or cantidad < 1:
            raise CarritoError("La cantidad debe ser un número entero mayor o igual a 1.")
        item = self.buscar_item(producto.id)
        if item is None:
            item = ItemCarrito(producto, cantidad)
            self.items.append(item)
        else:
            item.cantidad = item.cantidad + cantidad
        return item

    def modificar_cantidad(self, id_producto, nueva_cantidad):
        """Cambia la cantidad de un producto que ya está en el carrito.

        Parámetros:
            id_producto (int): ID del producto a modificar.
            nueva_cantidad (int): cantidad nueva, mayor o igual a 1.

        Regresa:
            ItemCarrito: el renglón con la cantidad actualizada.

        Lanza:
            CarritoError: si el producto no está en el carrito o si la
                nueva cantidad no es un entero mayor o igual a 1.
        """
        item = self.buscar_item(id_producto)
        if item is None:
            raise CarritoError("Ese producto no está en el carrito.")
        item.cantidad = nueva_cantidad
        return item

    def eliminar(self, id_producto):
        """Quita un producto del carrito.

        Lanza:
            CarritoError: si el producto no está en el carrito.
        """
        item = self.buscar_item(id_producto)
        if item is None:
            raise CarritoError("Ese producto no está en el carrito.")
        self.items.remove(item)
        return item

    def vaciar(self):
        """Quita todos los productos del carrito."""
        self.items.clear()

    @property
    def total(self):
        """Suma de los subtotales de todos los renglones."""
        suma = 0
        for item in self.items:
            suma = suma + item.subtotal
        return suma

    @property
    def total_articulos(self):
        """Suma de las cantidades (cuántas piezas hay en total)."""
        suma = 0
        for item in self.items:
            suma = suma + item.cantidad
        return suma

    @property
    def total_productos(self):
        """Cuántos productos distintos hay en el carrito."""
        return len(self.items)


def catalogo_inicial():
    """Regresa el catálogo con los 5 productos de la tienda."""
    return Catalogo([
        Producto(1, "Teclado", "Accesorios", 450),
        Producto(2, "Mouse", "Accesorios", 250),
        Producto(3, "Monitor", "Electrónica", 3200),
        Producto(4, "Audífonos", "Audio", 800),
        Producto(5, "Memoria USB", "Almacenamiento", 180),
    ])
