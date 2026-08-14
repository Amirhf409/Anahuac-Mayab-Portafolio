// Fig. 10.8: EmpleadoBaseMasComision.cs
// La clase EmpleadoBaseMasComision hereda de EmpleadoPorComision.

public class EmpleadoBaseMasComision : EmpleadoPorComision {
   private double salarioBase; // salario base por semana

   // constructor con seis argumentos
   public EmpleadoBaseMasComision(string nombre, string apellido,
         string nss, double ventas, double tarifa, double salario) 
         : base(nombre, apellido, nss, ventas, tarifa)
   {
      establecerSalarioBase(salario); // valida y almacena el salario base
   } // fin del constructor de EmpleadoBaseMasComision con seis argumentos

   // establece el salario base
   public void establecerSalarioBase(double salario) {
      salarioBase = (salario < 0.0) ? 0.0 : salario; // positivo
   } // fin del mtodo establecerSalarioBase

   // devuelve el salario base
   public double obtenerSalarioBase() {
      return salarioBase;
   } // fin del mtodo obtenerSalarioBase

   // calcula los ingresos; sobrescribe el mtodo ingresos en EmpleadoPorComision
   public override double Ingresos() {
      return obtenerSalarioBase() + base.Ingresos();
   } // fin del mtodo Ingresos

   // devuelve representacin string de un objeto EmpleadoBaseMasComision
   public override string ToString() {
      return string.Format("{0} {1}\n{2}: {3:C2}",
            "con salario base", base.ToString(),
            "salario base", obtenerSalarioBase());
   } // fin del mtodo ToString
} // fin de la clase EmpleadoBaseMasComision
