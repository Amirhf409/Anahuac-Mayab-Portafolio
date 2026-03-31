public class PruebaSistemaNomina {
   public static void main(String args[]) {
      // crear objetos de cada tipo de empleado
      EmpleadoAsalariado empleadoAsalariado = new EmpleadoAsalariado("John", "Smith", "111-11-1111", 800.00);

      EmpleadoPorHoras empleadoPorHoras = new EmpleadoPorHoras("Karen", "Price", "222-22-2222", 16.75, 40);

      EmpleadoPorComision empleadoPorComision = new EmpleadoPorComision("Sue", "Jones", "333-33-3333", 10000, .06);

      EmpleadoBaseMasComision empleadoBaseMasComision = new EmpleadoBaseMasComision("Bob", "Lewis", "444-44-4444", 5000,
            .04, 300);

      // NUEVO empleado
      TrabajadorPiezas trabajadorPiezas = new TrabajadorPiezas("Luis", "Gomez", "555-55-5555", 5.0, 200);

      System.out.println("Empleados procesados por separado:\n");

      System.out.printf("%s\n%s: $%,.2f\n\n",
            empleadoAsalariado, "ingresos", empleadoAsalariado.ingresos());

      System.out.printf("%s\n%s: $%,.2f\n\n",
            empleadoPorHoras, "ingresos", empleadoPorHoras.ingresos());

      System.out.printf("%s\n%s: $%,.2f\n\n",
            empleadoPorComision, "ingresos", empleadoPorComision.ingresos());

      System.out.printf("%s\n%s: $%,.2f\n\n",
            empleadoBaseMasComision, "ingresos", empleadoBaseMasComision.ingresos());

      System.out.printf("%s\n%s: $%,.2f\n\n",
            trabajadorPiezas, "ingresos", trabajadorPiezas.ingresos());

      // arreglo con TODOS los empleados
      Empleado empleados[] = new Empleado[5];

      empleados[0] = empleadoAsalariado;
      empleados[1] = empleadoPorHoras;
      empleados[2] = empleadoPorComision;
      empleados[3] = empleadoBaseMasComision;
      empleados[4] = trabajadorPiezas;

      System.out.println("Empleados procesados en forma polimorfica:\n");

      for (Empleado empleadoActual : empleados) {
         System.out.println(empleadoActual);

         // aumento solo para base + comisión
         if (empleadoActual instanceof EmpleadoBaseMasComision) {
            EmpleadoBaseMasComision empleado = (EmpleadoBaseMasComision) empleadoActual;

            double salarioBaseAnterior = empleado.obtenerSalarioBase();
            empleado.establecerSalarioBase(1.10 * salarioBaseAnterior);

            System.out.printf(
                  "Nuevo salario base con 10%% de aumento: $%,.2f\n",
                  empleado.obtenerSalarioBase());
         }

         System.out.printf("ingresos: $%,.2f\n\n",
               empleadoActual.ingresos());
      }

      // mostrar tipo de cada objeto
      for (int j = 0; j < empleados.length; j++) {
         System.out.printf("El empleado %d es un %s\n",
               j, empleados[j].getClass().getName());
      }
   }
}