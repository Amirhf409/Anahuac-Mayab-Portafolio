#ifndef EMPLEADOASALARIADO_H
#define EMPLEADOASALARIADO_H

#include "Empleado.h"

class EmpleadoAsalariado : public Empleado {
private:
  double salarioSemanal;

public:
  EmpleadoAsalariado(string nombre, string apellido, string nss,
                     double salario);

  double ingresos() const override;

  string toString() const override;
};

#endif