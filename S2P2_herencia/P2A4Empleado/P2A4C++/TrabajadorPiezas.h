#ifndef TRABAJADORPIEZAS_H
#define TRABAJADORPIEZAS_H

#include "Empleado.h"

class TrabajadorPiezas : public Empleado {
private:
    double salarioPorPieza;
    int piezas;

public:
    TrabajadorPiezas(const std::string& nombre, const std::string& apellido, 
                     const std::string& nss, double salarioPorPieza, int piezas);

    void establecerSalarioPorPieza(double salario);
    double obtenerSalarioPorPieza() const;

    void establecerPiezas(int piezasProducidas);
    int obtenerPiezas() const;

    virtual double ingresos() const override;
    virtual std::string toString() const override;
};

#endif // TRABAJADORPIEZAS_H
