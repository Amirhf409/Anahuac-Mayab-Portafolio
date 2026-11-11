/**
 * Clase Registro
 * Representa un dato que queremos guardar y ordenar.
 * En el problema del censo es una persona (folio, nombre y edad)
 * y en el de la tienda es un producto (código, nombre y precio).
 *
 * @author Amir Moisés Hernández Farah
 */
public class Registro {

    private int clave;      // folio de la persona o código del producto
    private String nombre;
    private int valor;      // edad de la persona o precio del producto

    public Registro(int clave, String nombre, int valor) {
        this.clave = clave;
        this.nombre = nombre;
        this.valor = valor;
    }

    public int getClave() {
        return clave;
    }

    public String getNombre() {
        return nombre;
    }

    public int getValor() {
        return valor;
    }

    @Override
    public String toString() {
        return clave + " - " + nombre + " (" + valor + ")";
    }
}
