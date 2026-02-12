//(Contiene la declaración: qué tiene la clase).
#pragma once
#include <string>

class Cuenta {
public:
    string nombre;
    double saldo;

    Cuenta(string nombre, double saldo);
    void deposito(double, montoDeposito);
    double getSaldo();
    void setNombre(string nombre);
    string getNombre();

};