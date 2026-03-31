#include "EmpleadoAsalariado.h"

EmpleadoAsalariado::EmpleadoAsalariado(string nombre, string apellido,
                                       string nss, double salario)
    : Empleado(nombre, apellido, nss) {
  salarioSemanal = salario < 0.0 ? 0.0 : salario;
}

double EmpleadoAsalariado::ingresos() const { return salarioSemanal; }

string EmpleadoAsalariado::toString() const {
  return "empleado asalariado: " + Empleado::toString() +
         "\nsalario semanal: " + to_string(salarioSemanal);
}