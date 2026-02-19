#include "Termometro.h"
#include <iostream>
#include <cstdlib>

using namespace std;

// Constructor por defecto
Termometro::Termometro() {
    temperatura = static_cast<float>(rand()) / RAND_MAX * 100;
}

// Constructor parametrizado
Termometro::Termometro(float temp) {
    temperatura = temp;
}

float Termometro::temperaturaC() {
    return temperatura;
}

float Termometro::temperaturaF() {
    return (temperatura * 9/5) + 32;
}

float Termometro::temperaturaK() {
    return temperatura + 273.15f;
}

void Termometro::mostrarTemperaturas() {
    cout << "Temperatura en Celsius: " << temperaturaC() << endl;
    cout << "Temperatura en Fahrenheit: " << temperaturaF() << endl;
    cout << "Temperatura en Kelvin: " << temperaturaK() << endl;
}