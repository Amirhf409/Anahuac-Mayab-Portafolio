#pragma once
#include <string>

using namespace std;

class Cuenta {
private:
    string nombre; // Ahora son privados
    double saldo;

public:
    Cuenta(string nombre, double saldo);
    void deposito(double montoDeposito);
    double getSaldo();
    void setNombre(string nombre);
    string getNombre();
};