from Empleado import Empleado

class TrabajadorPiezas(Empleado):
    def __init__(self, nombre, apellido, nss, salarioPorPieza, piezas):
        super().__init__(nombre, apellido, nss)
        self._salarioPorPieza = 0.0
        self._piezas = 0
        self.establecerSalarioPorPieza(salarioPorPieza)
        self.establecerPiezas(piezas)

    def establecerSalarioPorPieza(self, salario):
        self._salarioPorPieza = 0.0 if (salario < 0.0) else salario

    def obtenerSalarioPorPieza(self):
        return self._salarioPorPieza

    def establecerPiezas(self, piezasProducidas):
        self._piezas = 0 if (piezasProducidas < 0) else piezasProducidas

    def obtenerPiezas(self):
        return self._piezas

    def Ingresos(self):
        return self.obtenerSalarioPorPieza() * self.obtenerPiezas()

    def __str__(self):
        return f"trabajador por piezas: {super().__str__()}\nsalario por pieza: ${self.obtenerSalarioPorPieza():,.2f}; piezas producidas: {self.obtenerPiezas()}"
