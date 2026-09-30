"""
Árbol Binario de Búsqueda (ABB) a partir de una oración.

Decisiones de diseño (documentadas):
- Normalización: todo se pasa a minúsculas y se quitan signos de puntuación
  (¿?¡!.,;:"()- etc.). Los números y letras con acento se conservan.
- Comparación alfabética: se compara usando una "clave" SIN acentos
  (árbol -> arbol), porque Python compara por código Unicode y 'á' quedaría
  DESPUÉS de 'z'. Así "árbol" queda antes que "zorro", como en el diccionario.
- Duplicados: NO se crea un nodo nuevo. Cada nodo tiene un contador
  (frecuencia) que aumenta cuando la palabra se repite. Esto sirve para el
  objetivo de la empresa (analizar qué palabras se usan y cuántas veces).
"""

import string
import unicodedata

# Signos a limpiar (incluye los signos de apertura del español)
SIGNOS = string.punctuation + "¿¡«»“”‘’…"


class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.frecuencia = 1
        self.izq = None
        self.der = None

    def es_hoja(self):
        return self.izq is None and self.der is None


def clave(palabra):
    """Quita acentos para comparar alfabéticamente (ñ se respeta después de n)."""
    resultado = ""
    for letra in palabra:
        if letra == "ñ":
            resultado += "n~"  # queda entre 'n' y 'o'
        else:
            base = unicodedata.normalize("NFD", letra)
            resultado += "".join(c for c in base if unicodedata.category(c) != "Mn")
    return resultado


def limpiar_oracion(texto):
    """Minúsculas, sin puntuación, dividida en palabras."""
    palabras = []
    for p in texto.lower().split():
        p = p.strip(SIGNOS)
        if p:
            palabras.append(p)
    return palabras


class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    # ---------- Inserción ----------
    def insertar(self, palabra):
        if self.raiz is None:
            self.raiz = Nodo(palabra)
            return
        actual = self.raiz
        while True:
            if clave(palabra) < clave(actual.palabra):
                if actual.izq is None:
                    actual.izq = Nodo(palabra)
                    return
                actual = actual.izq
            elif clave(palabra) > clave(actual.palabra):
                if actual.der is None:
                    actual.der = Nodo(palabra)
                    return
                actual = actual.der
            else:  # duplicado
                actual.frecuencia += 1
                return

    # ---------- Recorridos ----------
    def inorden(self, n, lista):
        if n:
            self.inorden(n.izq, lista)
            lista.append(n)
            self.inorden(n.der, lista)
        return lista

    def preorden(self, n, lista):
        if n:
            lista.append(n)
            self.preorden(n.izq, lista)
            self.preorden(n.der, lista)
        return lista

    def postorden(self, n, lista):
        if n:
            self.postorden(n.izq, lista)
            self.postorden(n.der, lista)
            lista.append(n)
        return lista

    # ---------- Cálculos ----------
    def contar_nodos(self, n):
        if n is None:
            return 0
        return 1 + self.contar_nodos(n.izq) + self.contar_nodos(n.der)

    def hojas(self, n, lista):
        if n:
            if n.es_hoja():
                lista.append(n)
            self.hojas(n.izq, lista)
            self.hojas(n.der, lista)
        return lista

    def internos(self, n, lista):
        if n:
            if not n.es_hoja():
                lista.append(n)
            self.internos(n.izq, lista)
            self.internos(n.der, lista)
        return lista

    def maximo(self):
        """El máximo alfabético es el nodo más a la derecha."""
        if self.raiz is None:
            return None
        n = self.raiz
        while n.der:
            n = n.der
        return n

    # ---------- Dibujo en consola ----------
    def dibujar(self, n=None, prefijo="", lado=None, ultimo=True):
        """Dibuja el árbol en texto. lado = 'I' o 'D' (None para la raíz)."""
        if n is None:
            n = self.raiz
            if n is None:
                return ""
        etiqueta = n.palabra + (f" (x{n.frecuencia})" if n.frecuencia > 1 else "")
        if lado is None:
            texto = etiqueta + "\n"
            prefijo_hijos = ""
        else:
            texto = prefijo + ("└── " if ultimo else "├── ") + f"{lado}: " + etiqueta + "\n"
            prefijo_hijos = prefijo + ("    " if ultimo else "│   ")
        hijos = [(h, l) for h, l in ((n.izq, "I"), (n.der, "D")) if h]
        for i, (h, l) in enumerate(hijos):
            texto += self.dibujar(h, prefijo_hijos, l, i == len(hijos) - 1)
        return texto


def fmt(nodos):
    return ", ".join(n.palabra + (f"(x{n.frecuencia})" if n.frecuencia > 1 else "") for n in nodos) or "(ninguno)"


def analizar(texto):
    palabras = limpiar_oracion(texto)
    arbol = ArbolBusqueda()
    for p in palabras:
        arbol.insertar(p)

    print(f"\nOración: {texto!r}")
    print(f"Palabras limpias: {palabras}")
    if arbol.raiz is None:
        print("No hay palabras válidas; el árbol está vacío.")
        return arbol

    print("\nÁrbol (I = izquierdo, D = derecho):")
    print(arbol.dibujar())
    print("Inorden:   ", fmt(arbol.inorden(arbol.raiz, [])))
    print("Preorden:  ", fmt(arbol.preorden(arbol.raiz, [])))
    print("Postorden: ", fmt(arbol.postorden(arbol.raiz, [])))
    hojas = arbol.hojas(arbol.raiz, [])
    internos = arbol.internos(arbol.raiz, [])
    print("\nTotal de nodos:        ", arbol.contar_nodos(arbol.raiz))
    print("Nodos internos:        ", len(internos))
    print("Palabra máxima (alfab.):", arbol.maximo().palabra)
    print("Info en las hojas:     ", fmt(hojas))
    print("Info en nodos internos:", fmt(internos))
    return arbol


if __name__ == "__main__":
    texto = input("Escribe una oración: ")
    analizar(texto)
