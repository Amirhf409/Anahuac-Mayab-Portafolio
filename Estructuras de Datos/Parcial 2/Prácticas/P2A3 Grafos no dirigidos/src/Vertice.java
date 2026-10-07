/**
 * Clase Vertice - Representa un vértice (nodo) de un grafo.
 *
 * Conceptos reforzados:
 * - Vértice como elemento fundamental de un grafo V(G)
 * - Vértice aislado: no incide arista alguna
 * - Grado de un vértice: número de extremos de aristas que salen de él
 *
 * @author Amir Moisés Hernández Farah
 * @version 1.0
 * Periodo 202660
 */
public class Vertice {

    // ============================
    // ATRIBUTOS
    // ============================
    private String nombre;     // Nombre del vértice (ej: "v1", "v2")
    private int id;            // Identificador numérico único
    private int grado;         // Grado del vértice (se calcula desde Grafo)
    private boolean esAislado; // true si no incide arista alguna (grado == 0)

    // ============================
    // CONSTRUCTORES
    // ============================

    /**
     * Constructor vacío.
     * Inicializa el vértice con valores por defecto.
     */
    public Vertice() {
        this.nombre = "";
        this.id = 0;
        this.grado = 0;
        this.esAislado = true;
    }

    /**
     * Constructor parametrizado.
     * @param nombre Nombre del vértice (ej: "v1")
     * @param id Identificador numérico único
     */
    public Vertice(String nombre, int id) {
        this.nombre = nombre;
        this.id = id;
        this.grado = 0;
        this.esAislado = true;
    }

    // ============================
    // GETTERS Y SETTERS
    // ============================

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

    // ============================
    // MÉTODOS AUXILIARES
    // ============================

    /**
     * Representación en texto del vértice.
     * Formato esperado: "v1 (grado: 3)" o "v4 (grado: 0) [AISLADO]"
     */
    @Override
    public String toString() {
        String texto = nombre + " (grado: " + grado + ")";
        if (esAislado) {
            texto += " [AISLADO]";
        }
        return texto;
    }
}
