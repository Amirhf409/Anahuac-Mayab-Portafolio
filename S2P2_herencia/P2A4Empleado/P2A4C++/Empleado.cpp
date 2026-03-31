#include "Empleado.h"

Empleado::Empleado(string nombre, string apellido, string nss) {
  primerNombre = nombre;
  apellidoPaterno = apellido;
  numeroSeguroSocial = nss;
}

string Empleado::toString() const {
  return primerNombre + " " + apellidoPaterno +
         "\nnumero de seguro social: " + numeroSeguroSocial;
}