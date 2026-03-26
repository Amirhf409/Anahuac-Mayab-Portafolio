// Fig. 10.5: EmpleadoAsalariado.java
// La clase EmpleadoAsalariado extiende a Empleado.

public class EmpleadoAsalariado extends Empleado {
   private double salarioSemanal;

   // constructor de cuatro argumentos
   public EmpleadoAsalariado(String nombre, String apellido, String nss,
         double salario) {
      super(nombre, apellido, nss); // los pasa al constructor de Empleado
      establecerSalarioSemanal(salario); // valida y almacena el salario
   } // fin del constructor de EmpleadoAsalariado con cuatro argumentos

   // establece el salario
   public void establecerSalarioSemanal(double salario) {
      salarioSemanal = salario < 0.0 ? 0.0 : salario;
   } // fin del m�todo establecerSalarioSemanal

   // devuelve el salario
   public double obtenerSalarioSemanal() {
      return salarioSemanal;
   } // fin del m�todo obtenerSalarioSemanal

   // calcula los ingresos; sobrescribe el m�todo abstracto ingresos en Empleado
   public double ingresos() {
      return obtenerSalarioSemanal();
   } // fin del m�todo ingresos

   // devuelve representaci�n String de un objeto EmpleadoAsalariado
   public String toString() {
      return String.format("empleado asalariado: %s\n%s: $%,.2f",
            super.toString(), "salario semanal", obtenerSalarioSemanal());
   } // fin del m�todo toString
} // fin de la clase EmpleadoAsalariadoa.

/**************************************************************************
 * (C) Copyright 1992-2007 por Deitel & Associates, Inc. y *
 * Pearson Education, Inc. Todos los derechos reservados. *
 * *
 * RENUNCIA: Los autores y el editor de este libro han realizado su mejor *
 * esfuerzo para preparar este libro. Esto incluye el desarrollo, la *
 * investigaci�n y prueba de las teor�as y programas para determinar su *
 * efectividad. Los autores y el editor no hacen ninguna garant�a de *
 * ning�n tipo, expresa o impl�cita, en relaci�n con estos programas o *
 * con la documentaci�n contenida en estos libros. Los autores y el *
 * editor no ser�n responsables en ning�n caso por los da�os consecuentes *
 * en conexi�n con, o que surjan de, el suministro, desempe�o o uso de *
 * estos programas. *
 *************************************************************************/
