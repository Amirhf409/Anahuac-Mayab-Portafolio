#include "EmpleadoPorComision.h"

EmpleadoPorComision::EmpleadoPorComision(string nombre, string apellido,
                                         string nss, double ventas,
                                         double tarifa)
    : Empleado(nombre, apellido, nss) {
  ventasBrutas = ventas < 0.0 ? 0.0 : ventas;
  tarifaComision = (tarifa > 0.0 && tarifa < 1.0) ? tarifa : 0.0;
}

double EmpleadoPorComision::ingresos() const {
  return ventasBrutas * tarifaComision;
}

string EmpleadoPorComision::toString() const {
  return "empleado por comision: " + Empleado::toString() +
         "\nventas: " + to_string(ventasBrutas) +
         "\ntarifa: " + to_string(tarifaComision);
}