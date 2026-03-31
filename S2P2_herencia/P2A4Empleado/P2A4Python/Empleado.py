from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, apellido, nss):
        self._primerNombre = nombre
        self._apellidoPaterno = apellido
        self._numeroSeguroSocial = nss

    def establecerPrimerNombre(self, nombre):
        self._primerNombre = nombre

    def obtenerPrimerNombre(self):
        return self._primerNombre

    def establecerApellidoPaterno(self, apellido):
        self._apellidoPaterno = apellido

    def obtenerApellidoPaterno(self):
        return self._apellidoPaterno

    def establecerNumeroSeguroSocial(self, nss):
        self._numeroSeguroSocial = nss

    def obtenerNumeroSeguroSocial(self):
        return self._numeroSeguroSocial

    def __str__(self):
        return f"{self.obtenerPrimerNombre()} {self.obtenerApellidoPaterno()}\nnumero de seguro social: {self.obtenerNumeroSeguroSocial()}"

    @abstractmethod
    def Ingresos(self):
        pass
