class Usuario:

    # Declaración de los atributos es en el método __init__
    def __init__(self, nombre="", apellidos="", edad=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    # Declaración de setter y getter
    # Python exige que se programe los getter con @property
    @property
    def nombre(self): #get de __nombre
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre): #set de __nombre
        self.__nombre = nombre

    @property
    def apellidos(self): #get de __apellidos
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos): #set de __apellidos
        self.__apellidos = apellidos

    @property
    def edad(self): #get de __edad
        return self.__edad

    @edad.setter
    def edad(self, edad): #set de __edad
        self.__edad = edad

    # Métodos
    def iniciarSesion(self):
        return f"El usuario {self.nombre} esta iniciando sesión."

    def cerrarSesion(self):
        return f"El usuario {self.nombre} ha cerrando la sesión."

    def hacerReporte(self):
        return f"Reporte de usuario\nNombre Completo: {self.nombre} {self.apellidos}\nEdad: {self.edad}"