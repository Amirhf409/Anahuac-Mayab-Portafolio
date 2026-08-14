from Empleado import Empleado

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, apellido, nss, sueldoPorHoras, horasTrabajadas):
        super().__init__(nombre, apellido, nss)
        self._sueldo = 0.0
        self._horas = 0.0
        self.establecerSueldo(sueldoPorHoras)
        self.establecerHoras(horasTrabajadas)

    def establecerSueldo(self, sueldoPorHoras):
        self._sueldo = 0.0 if (sueldoPorHoras < 0.0) else sueldoPorHoras

    def obtenerSueldo(self):
        return self._sueldo

    def establecerHoras(self, horasTrabajadas):
        self._horas = horasTrabajadas if (horasTrabajadas >= 0.0 and horasTrabajadas <= 168.0) else 0.0

    def obtenerHoras(self):
        return self._horas

    def Ingresos(self):
        if self.obtenerHoras() <= 40:
            return self.obtenerSueldo() * self.obtenerHoras()
        else:
            return 40 * self.obtenerSueldo() + (self.obtenerHoras() - 40) * self.obtenerSueldo() * 1.5

    def __str__(self):
        return f"empleado por horas: {super().__str__()}\nsueldo por hora: ${self.obtenerSueldo():,.2f}; horas trabajadas: {self.obtenerHoras():.2f}"
