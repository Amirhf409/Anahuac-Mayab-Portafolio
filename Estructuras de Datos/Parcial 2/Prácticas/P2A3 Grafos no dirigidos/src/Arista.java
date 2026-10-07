/**
 * Clase Arista
 * Representa una línea que une dos vértices.
 * Si los dos extremos son el mismo vértice, es un bucle.
 *
 * @author Amir Moisés Hernández Farah
 * Periodo 202660
 */
public class Arista {

    // Atributos
    private String nombre;     // ej: "e1"
    private int id;
    private Vertice extremo1;
    private Vertice extremo2;
    private boolean esBucle;   // true si extremo1 y extremo2 son el mismo

    // Constructor vacío
    public Arista() {
        nombre = "";
        id = 0;
        extremo1 = null;
        extremo2 = null;
        esBucle = false;
    }

    // Constructor con datos; aquí revisamos si es bucle
    public Arista(String nombre, int id, Vertice extremo1, Vertice extremo2) {
        this.nombre = nombre;
        this.id = id;
        this.extremo1 = extremo1;
        this.extremo2 = extremo2;
        this.esBucle = (extremo1.getId() == extremo2.getId());
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public int getId() {
        return id;
    }

    public Vertice getExtremo1() {
        return extremo1;
    }

    public Vertice getExtremo2() {
        return extremo2;
    }

    public boolean esBucle() {
        return esBucle;
    }

    // Dos aristas son paralelas si unen los mismos vértices
    // ({v1, v3} es lo mismo que {v3, v1})
    public boolean esParalela(Arista otra) {
        if (this.id == otra.id) {
            return false; // es la misma arista
        }
        int a1 = this.extremo1.getId();
        int a2 = this.extremo2.getId();
        int b1 = otra.extremo1.getId();
        int b2 = otra.extremo2.getId();

        boolean mismoOrden = (a1 == b1 && a2 == b2);
        boolean alReves = (a1 == b2 && a2 == b1);
        return mismoOrden || alReves;
    }

    // La arista incide en v si v es uno de sus extremos
    public boolean incideEn(Vertice v) {
        return extremo1.getId() == v.getId() || extremo2.getId() == v.getId();
    }

    // Regresa los extremos así: "{v1, v2}" o "{v5}" si es bucle
    public String extremosTexto() {
        if (esBucle) {
            return "{" + extremo1.getNombre() + "}";
        }
        return "{" + extremo1.getNombre() + ", " + extremo2.getNombre() + "}";
    }

    // Ejemplo: "e1: {v1, v2}" o "e6: {v5} [BUCLE]"
    @Override
    public String toString() {
        String texto = nombre + ": " + extremosTexto();
        if (esBucle) {
            texto = texto + " [BUCLE]";
        }
        return texto;
    }
}
