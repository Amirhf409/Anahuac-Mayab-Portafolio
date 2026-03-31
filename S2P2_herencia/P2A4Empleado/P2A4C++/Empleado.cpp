#include "Empleado.h"
#include <sstream>

Empleado::Empleado(const std::string& nombre, const std::string& apellido, const std::string& nss)
    : primerNombre(nombre), apellidoPaterno(apellido), numeroSeguroSocial(nss) {}

void Empleado::establecerPrimerNombre(const std::string& nombre) {
    primerNombre = nombre;
}

std::string Empleado::obtenerPrimerNombre() const {
    return primerNombre;
}

void Empleado::establecerApellidoPaterno(const std::string& apellido) {
    apellidoPaterno = apellido;
}

std::string Empleado::obtenerApellidoPaterno() const {
    return apellidoPaterno;
}

void Empleado::establecerNumeroSeguroSocial(const std::string& nss) {
    numeroSeguroSocial = nss;
}

std::string Empleado::obtenerNumeroSeguroSocial() const {
    return numeroSeguroSocial;
}

std::string Empleado::toString() const {
    std::ostringstream output;
    output << obtenerPrimerNombre() << " " << obtenerApellidoPaterno()
           << "\nnumero de seguro social: " << obtenerNumeroSeguroSocial();
    return output.str();
}
