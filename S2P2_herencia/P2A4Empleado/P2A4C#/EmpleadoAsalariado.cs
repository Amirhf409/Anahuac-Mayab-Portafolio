// Fig. 10.5: EmpleadoAsalariado.cs
// La clase EmpleadoAsalariado hereda de Empleado.

public class EmpleadoAsalariado : Empleado 
{
   private double salarioSemanal;

   // constructor de cuatro argumentos
   public EmpleadoAsalariado( string nombre, string apellido, string nss, 
      double salario ) : base( nombre, apellido, nss )
   {
      establecerSalarioSemanal( salario ); // valida y almacena el salario
   } // fin del constructor de EmpleadoAsalariado con cuatro argumentos

   // establece el salario
   public void establecerSalarioSemanal( double salario )
   {
      salarioSemanal = salario < 0.0 ? 0.0 : salario;
   } // fin del mtodo establecerSalarioSemanal

   // devuelve el salario
   public double obtenerSalarioSemanal()
   {
      return salarioSemanal;
   } // fin del mtodo obtenerSalarioSemanal

   // calcula los ingresos; sobrescribe el mtodo abstracto ingresos en Empleado
   public override double Ingresos()
   {
      return obtenerSalarioSemanal();
   } // fin del mtodo Ingresos

   // devuelve representacin string de un objeto EmpleadoAsalariado
   public override string ToString()
   {
      return string.Format( "empleado asalariado: {0}\n{1}: {2:C2}", 
         base.ToString(), "salario semanal", obtenerSalarioSemanal() );
   } // fin del mtodo ToString
} // fin de la clase EmpleadoAsalariado
