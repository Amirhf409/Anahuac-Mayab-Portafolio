#include <iostream>
#include <ctime>
#include "Termometro.h"

using namespace std;

int main() {

    srand(time(0)); // Inicializar random

    Termometro t1;
    cout << "Termómetro 1 (aleatorio):" << endl;
    t1.mostrarTemperaturas();

    float tempUsuario;
    cout << "\nIngrese una temperatura en Celsius: ";
    cin >> tempUsuario;

    Termometro t2(tempUsuario);
    cout << "\nTermómetro 2 (Usuario):" << endl;
    t2.mostrarTemperaturas();

    return 0;
}