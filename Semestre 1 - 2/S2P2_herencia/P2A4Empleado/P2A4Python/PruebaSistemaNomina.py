from EmpleadoAsalariado import EmpleadoAsalariado
from EmpleadoPorHoras import EmpleadoPorHoras
from EmpleadoPorComision import EmpleadoPorComision
from EmpleadoBaseMasComision import EmpleadoBaseMasComision
from TrabajadorPiezas import TrabajadorPiezas

def main():
    empleadoAsalariado = EmpleadoAsalariado("John", "Smith", "111-11-1111", 800.00)
    empleadoPorHoras = EmpleadoPorHoras("Karen", "Price", "222-22-2222", 16.75, 40)
    empleadoPorComision = EmpleadoPorComision("Sue", "Jones", "333-33-3333", 10000, .06)
    empleadoBaseMasComision = EmpleadoBaseMasComision("Bob", "Lewis", "444-44-4444", 5000, .04, 300)
    trabajadorPiezas = TrabajadorPiezas("Luis", "Gomez", "555-55-5555", 5.0, 200)

    print("Empleados procesados por separado:\n")

    print(f"{empleadoAsalariado}\ningresos: ${empleadoAsalariado.Ingresos():,.2f}\n")
    print(f"{empleadoPorHoras}\ningresos: ${empleadoPorHoras.Ingresos():,.2f}\n")
    print(f"{empleadoPorComision}\ningresos: ${empleadoPorComision.Ingresos():,.2f}\n")
    print(f"{empleadoBaseMasComision}\ningresos: ${empleadoBaseMasComision.Ingresos():,.2f}\n")
    print(f"{trabajadorPiezas}\ningresos: ${trabajadorPiezas.Ingresos():,.2f}\n")

    # arreglo con TODOS los empleados
    empleados = [
        empleadoAsalariado,
        empleadoPorHoras,
        empleadoPorComision,
        empleadoBaseMasComision,
        trabajadorPiezas
    ]

    print("Empleados procesados en forma polimorfica:\n")

    for empleadoActual in empleados:
        print(empleadoActual)

        # aumento solo para base + comisión
        if isinstance(empleadoActual, EmpleadoBaseMasComision):
            salarioBaseAnterior = empleadoActual.obtenerSalarioBase()
            empleadoActual.establecerSalarioBase(1.10 * salarioBaseAnterior)
            print(f"Nuevo salario base con 10% de aumento: ${empleadoActual.obtenerSalarioBase():,.2f}")

        print(f"ingresos: ${empleadoActual.Ingresos():,.2f}\n")

    # mostrar tipo de cada objeto
    for j, empleado in enumerate(empleados):
        print(f"El empleado {j} es un {empleado.__class__.__name__}")


if __name__ == "__main__":
    main()
