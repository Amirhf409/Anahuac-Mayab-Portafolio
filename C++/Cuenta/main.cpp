#include <iostream>
#include <string>
#include "Cuenta.h"

using namespace std;

int main() {
    // Crear objetos iniciales
    Cuenta cuenta1("Jane Green", 50.00);
    Cuenta cuenta2("John Blue", -7.53);

    // Mostrar saldos iniciales
    cout << "Saldo de " << cuenta1.getNombre() << ": $" << cuenta1.getSaldo() << endl;
    cout << "Saldo de " << cuenta2.getNombre() << ": $" << cuenta2.getSaldo() << endl << endl;

    double montoDeposito;

    // Interacción con cuenta1
    cout << "Ingrese el monto del deposito para la cuenta1: ";
    cin >> montoDeposito;
    cout << "\nagregando " << montoDeposito << " al saldo de la cuenta1" << endl << endl;
    cuenta1.deposito(montoDeposito);

    // Mostrar saldos tras primer deposito
    cout << "Saldo de " << cuenta1.getNombre() << ": $" << cuenta1.getSaldo() << endl;
    cout << "Saldo de " << cuenta2.getNombre() << ": $" << cuenta2.getSaldo() << endl << endl;

    // Interacción con cuenta2
    cout << "Ingrese el monto del deposito para la cuenta2: ";
    cin >> montoDeposito;
    cout << "\nagregando " << montoDeposito << " al saldo de la cuenta2" << endl << endl;
    cuenta2.deposito(montoDeposito);

    // Mostrar saldos finales
    cout << cuenta1.getNombre() << " saldo: $" << cuenta1.getSaldo() << endl;
    cout << cuenta2.getNombre() << " saldo: $" << cuenta2.getSaldo() << endl;

    return 0;
}