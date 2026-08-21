using System;

public class PruebaSistemaNomina
{
   public static void Main(string[] args)
   {
      // crear objetos de cada tipo de empleado
      EmpleadoAsalariado empleadoAsalariado = new EmpleadoAsalariado("John", "Smith", "111-11-1111", 800.00);

      EmpleadoPorHoras empleadoPorHoras = new EmpleadoPorHoras("Karen", "Price", "222-22-2222", 16.75, 40);

      EmpleadoPorComision empleadoPorComision = new EmpleadoPorComision("Sue", "Jones", "333-33-3333", 10000, .06);

      EmpleadoBaseMasComision empleadoBaseMasComision = new EmpleadoBaseMasComision("Bob", "Lewis", "444-44-4444", 5000,
            .04, 300);

      // NUEVO empleado
      TrabajadorPiezas trabajadorPiezas = new TrabajadorPiezas("Luis", "Gomez", "555-55-5555", 5.0, 200);

      Console.WriteLine("Empleados procesados por separado:\n");

      Console.WriteLine($"{empleadoAsalariado}\ningresos: {empleadoAsalariado.Ingresos():C2}\n");
      Console.WriteLine($"{empleadoPorHoras}\ningresos: {empleadoPorHoras.Ingresos():C2}\n");
      Console.WriteLine($"{empleadoPorComision}\ningresos: {empleadoPorComision.Ingresos():C2}\n");
      Console.WriteLine($"{empleadoBaseMasComision}\ningresos: {empleadoBaseMasComision.Ingresos():C2}\n");
      Console.WriteLine($"{trabajadorPiezas}\ningresos: {trabajadorPiezas.Ingresos():C2}\n");

      // arreglo con TODOS los empleados
      Empleado[] empleados = new Empleado[5];

      empleados[0] = empleadoAsalariado;
      empleados[1] = empleadoPorHoras;
      empleados[2] = empleadoPorComision;
      empleados[3] = empleadoBaseMasComision;
      empleados[4] = trabajadorPiezas;

      Console.WriteLine("Empleados procesados en forma polimorfica:\n");

      foreach (Empleado empleadoActual in empleados)
      {
         Console.WriteLine(empleadoActual);

         // aumento solo para base + comisión
         if (empleadoActual is EmpleadoBaseMasComision)
         {
            EmpleadoBaseMasComision empleado = (EmpleadoBaseMasComision)empleadoActual;

            double salarioBaseAnterior = empleado.obtenerSalarioBase();
            empleado.establecerSalarioBase(1.10 * salarioBaseAnterior);

            Console.WriteLine($"Nuevo salario base con 10% de aumento: {empleado.obtenerSalarioBase():C2}");
         }

         Console.WriteLine($"ingresos: {empleadoActual.Ingresos():C2}\n");
      }

      // mostrar tipo de cada objeto
      for (int j = 0; j < empleados.Length; j++)
      {
         Console.WriteLine($"El empleado {j} es un {empleados[j].GetType().Name}");
      }
   }
}