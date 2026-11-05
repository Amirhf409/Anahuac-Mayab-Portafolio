# pagina.py
# Pagina es la clase padre y de ella heredan PaginaWeb y PaginaNoEncontrada.
# Se hizo asi para que el navegador pueda guardar los dos tipos en la misma
# pila sin tener que distinguirlos.


class Pagina:

    def __init__(self, url, titulo):
        self.url = url
        self.titulo = titulo

    # Las clases hijas sobrescriben este metodo con su propio texto
    def verDescripcion(self):
        return ""

    def __str__(self):
        return self.url


class PaginaWeb(Pagina):
    # La pagina si aparece en el catalogo

    def __init__(self, url, descripcion):
        super().__init__(url, url)      # en este tipo de pagina el titulo es la misma URL
        self.descripcion = descripcion

    def verDescripcion(self):
        return self.descripcion


class PaginaNoEncontrada(Pagina):
    # La pagina no aparece en el catalogo, o sea el error 404

    def __init__(self, url):
        super().__init__(url, "404 - Pagina no encontrada")

    def verDescripcion(self):
        return "No se encontro el sitio " + self.url
