#ifndef TRABAJADORPIEZAS_H
#define TRABAJADORPIEZAS_H

#include "Empleado.h"

class TrabajadorPiezas : public Empleado {
private:
  double salarioPorPieza;
  int piezas;

public:
  TrabajadorPiezas(string nombre, string apellido, string nss, double salario,
                   int piezas);

  double ingresos() const override;

  string toString() const override;
};

#endif