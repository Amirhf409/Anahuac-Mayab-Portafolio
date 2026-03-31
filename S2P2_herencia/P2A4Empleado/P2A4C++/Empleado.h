#ifndef EMPLEADO_H
#define EMPLEADO_H

#include <string>
using namespace std;

class Empleado {
protected:
  string primerNombre;
  string apellidoPaterno;
  string numeroSeguroSocial;

public:
  Empleado(string nombre, string apellido, string nss);

  virtual double ingresos() const = 0;

  virtual string toString() const;

  virtual ~Empleado() {}
};

#endif