from EmpleadoPorComision import EmpleadoPorComision

class EmpleadoBaseMasComision(EmpleadoPorComision):
    def __init__(self, nombre, apellido, nss, ventas, tarifa, salario):
        super().__init__(nombre, apellido, nss, ventas, tarifa)
        self._salarioBase = 0.0
        self.establecerSalarioBase(salario)

    def establecerSalarioBase(self, salario):
        self._salarioBase = 0.0 if (salario < 0.0) else salario

    def obtenerSalarioBase(self):
        return self._salarioBase

    def Ingresos(self):
        return self.obtenerSalarioBase() + super().Ingresos()

    def __str__(self):
        return f"con salario base {super().__str__()}\nsalario base: ${self.obtenerSalarioBase():,.2f}"
