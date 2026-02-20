#ifndef TERMOMETRO_H
#define TERMOMETRO_H

class Termometro {
private:
    float temperatura;

public:
    Termometro();               // Constructor por defecto
    Termometro(float temp);     // Constructor parametrizado

    float temperaturaC();
    float temperaturaF();
    float temperaturaK();

    void mostrarTemperaturas();
};

#endif