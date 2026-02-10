class Empleado:

    def __init__(self, n="NULL", a=0, s=0.0):
        self.nombre = n
        self.anioContratacion = a
        self.salario = s

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    @property
    def anioContratacion(self):
        return self.__anioContratacion

    @anioContratacion.setter
    def anioContratacion(self, a):
        self.__anioContratacion = a

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, s):
        self.__salario = s

    def toString(self):
        return self.__nombre + " " + str(self.__anioContratacion) + " " + str(self.__salario)

    def calcularSalario(self):
        return self.__salario * 12