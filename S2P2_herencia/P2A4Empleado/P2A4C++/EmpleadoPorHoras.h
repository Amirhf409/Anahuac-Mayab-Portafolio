#ifndef EMPLEADOPORHORAS_H
#define EMPLEADOPORHORAS_H

#include "Empleado.h"

class EmpleadoPorHoras : public Empleado {
private:
    double sueldo;
    double horas;

public:
    EmpleadoPorHoras(const std::string& nombre, const std::string& apellido, 
                     const std::string& nss, double sueldoPorHoras, double horasTrabajadas);

    void establecerSueldo(double sueldoPorHoras);
    double obtenerSueldo() const;

    void establecerHoras(double horasTrabajadas);
    double obtenerHoras() const;

    virtual double ingresos() const override;
    virtual std::string toString() const override;
};

#endif // EMPLEADOPORHORAS_H
