#include <iostream>
#include <vector>

#include "EmpleadoAsalariado.h"
#include "EmpleadoPorComision.h"
#include "EmpleadoPorHoras.h"
#include "TrabajadorPiezas.h"


using namespace std;

int main() {

  EmpleadoAsalariado e1("John", "Smith", "111", 800);
  EmpleadoPorHoras e2("Karen", "Price", "222", 16.75, 40);
  EmpleadoPorComision e3("Sue", "Jones", "333", 10000, 0.06);
  TrabajadorPiezas e4("Luis", "Gomez", "444", 5.0, 200);

  vector<Empleado *> empleados = {&e1, &e2, &e3, &e4};

  for (Empleado *e : empleados) {
    cout << e->toString() << endl;
    cout << "ingresos: " << e->ingresos() << endl << endl;
  }

  return 0;
}