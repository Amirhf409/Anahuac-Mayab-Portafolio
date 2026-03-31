#include "EmpleadoPorHoras.h"
#include <sstream>
#include <iomanip>

EmpleadoPorHoras::EmpleadoPorHoras(const std::string& nombre, const std::string& apellido, 
                                   const std::string& nss, double sueldoPorHoras, double horasTrabajadas)
    : Empleado(nombre, apellido, nss) {
    establecerSueldo(sueldoPorHoras);
    establecerHoras(horasTrabajadas);
}

void EmpleadoPorHoras::establecerSueldo(double sueldoPorHoras) {
    sueldo = (sueldoPorHoras < 0.0) ? 0.0 : sueldoPorHoras;
}

double EmpleadoPorHoras::obtenerSueldo() const {
    return sueldo;
}

void EmpleadoPorHoras::establecerHoras(double horasTrabajadas) {
    horas = (horasTrabajadas >= 0.0 && horasTrabajadas <= 168.0) ? horasTrabajadas : 0.0;
}

double EmpleadoPorHoras::obtenerHoras() const {
    return horas;
}

double EmpleadoPorHoras::ingresos() const {
    if (obtenerHoras() <= 40)
        return obtenerSueldo() * obtenerHoras();
    else
        return 40 * obtenerSueldo() + (obtenerHoras() - 40) * obtenerSueldo() * 1.5;
}

std::string EmpleadoPorHoras::toString() const {
    std::ostringstream output;
    output << std::fixed << std::setprecision(2);
    output << "empleado por horas: " << Empleado::toString()
           << "\nsueldo por hora: $" << obtenerSueldo()
           << "; horas trabajadas: " << obtenerHoras();
    return output.str();
}
