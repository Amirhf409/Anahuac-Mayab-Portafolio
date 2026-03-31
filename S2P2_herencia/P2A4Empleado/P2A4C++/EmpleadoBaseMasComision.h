#ifndef EMPLEADOBASEMASCOMISION_H
#define EMPLEADOBASEMASCOMISION_H

#include "EmpleadoPorComision.h"

class EmpleadoBaseMasComision : public EmpleadoPorComision {
private:
    double salarioBase;

public:
    EmpleadoBaseMasComision(const std::string& nombre, const std::string& apellido, 
                            const std::string& nss, double ventas, double tarifa, double salario);

    void establecerSalarioBase(double salario);
    double obtenerSalarioBase() const;

    virtual double ingresos() const override;
    virtual std::string toString() const override;
};

#endif // EMPLEADOBASEMASCOMISION_H
