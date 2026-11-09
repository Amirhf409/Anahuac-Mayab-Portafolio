"""Funciones de apoyo que usan las demás partes del programa.

Equipo ProyectoFinal 7 - Proyecto 2
"""

import unicodedata


def normalizar(texto):
    """Pasa el texto a minúsculas y le quita los acentos.

    Sirve para comparar nombres sin que importen los acentos,
    por ejemplo 'Audífonos' y 'audifonos' quedan iguales.
    """
    sin_acentos = unicodedata.normalize("NFD", texto)
    resultado = ""
    for letra in sin_acentos:
        if not unicodedata.combining(letra):  # combining = el acento separado de la letra
            resultado = resultado + letra
    return resultado.casefold().strip()


def formatear_dinero(monto):
    """Regresa el monto como texto de dinero: 450 -> '$450' y 450.5 -> '$450.50'."""
    if float(monto).is_integer():
        return f"${int(monto)}"
    return f"${monto:.2f}"


def filtrar_por_referencia(elementos, referencia):
    """Busca elementos (productos o renglones del carrito) por ID o por nombre.

    Si la referencia es un número se busca por ID. Si es texto, primero se
    buscan nombres exactos y, si no hay, nombres que contengan el texto.

    Parámetros:
        elementos (list): objetos que tienen .id y .nombre.
        referencia (str): lo que escribió el usuario.

    Regresa:
        list: los elementos que coinciden (puede estar vacía).
    """
    ref = referencia.strip()
    if not ref:
        return []

    if ref.isascii() and ref.isdigit():
        por_id = []
        for elemento in elementos:
            if elemento.id == int(ref):
                por_id.append(elemento)
        return por_id

    ref_norm = normalizar(ref)
    exactos = []
    parciales = []
    for elemento in elementos:
        nombre = normalizar(elemento.nombre)
        if nombre == ref_norm:
            exactos.append(elemento)
        elif ref_norm in nombre:
            parciales.append(elemento)

    if exactos:
        return exactos
    return parciales
