#include "Cuenta.h"
#include <string>

using namespace std;

Cuenta::Cuenta(string nombre, double saldo) {
    this->nombre = nombre;
    // Validamos que el saldo inicial sea positivo
    this->saldo = (saldo > 0.0) ? saldo : 0.0;
}

void Cuenta::deposito(double montoDeposito) {
    if (montoDeposito > 0.0) {
        saldo += montoDeposito;
    }
}

double Cuenta::getSaldo() {
    return saldo;
}

void Cuenta::setNombre(string nombre) {
    this->nombre = nombre;
}

string Cuenta::getNombre() {
    return nombre;
}