/**
 * Clase Vertice
 * Representa un punto (nodo) del grafo.
 *
 * @author Amir Moisés Hernández Farah
 * Periodo 202660
 */
public class Vertice {

    // Atributos
    private String nombre;     // ej: "v1"
    private int id;            // número para identificarlo
    private int grado;         // cuántas aristas le llegan (lo calcula el Grafo)
    private boolean esAislado; // true si no tiene ninguna arista

    // Constructor vacío
    public Vertice() {
        nombre = "";
        id = 0;
        grado = 0;
        esAislado = true;
    }

    // Constructor con nombre e id
    public Vertice(String nombre, int id) {
        this.nombre = nombre;
        this.id = id;
        this.grado = 0;
        this.esAislado = true;
    }

    // Getters y setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getGrado() {
        return grado;
    }

    public void setGrado(int grado) {
        this.grado = grado;
    }

    public boolean esAislado() {
        return esAislado;
    }

    public void setEsAislado(boolean esAislado) {
        this.esAislado = esAislado;
    }

    // Ejemplo: "v1 (grado: 3)" o "v4 (grado: 0) [AISLADO]"
    @Override
    public String toString() {
        String texto = nombre + " (grado: " + grado + ")";
        if (esAislado) {
            texto = texto + " [AISLADO]";
        }
        return texto;
    }
}
