# navegador.py
# Clase Navegador. Maneja el historial con dos pilas:
#   pilaAtras    -> las paginas por las que ya pasamos
#   pilaAdelante -> las paginas a las que podemos volver despues de un Back

from pagina import PaginaWeb, PaginaNoEncontrada
from pila import Pila

# Sitios que el navegador conoce. Si la URL no esta aqui se manda un 404.
CATALOGO = {
    "https://www.google.com": "Sitio oficial de Google",
    "https://www.mozilla.org": "Bienvenido a Mozilla",
    "https://openai.com": "Sitio oficial de OpenAI",
    "https://stackoverflow.com": "Bienvenido a Stack Overflow",
    "https://merida.anahuac.mx": "Bienvenido a la Universidad Anahuac Mayab",
    "https://github.com": "Sitio oficial de GitHub",
    "https://www.youtube.com": "Bienvenido a YouTube",
    "https://www.wikipedia.org": "La enciclopedia libre",
}


class Navegador:
    # Aplica las tres reglas del proyecto sobre las dos pilas

    def __init__(self):
        self.pilaAtras = Pila()
        self.pilaAdelante = Pila()
        self.paginaActual = None

    def visitar(self, url):
        direccion = self.limpiarUrl(url)

        if direccion == "":
            return "Tienes que escribir una URL."

        # La primera vez que se abre el programa no hay pagina que guardar
        if self.paginaActual != None:

            # Si el historial ya no tiene espacio no cambiamos de pagina,
            # porque perderiamos la que estamos viendo
            if self.pilaAtras.estaLlena():
                return "PILA LLENA: el historial de atras ya guarda " + \
                       str(self.pilaAtras.capacidad) + " paginas. " + \
                       "Usa Back antes de visitar otra pagina."

            self.pilaAtras.apilar(self.paginaActual)

        self.paginaActual = self.buscarPagina(direccion)

        # Desde una pagina nueva ya no existe camino hacia adelante
        self.pilaAdelante.vaciar()

        return "Visitaste " + direccion

    def retroceder(self):
        if self.pilaAtras.estaVacia():
            return "PILA VACIA: no hay paginas anteriores para regresar."

        if self.pilaAdelante.estaLlena():
            return "PILA LLENA: el historial de adelante ya esta lleno."

        self.pilaAdelante.apilar(self.paginaActual)
        self.paginaActual = self.pilaAtras.desapilar()

        return "Regresaste a " + self.paginaActual.url

    # Es lo mismo que retroceder pero intercambiando las dos pilas
    def avanzar(self):
        if self.pilaAdelante.estaVacia():
            return "PILA VACIA: no hay paginas siguientes para avanzar."

        if self.pilaAtras.estaLlena():
            return "PILA LLENA: el historial de atras ya esta lleno."

        self.pilaAtras.apilar(self.paginaActual)
        self.paginaActual = self.pilaAdelante.desapilar()

        return "Avanzaste a " + self.paginaActual.url

    def limpiarUrl(self, url):
        direccion = url.strip().lower()

        # Sin esto "https://github.com/" y "https://github.com" se tomarian
        # como dos paginas distintas
        if direccion.endswith("/"):
            direccion = direccion[0:len(direccion) - 1]

        return direccion

    # Aqui se usa la herencia: las dos opciones que puede regresar son hijas
    # de Pagina, asi que el resto del programa las trata igual
    def buscarPagina(self, direccion):
        if direccion in CATALOGO:
            return PaginaWeb(direccion, CATALOGO[direccion])

        return PaginaNoEncontrada(direccion)

    def sitiosDisponibles(self):
        return list(CATALOGO.keys())
