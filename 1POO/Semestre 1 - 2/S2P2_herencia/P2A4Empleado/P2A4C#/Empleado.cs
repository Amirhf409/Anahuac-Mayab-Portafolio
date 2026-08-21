//En este archivo basicamente solo copie y pegué el java, modifiqué las mayúsculas de strings
// el string format el Format cambia
// los %s cambian a {0} {1} {2}
// en C# el toString cambia a override string ToString() 

public abstract class Empleado 
{
   private string primerNombre;
   private string apellidoPaterno;
   private string numeroSeguroSocial;

   // constructor con tres argumentos
   public Empleado( string nombre, string apellido, string nss )
   {
      primerNombre = nombre;
      apellidoPaterno = apellido;
      numeroSeguroSocial = nss;
   } // fin del constructor de Empleado con tres argumentos

   // establece el primer nombre
   public void establecerPrimerNombre( string nombre )
   {
      primerNombre = nombre;
   } // fin del m�todo establecerPrimerNombre

   // devuelve el primer nombre
   public string obtenerPrimerNombre()
   {
      return primerNombre;
   } // fin del m�todo obtenerPrimerNombre

   // establece el apellido paterno
   public void establecerApellidoPaterno( string apellido )
   {
      apellidoPaterno = apellido;
   } // fin del m�todo establecerApellidoPaterno

   // devuelve el apellido paterno
   public string obtenerApellidoPaterno()
   {
      return apellidoPaterno;
   } // fin del m�todo obtenerApellidoPaterno

   // establece el n�mero de seguro social
   public void establecerNumeroSeguroSocial( string nss )
   {
      numeroSeguroSocial = nss; // debe validar
   } // fin del m�todo establecerNumeroSeguroSocial

   // devuelve el n�mero de seguro social
   public string obtenerNumeroSeguroSocial()
   {
      return numeroSeguroSocial;
   } // fin del m�todo obtenerNumeroSeguroSocial

   // devuelve representaci�n String de un objeto Empleado
   public override string ToString()
   {
      return string.Format("{0} {1}\nnumero de seguro social: {2}", 
         obtenerPrimerNombre(), obtenerApellidoPaterno(), obtenerNumeroSeguroSocial() );
   } // fin del m�todo toString

   // m�todo abstracto sobrescrito por las subclases
   public abstract double Ingresos(); // aqu� no hay implementaci�n
} // fin de la clase abstracta Empleado