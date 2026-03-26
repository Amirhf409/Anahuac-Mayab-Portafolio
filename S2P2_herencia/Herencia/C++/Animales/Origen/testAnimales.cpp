#include "../Encabezado/Animales.h"
#include <iostream>

using namespace std;

int main() {
  Gato mitch("Mitch", 6.7, 10);
  Vaca nani("Nani", 350, 20);
  Ballena titi("Titi", 200000);

  cout << mitch.toString() << endl << endl;

  cout << nani.toString() << endl;
  nani.calcularCantidadComida();

  cout << titi.toString() << endl;
}