#ifndef EMPLEADOPORHORAS_H
#define EMPLEADOPORHORAS_H

#include "Empleado.h"

class EmpleadoPorHoras : public Empleado {
private:
  double sueldo;
  double horas;

public:
  EmpleadoPorHoras(string nombre, string apellido, string nss, double sueldo,
                   double horas);

  double ingresos() const override;

  string toString() const override;
};

#endif