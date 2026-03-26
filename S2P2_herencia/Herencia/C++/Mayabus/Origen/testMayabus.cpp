#include "../Encabezado/Mayabus.h"
#include <iostream>

using namespace std;

int main() {

  Alumno alumno("Carlos", "A01", 10);
  Maestro maestro("Pedro", "M01");
  Administrativo admin("Luis", "AD01");

  alumno.setTickets(3);

  cout << "Alumno:" << endl;
  alumno.viajar();
  alumno.viajar();

  cout << endl;

  cout << "Maestro:" << endl;
  maestro.viajar();
  maestro.viajar();

  cout << endl;

  cout << "Administrativo:" << endl;
  admin.viajar();

  cout << endl;

  alumno.calcularCuota();
  alumno.calcularCuota(5);

  return 0;
}