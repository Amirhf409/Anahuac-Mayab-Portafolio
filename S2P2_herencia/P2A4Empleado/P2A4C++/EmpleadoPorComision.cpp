#include "EmpleadoPorComision.h"
#include <sstream>
#include <iomanip>

EmpleadoPorComision::EmpleadoPorComision(const std::string& nombre, const std::string& apellido, 
                                         const std::string& nss, double ventas, double tarifa)
    : Empleado(nombre, apellido, nss) {
    establecerVentasBrutas(ventas);
    establecerTarifaComision(tarifa);
}

void EmpleadoPorComision::establecerTarifaComision(double tarifa) {
    tarifaComision = (tarifa > 0.0 && tarifa < 1.0) ? tarifa : 0.0;
}

double EmpleadoPorComision::obtenerTarifaComision() const {
    return tarifaComision;
}

void EmpleadoPorComision::establecerVentasBrutas(double ventas) {
    ventasBrutas = (ventas < 0.0) ? 0.0 : ventas;
}

double EmpleadoPorComision::obtenerVentasBrutas() const {
    return ventasBrutas;
}

double EmpleadoPorComision::ingresos() const {
    return obtenerTarifaComision() * obtenerVentasBrutas();
}

std::string EmpleadoPorComision::toString() const {
    std::ostringstream output;
    output << std::fixed << std::setprecision(2);
    output << "empleado por comision: " << Empleado::toString()
           << "\nventas brutas: $" << obtenerVentasBrutas()
           << "; tarifa de comision: " << obtenerTarifaComision();
    return output.str();
}
