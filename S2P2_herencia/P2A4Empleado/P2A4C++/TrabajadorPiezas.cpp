#include "TrabajadorPiezas.h"
#include <sstream>
#include <iomanip>

TrabajadorPiezas::TrabajadorPiezas(const std::string& nombre, const std::string& apellido, 
                                   const std::string& nss, double salarioPorPieza, int piezas)
    : Empleado(nombre, apellido, nss) {
    establecerSalarioPorPieza(salarioPorPieza);
    establecerPiezas(piezas);
}

void TrabajadorPiezas::establecerSalarioPorPieza(double salario) {
    salarioPorPieza = (salario < 0.0) ? 0.0 : salario;
}

double TrabajadorPiezas::obtenerSalarioPorPieza() const {
    return salarioPorPieza;
}

void TrabajadorPiezas::establecerPiezas(int piezasProducidas) {
    piezas = (piezasProducidas < 0) ? 0 : piezasProducidas;
}

int TrabajadorPiezas::obtenerPiezas() const {
    return piezas;
}

double TrabajadorPiezas::ingresos() const {
    return obtenerSalarioPorPieza() * obtenerPiezas();
}

std::string TrabajadorPiezas::toString() const {
    std::ostringstream output;
    output << std::fixed << std::setprecision(2);
    output << "trabajador por piezas: " << Empleado::toString()
           << "\nsalario por pieza: $" << obtenerSalarioPorPieza()
           << "; piezas producidas: " << obtenerPiezas();
    return output.str();
}
