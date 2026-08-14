#include "EmpleadoPorHoras.h"

EmpleadoPorHoras::EmpleadoPorHoras(string nombre, string apellido, string nss,
                                   double sueldoPorHoras,
                                   double horasTrabajadas)
    : Empleado(nombre, apellido, nss) {
  sueldo = sueldoPorHoras < 0.0 ? 0.0 : sueldoPorHoras;
  horas = (horasTrabajadas >= 0.0 && horasTrabajadas <= 168.0) ? horasTrabajadas
                                                               : 0.0;
}

double EmpleadoPorHoras::ingresos() const {
  if (horas <= 40)
    return sueldo * horas;
  else
    return 40 * sueldo + (horas - 40) * sueldo * 1.5;
}

string EmpleadoPorHoras::toString() const {
  return "empleado por horas: " + Empleado::toString() +
         "\nsueldo: " + to_string(sueldo) + "\nhoras: " + to_string(horas);
}