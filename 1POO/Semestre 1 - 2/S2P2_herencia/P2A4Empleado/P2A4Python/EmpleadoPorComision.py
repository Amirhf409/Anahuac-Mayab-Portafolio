from Empleado import Empleado

class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, apellido, nss, ventas, tarifa):
        super().__init__(nombre, apellido, nss)
        self._ventasBrutas = 0.0
        self._tarifaComision = 0.0
        self.establecerVentasBrutas(ventas)
        self.establecerTarifaComision(tarifa)

    def establecerTarifaComision(self, tarifa):
        self._tarifaComision = tarifa if (tarifa > 0.0 and tarifa < 1.0) else 0.0

    def obtenerTarifaComision(self):
        return self._tarifaComision

    def establecerVentasBrutas(self, ventas):
        self._ventasBrutas = 0.0 if (ventas < 0.0) else ventas

    def obtenerVentasBrutas(self):
        return self._ventasBrutas

    def Ingresos(self):
        return self.obtenerTarifaComision() * self.obtenerVentasBrutas()

    def __str__(self):
        return f"empleado por comision: {super().__str__()}\nventas brutas: ${self.obtenerVentasBrutas():,.2f}; tarifa de comision: {self.obtenerTarifaComision():.2f}"
