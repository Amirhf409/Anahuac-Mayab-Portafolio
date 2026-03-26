#include "../Encabezado/Animales.h"
#include <iostream>

Mamifero::Mamifero(string n, double p) {
  this->nombre = n;
  this->peso = p;
}

void Mamifero::setNombre(string n) { this->nombre = n; }

string Mamifero::getNombre() { return this->nombre; }

string Mamifero::toString() {
  return "Mamifero\n [" + nombre + "," + to_string(peso) + " kg]";
}

// Clase Gato
Gato::Gato(string n, double p, int b) : Mamifero(n, p) { this->nBigotes = b; }

string Gato::toString() {
  return "GATO " + Mamifero::toString() + "[Bigotes:" + to_string(nBigotes) +
         "]";
}

// Clase Vaca
Vaca::Vaca(string n, double p, double l) : Mamifero(n, p) {
  this->litrosLeche = l;
}

void Vaca::calcularCantidadComida() {
  cout << this->peso * 0.03 << " kg de alimento";
}

string Vaca::toString() {
  return "VACA " + Mamifero::toString() +
         "[Litros de leche:" + to_string(litrosLeche) + "]";
}

// Clase Ballena

Ballena::Ballena(string n, double p) : Mamifero(n, p) {}

string Ballena::toString() { return "BALLENA " + Mamifero::toString(); }