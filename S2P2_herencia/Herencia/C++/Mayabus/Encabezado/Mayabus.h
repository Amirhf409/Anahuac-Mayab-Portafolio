#pragma once
#include <string>
using namespace std;

class Usuario {
private:
  string nombre;
  string id;
  int tickets;

public:
  Usuario(string nombre, string id);

  string getNombre();
  void setNombre(string nombre);

  string getId();
  void setId(string id);

  int getTickets();
  void setTickets(int cantidad);
};

class Alumno : public Usuario {
private:
  double costo;

public:
  Alumno(string nombre, string id, double costo);

  void calcularCuota();
  void calcularCuota(int cantidad);

  void setCosto(double costo);
  double getCosto();

  void viajar();
};

class Maestro : public Usuario {
public:
  Maestro(string nombre, string id);
  void viajar();
};

class Administrativo : public Usuario {
public:
  Administrativo(string nombre, string id);
  void viajar();
};