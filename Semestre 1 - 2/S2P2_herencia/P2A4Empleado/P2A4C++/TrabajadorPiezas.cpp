#include "TrabajadorPiezas.h"

TrabajadorPiezas::TrabajadorPiezas(string nombre, string apellido, string nss,
                                   double salario, int piezasProducidas)
    : Empleado(nombre, apellido, nss) {
  salarioPorPieza = salario < 0.0 ? 0.0 : salario;
  piezas = piezasProducidas < 0 ? 0 : piezasProducidas;
}

double TrabajadorPiezas::ingresos() const { return salarioPorPieza * piezas; }

string TrabajadorPiezas::toString() const {
  return "trabajador por piezas: " + Empleado::toString() +
         "\nsalario por pieza: " + to_string(salarioPorPieza) +
         "\npiezas: " + to_string(piezas);
}