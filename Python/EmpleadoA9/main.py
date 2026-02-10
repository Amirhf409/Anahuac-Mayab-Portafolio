from claseEmpleado import Empleado

objeto1 = Empleado()
objeto2 = Empleado("Donald Trump", 2025, 400000.99)
objeto3 = Empleado()

print(objeto1.toString())
print("Salario anual:",objeto1.calcularSalario())

print()

print(objeto2.toString())
print("Salario anual:",objeto2.calcularSalario())

print()

nombre = input("Ingrese el nombre del empleado: ")
anio = int(input("Ingreses el año de contratación: "))
salario = float(input("Ingrese el salario mensual: "))

print()

objeto3.nombre = nombre
objeto3.anioContratacion = anio
objeto3.salario = salario

print(objeto3.toString())
print("Salario anual:",objeto3.calcularSalario())
