#ifndef EMPLEADO_H
#define EMPLEADO_H

#include <string>

class Empleado {
private:
    std::string primerNombre;
    std::string apellidoPaterno;
    std::string numeroSeguroSocial;

public:
    Empleado(const std::string& nombre, const std::string& apellido, const std::string& nss);
    virtual ~Empleado() = default;

    void establecerPrimerNombre(const std::string& nombre);
    std::string obtenerPrimerNombre() const;

    void establecerApellidoPaterno(const std::string& apellido);
    std::string obtenerApellidoPaterno() const;

    void establecerNumeroSeguroSocial(const std::string& nss);
    std::string obtenerNumeroSeguroSocial() const;

    virtual std::string toString() const;
    virtual double ingresos() const = 0; // función virtual pura
};

#endif // EMPLEADO_H
