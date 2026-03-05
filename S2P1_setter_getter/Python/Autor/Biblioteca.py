class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self): #Equivalente al método toString
        return f"Autor: {self.nombre}\nNacionalidad: {self.nacionalidad}"

class Libro:
    def __init__(self, titulo, anioPublicacion, autor):
        self.titulo = titulo
        self.anioPublicacion = anioPublicacion
        self.autor = autor #Objeto de la clase Autor como Atributo

    def __str__(self): 
        return f"{self.autor}\nTitulo: {self.titulo}\nAnio Publicacion: {self.anioPublicacion}"