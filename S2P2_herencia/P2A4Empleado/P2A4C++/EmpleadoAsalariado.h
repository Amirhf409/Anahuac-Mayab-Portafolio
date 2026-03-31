#ifndef EMPLEADOASALARIADO_H
#define EMPLEADOASALARIADO_H

#include "Empleado.h"

class EmpleadoAsalariado : public Empleado {
private:
    double salarioSemanal;

public:
    EmpleadoAsalariado(const std::string& nombre, const std::string& apellido, 
                       const std::string& nss, double salario);

    void establecerSalarioSemanal(double salario);
    double obtenerSalarioSemanal() const;

    virtual double ingresos() const override;
    virtual std::string toString() const override;
};

#endif // EMPLEADOASALARIADO_H
