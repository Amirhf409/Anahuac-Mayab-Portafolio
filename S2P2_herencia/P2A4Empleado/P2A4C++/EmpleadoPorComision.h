#ifndef EMPLEADOPORCOMISION_H
#define EMPLEADOPORCOMISION_H

#include "Empleado.h"

class EmpleadoPorComision : public Empleado {
private:
    double ventasBrutas;
    double tarifaComision;

public:
    EmpleadoPorComision(const std::string& nombre, const std::string& apellido, 
                        const std::string& nss, double ventas, double tarifa);

    void establecerTarifaComision(double tarifa);
    double obtenerTarifaComision() const;

    void establecerVentasBrutas(double ventas);
    double obtenerVentasBrutas() const;

    virtual double ingresos() const override;
    virtual std::string toString() const override;
};

#endif // EMPLEADOPORCOMISION_H
