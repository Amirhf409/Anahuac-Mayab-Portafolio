//(Contiene la implementación: cómo funcionan los métodos).
#include "Cuenta.h"
#include <string>
using namespace std;

Cuenta::Cuenta(string nombre, double saldo){
    this->nombre = nombre;

    if (saldo > 0.0){
        this->saldo = saldo;
    } else {
        this->saldo = 0.0;
    }
}

void Cuenta:deposito(double montoDeposito){
    if (montoDeposito > 0.0){
        this->saldo += montoDeposito;
    }
}

double Cuenta::getSaldo(){
    return saldo;
}

void Cuenta::setNombre(string nombre){
    this->nombre = nombre;
}

string Cuenta::getNombre(){
    return nombre;
}
