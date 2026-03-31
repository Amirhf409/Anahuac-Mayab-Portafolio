#include <iostream>
#include <iomanip>
#include <vector>
#include <typeinfo>
#include "EmpleadoAsalariado.h"
#include "EmpleadoPorHoras.h"
#include "EmpleadoPorComision.h"
#include "EmpleadoBaseMasComision.h"
#include "TrabajadorPiezas.h"

using namespace std;

string obtenerNombreClaseAmigable(const string& typeidName) {
    if (typeidName.find("EmpleadoAsalariado") != string::npos) return "EmpleadoAsalariado";
    if (typeidName.find("EmpleadoPorHoras") != string::npos) return "EmpleadoPorHoras";
    if (typeidName.find("EmpleadoBaseMasComision") != string::npos) return "EmpleadoBaseMasComision";
    if (typeidName.find("EmpleadoPorComision") != string::npos) return "EmpleadoPorComision";
    if (typeidName.find("TrabajadorPiezas") != string::npos) return "TrabajadorPiezas";
    return typeidName;
}

int main() {
    EmpleadoAsalariado empleadoAsalariado("John", "Smith", "111-11-1111", 800.00);
    EmpleadoPorHoras empleadoPorHoras("Karen", "Price", "222-22-2222", 16.75, 40);
    EmpleadoPorComision empleadoPorComision("Sue", "Jones", "333-33-3333", 10000, .06);
    EmpleadoBaseMasComision empleadoBaseMasComision("Bob", "Lewis", "444-44-4444", 5000, .04, 300);
    TrabajadorPiezas trabajadorPiezas("Luis", "Gomez", "555-55-5555", 5.0, 200);

    cout << "Empleados procesados por separado:\n\n";

    cout << fixed << setprecision(2);

    cout << empleadoAsalariado.toString() << "\ningresos: $" << empleadoAsalariado.ingresos() << "\n\n";
    cout << empleadoPorHoras.toString() << "\ningresos: $" << empleadoPorHoras.ingresos() << "\n\n";
    cout << empleadoPorComision.toString() << "\ningresos: $" << empleadoPorComision.ingresos() << "\n\n";
    cout << empleadoBaseMasComision.toString() << "\ningresos: $" << empleadoBaseMasComision.ingresos() << "\n\n";
    cout << trabajadorPiezas.toString() << "\ningresos: $" << trabajadorPiezas.ingresos() << "\n\n";

    vector<Empleado*> empleados(5);
    empleados[0] = &empleadoAsalariado;
    empleados[1] = &empleadoPorHoras;
    empleados[2] = &empleadoPorComision;
    empleados[3] = &empleadoBaseMasComision;
    empleados[4] = &trabajadorPiezas;

    cout << "Empleados procesados en forma polimorfica:\n\n";

    for (Empleado* empleadoActual : empleados) {
        cout << empleadoActual->toString() << endl;

        EmpleadoBaseMasComision* empBaseComision = dynamic_cast<EmpleadoBaseMasComision*>(empleadoActual);
        
        if (empBaseComision != nullptr) {
            double salarioBaseAnterior = empBaseComision->obtenerSalarioBase();
            empBaseComision->establecerSalarioBase(1.10 * salarioBaseAnterior);
            cout << "Nuevo salario base con 10% de aumento: $" << empBaseComision->obtenerSalarioBase() << endl;
        }

        cout << "ingresos: $" << empleadoActual->ingresos() << "\n\n";
    }

    for (size_t j = 0; j < empleados.size(); j++) {
        cout << "El empleado " << j << " es un " << obtenerNombreClaseAmigable(typeid(*empleados[j]).name()) << endl;
    }

    return 0;
}
