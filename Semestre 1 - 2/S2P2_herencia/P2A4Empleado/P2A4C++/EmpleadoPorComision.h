#ifndef EMPLEADOPORCOMISION_H
#define EMPLEADOPORCOMISION_H

#include "Empleado.h"

class EmpleadoPorComision : public Empleado {
private:
  double ventasBrutas;
  double tarifaComision;

public:
  EmpleadoPorComision(string nombre, string apellido, string nss, double ventas,
                      double tarifa);

  double ingresos() const override;

  string toString() const override;
};

#endif