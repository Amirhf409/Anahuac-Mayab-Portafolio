/**
 * Clase padre (abstracta) de todo lo que se guarda en el sistema de archivos.
 * Cada objeto de esta clase es un NODO del arbol binario de busqueda (ABB).
 * De aqui heredan Directorio y Archivo.
 */
public abstract class ElementoSistema {

    // nombre del elemento, es la "clave" para ordenar el arbol
    protected String nombre;

    // hijos del nodo dentro del ABB
    protected ElementoSistema izquierdo;
    protected ElementoSistema derecho;

    // constructor: todo elemento nace sin hijos
    public ElementoSistema(String nombre) {
        this.nombre = nombre;
        this.izquierdo = null;
        this.derecho = null;
    }

    // cada hijo dice que tipo es ("Directorio" o "Archivo")
    public abstract String getTipo();

    // cada hijo regresa su extension ("-" si no tiene)
    public abstract String getExtension();

    // cada hijo regresa su tamano en bytes
    public abstract long getTamano();

    // nos dice si el elemento puede tener hijos o no
    public abstract boolean puedeTenerHijos();

    // regresa true si el nodo no tiene ningun hijo (es hoja)
    public boolean esHoja() {
        return izquierdo == null && derecho == null;
    }

    // compara este elemento con un nombre, en orden alfabetico y sin importar mayusculas
    // negativo = el nombre va antes, positivo = va despues, 0 = son iguales
    public int compararCon(String otroNombre) {
        return nombre.compareToIgnoreCase(otroNombre);
    }

    // imprime la informacion completa del elemento (para buscar y mostrar info)
    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Extension: " + getExtension());
        System.out.println("Tipo: " + getTipo());
        System.out.println("Tamano: " + getTamano() + " bytes");
    }

    // regresa una linea tipo tabla, se usa en los recorridos
    public String filaTabla() {
        return String.format("%-15s %-6s %-10d %-10s", nombre, getExtension(), getTamano(), getTipo());
    }

    // ----- getters y setters -----
    public String getNombre() {
        return nombre;
    }

    public ElementoSistema getIzquierdo() {
        return izquierdo;
    }

    public void setIzquierdo(ElementoSistema izquierdo) {
        this.izquierdo = izquierdo;
    }

    public ElementoSistema getDerecho() {
        return derecho;
    }

    public void setDerecho(ElementoSistema derecho) {
        this.derecho = derecho;
    }
}
