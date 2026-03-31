#include "EmpleadoAsalariado.h"
#include <sstream>
#include <iomanip>

EmpleadoAsalariado::EmpleadoAsalariado(const std::string& nombre, const std::string& apellido, 
                                       const std::string& nss, double salario)
    : Empleado(nombre, apellido, nss) {
    establecerSalarioSemanal(salario);
}

void EmpleadoAsalariado::establecerSalarioSemanal(double salario) {
    salarioSemanal = (salario < 0.0) ? 0.0 : salario;
}

double EmpleadoAsalariado::obtenerSalarioSemanal() const {
    return salarioSemanal;
}

double EmpleadoAsalariado::ingresos() const {
    return obtenerSalarioSemanal();
}

std::string EmpleadoAsalariado::toString() const {
    std::ostringstream output;
    output << std::fixed << std::setprecision(2);
    output << "empleado asalariado: " << Empleado::toString()
           << "\nsalario semanal: $" << obtenerSalarioSemanal();
    return output.str();
}
