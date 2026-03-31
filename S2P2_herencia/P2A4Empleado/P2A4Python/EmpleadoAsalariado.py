from Empleado import Empleado

class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, apellido, nss, salario):
        super().__init__(nombre, apellido, nss)
        self._salarioSemanal = 0.0
        self.establecerSalarioSemanal(salario)

    def establecerSalarioSemanal(self, salario):
        self._salarioSemanal = 0.0 if salario < 0.0 else salario

    def obtenerSalarioSemanal(self):
        return self._salarioSemanal

    def Ingresos(self):
        return self.obtenerSalarioSemanal()

    def __str__(self):
        return f"empleado asalariado: {super().__str__()}\nsalario semanal: ${self.obtenerSalarioSemanal():,.2f}"
