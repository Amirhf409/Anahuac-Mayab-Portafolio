#include "EmpleadoBaseMasComision.h"
#include <sstream>
#include <iomanip>

EmpleadoBaseMasComision::EmpleadoBaseMasComision(const std::string& nombre, const std::string& apellido, 
                                                 const std::string& nss, double ventas, double tarifa, double salario)
    : EmpleadoPorComision(nombre, apellido, nss, ventas, tarifa) {
    establecerSalarioBase(salario);
}

void EmpleadoBaseMasComision::establecerSalarioBase(double salario) {
    salarioBase = (salario < 0.0) ? 0.0 : salario;
}

double EmpleadoBaseMasComision::obtenerSalarioBase() const {
    return salarioBase;
}

double EmpleadoBaseMasComision::ingresos() const {
    return obtenerSalarioBase() + EmpleadoPorComision::ingresos();
}

std::string EmpleadoBaseMasComision::toString() const {
    std::ostringstream output;
    output << std::fixed << std::setprecision(2);
    output << "con salario base " << EmpleadoPorComision::toString()
           << "\nsalario base: $" << obtenerSalarioBase();
    return output.str();
}
