#include "../Encabezado/Mayabus.h"
#include <iostream>

using namespace std;

// ---------- Clase Usuario ----------

Usuario::Usuario(string n, string i) {
  this->nombre = n;
  this->id = i;
  this->tickets = 0;
}

string Usuario::getNombre() { return this->nombre; }

void Usuario::setNombre(string n) { this->nombre = n; }

string Usuario::getId() { return this->id; }

void Usuario::setId(string i) { this->id = i; }

int Usuario::getTickets() { return this->tickets; }

void Usuario::setTickets(int cantidad) { this->tickets = cantidad; }

// ---------- Clase Alumno ----------

Alumno::Alumno(string n, string i, double c) : Usuario(n, i) {
  this->costo = c;
}

void Alumno::calcularCuota() {
  cout << "Costo pase semestral: " << this->costo << endl;
}

void Alumno::calcularCuota(int cantidad) {
  cout << "Costo por " << cantidad << " tickets: " << this->costo * cantidad
       << endl;
}

void Alumno::setCosto(double c) { this->costo = c; }

double Alumno::getCosto() { return this->costo; }

void Alumno::viajar() {

  if (this->getTickets() > 0) {
    this->setTickets(this->getTickets() - 1);
    cout << "Alumno viajo. Tickets restantes: " << this->getTickets() << endl;
  } else {
    cout << "Alumno no tiene tickets disponibles" << endl;
  }
}

// ---------- Clase Maestro ----------

Maestro::Maestro(string n, string i) : Usuario(n, i) { this->setTickets(50); }

void Maestro::viajar() {

  if (this->getTickets() == 0) {
    this->setTickets(50);
    cout << "Se renovaron 50 tickets" << endl;
  }

  this->setTickets(this->getTickets() - 1);

  cout << "Maestro viajo. Tickets restantes: " << this->getTickets() << endl;
}

// ---------- Clase Administrativo ----------

Administrativo::Administrativo(string n, string i) : Usuario(n, i) {
  this->setTickets(50);
}

void Administrativo::viajar() {

  if (this->getTickets() == 0) {
    this->setTickets(50);
    cout << "Se renovaron 50 tickets" << endl;
  }

  this->setTickets(this->getTickets() - 1);

  cout << "Administrativo viajo. Tickets restantes: " << this->getTickets()
       << endl;
}