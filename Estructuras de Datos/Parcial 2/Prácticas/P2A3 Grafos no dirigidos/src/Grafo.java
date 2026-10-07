import java.util.ArrayList;

/**
 * Clase Grafo
 * Guarda la lista de vértices y la lista de aristas, y hace el análisis
 * del grafo: grados, adyacencia, bucles, paralelas, aislados, etc.
 *
 * @author Amir Moisés Hernández Farah
 * Periodo 202660
 */
public class Grafo {

    // Atributos
    private String nombre;
    private ArrayList<Vertice> vertices;  // V(G)
    private ArrayList<Arista> aristas;    // E(G)
    private int gradoTotal;               // suma de todos los grados

    // Constructor vacío
    public Grafo() {
        nombre = "";
        vertices = new ArrayList<>();
        aristas = new ArrayList<>();
        gradoTotal = 0;
    }

    // Constructor con nombre
    public Grafo(String nombre) {
        this.nombre = nombre;
        vertices = new ArrayList<>();
        aristas = new ArrayList<>();
        gradoTotal = 0;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public ArrayList<Vertice> getVertices() {
        return vertices;
    }

    public ArrayList<Arista> getAristas() {
        return aristas;
    }

    public int getGradoTotal() {
        return gradoTotal;
    }

    // ---------- Agregar cosas al grafo ----------

    public void agregarVertice(Vertice v) {
        vertices.add(v);
    }

    public void agregarArista(Arista a) {
        aristas.add(a);
    }

    // ---------- Grados ----------

    // Grado de v: un bucle suma 2, una arista normal suma 1
    public int calcularGrado(Vertice v) {
        int grado = 0;
        for (Arista a : aristas) {
            if (a.incideEn(v)) {
                if (a.esBucle()) {
                    grado = grado + 2;
                } else {
                    grado = grado + 1;
                }
            }
        }
        v.setGrado(grado);
        v.setEsAislado(grado == 0);
        return grado;
    }

    // Suma los grados de todos los vértices
    public int calcularGradoTotal() {
        gradoTotal = 0;
        for (Vertice v : vertices) {
            gradoTotal = gradoTotal + calcularGrado(v);
        }
        return gradoTotal;
    }

    // ---------- Terminología ----------

    // Vértices que están unidos a v por una arista
    // (si v tiene bucle, v es adyacente a sí mismo)
    public ArrayList<Vertice> obtenerAdyacentes(Vertice v) {
        ArrayList<Vertice> adyacentes = new ArrayList<>();
        for (Arista a : aristas) {
            if (a.incideEn(v)) {
                Vertice otro;
                if (a.esBucle()) {
                    otro = v;
                } else if (a.getExtremo1().getId() == v.getId()) {
                    otro = a.getExtremo2();
                } else {
                    otro = a.getExtremo1();
                }
                // para no repetir vértices
                if (!adyacentes.contains(otro)) {
                    adyacentes.add(otro);
                }
            }
        }
        return adyacentes;
    }

    // Aristas que tocan al vértice v
    public ArrayList<Arista> obtenerAristasIncidentes(Vertice v) {
        ArrayList<Arista> incidentes = new ArrayList<>();
        for (Arista a : aristas) {
            if (a.incideEn(v)) {
                incidentes.add(a);
            }
        }
        return incidentes;
    }

    // Aristas que comparten al menos un vértice con la arista a
    public ArrayList<Arista> obtenerAristasAdyacentes(Arista a) {
        ArrayList<Arista> adyacentes = new ArrayList<>();
        for (Arista b : aristas) {
            if (b.getId() != a.getId()) {
                if (b.incideEn(a.getExtremo1()) || b.incideEn(a.getExtremo2())) {
                    adyacentes.add(b);
                }
            }
        }
        return adyacentes;
    }

    // Todas las aristas que son bucle
    public ArrayList<Arista> obtenerBucles() {
        ArrayList<Arista> bucles = new ArrayList<>();
        for (Arista a : aristas) {
            if (a.esBucle()) {
                bucles.add(a);
            }
        }
        return bucles;
    }

    // Pares de aristas paralelas, ej: "{e2, e3}"
    // El segundo for empieza en i+1 para no repetir pares
    public ArrayList<String> obtenerParalelas() {
        ArrayList<String> paralelas = new ArrayList<>();
        for (int i = 0; i < aristas.size(); i++) {
            for (int j = i + 1; j < aristas.size(); j++) {
                if (aristas.get(i).esParalela(aristas.get(j))) {
                    paralelas.add("{" + aristas.get(i).getNombre() + ", " + aristas.get(j).getNombre() + "}");
                }
            }
        }
        return paralelas;
    }

    // Vértices con grado 0
    public ArrayList<Vertice> obtenerVerticesAislados() {
        calcularGradoTotal(); // primero actualizamos los grados
        ArrayList<Vertice> aislados = new ArrayList<>();
        for (Vertice v : vertices) {
            if (v.getGrado() == 0) {
                aislados.add(v);
            }
        }
        return aislados;
    }

    // ---------- Teoremas ----------

    // Teorema del saludo de mano: suma de grados = 2 x número de aristas
    public boolean verificarTeoremaSaludo() {
        calcularGradoTotal();
        return gradoTotal == 2 * aristas.size();
    }

    // Puede existir un grafo con esos grados si la suma es par
    // (y no hay grados negativos)
    public static boolean puedeExistirGrafo(int[] grados) {
        int suma = 0;
        for (int g : grados) {
            if (g < 0) {
                return false;
            }
            suma = suma + g;
        }
        return suma % 2 == 0;
    }

    // ---------- Imprimir ----------

    // Pasa una lista de vértices a texto: "{v1, v2}"
    private String textoVertices(ArrayList<Vertice> lista) {
        String texto = "{";
        for (int i = 0; i < lista.size(); i++) {
            texto = texto + lista.get(i).getNombre();
            if (i < lista.size() - 1) {
                texto = texto + ", ";
            }
        }
        return texto + "}";
    }

    // Pasa una lista de aristas a texto: "{e1, e2}"
    private String textoAristas(ArrayList<Arista> lista) {
        String texto = "{";
        for (int i = 0; i < lista.size(); i++) {
            texto = texto + lista.get(i).getNombre();
            if (i < lista.size() - 1) {
                texto = texto + ", ";
            }
        }
        return texto + "}";
    }

    // Tabla de función punto extremo-arista
    public void mostrarTablaExtremos() {
        System.out.println("\n--- Tabla Punto Extremo - Arista ---");
        System.out.printf("| %-8s | %-22s |%n", "Arista", "Punto(s) Extremo(s)");
        System.out.println("|----------|------------------------|");
        for (Arista a : aristas) {
            String extremos = a.extremosTexto();
            if (a.esBucle()) {
                extremos = extremos + " [BUCLE]";
            }
            System.out.printf("| %-8s | %-22s |%n", a.getNombre(), extremos);
        }
    }

    // Reporte con todo el análisis del grafo
    public void mostrarAnalisisCompleto() {
        calcularGradoTotal();

        System.out.println("==================================================");
        System.out.println(" ANÁLISIS COMPLETO DEL " + toString());
        System.out.println("==================================================");
        System.out.println("V(G) = " + textoVertices(vertices));
        System.out.println("E(G) = " + textoAristas(aristas));

        mostrarTablaExtremos();

        System.out.println("\n--- Grado de cada vértice ---");
        for (Vertice v : vertices) {
            String extra = "";
            if (v.esAislado()) {
                extra = "  [AISLADO]";
            }
            System.out.println("  deg(" + v.getNombre() + ") = " + v.getGrado() + extra);
        }
        System.out.println("  Grado total = " + gradoTotal);

        System.out.println("\n--- Adyacencia e incidencia por vértice ---");
        for (Vertice v : vertices) {
            System.out.println("  " + v.getNombre()
                    + " -> adyacentes: " + textoVertices(obtenerAdyacentes(v))
                    + " | aristas incidentes: " + textoAristas(obtenerAristasIncidentes(v)));
        }

        System.out.println("\n--- Aristas adyacentes ---");
        for (Arista a : aristas) {
            System.out.println("  " + a.getNombre() + " es adyacente a: "
                    + textoAristas(obtenerAristasAdyacentes(a)));
        }

        System.out.println("\n--- Terminología ---");
        ArrayList<Arista> bucles = obtenerBucles();
        if (bucles.isEmpty()) {
            System.out.println("  Bucles: ninguno");
        } else {
            System.out.println("  Bucles: " + textoAristas(bucles));
        }

        ArrayList<String> paralelas = obtenerParalelas();
        if (paralelas.isEmpty()) {
            System.out.println("  Aristas paralelas: ninguna");
        } else {
            System.out.println("  Aristas paralelas: " + String.join(", ", paralelas));
        }

        ArrayList<Vertice> aislados = obtenerVerticesAislados();
        if (aislados.isEmpty()) {
            System.out.println("  Vértices aislados: ninguno");
        } else {
            System.out.println("  Vértices aislados: " + textoVertices(aislados));
        }

        System.out.println("\n--- Teorema del Saludo de Mano ---");
        System.out.println("  Grado total = " + gradoTotal + ",  2 x |E| = 2 x " + aristas.size()
                + " = " + (2 * aristas.size()));
        System.out.println("  ¿Se cumple? " + (verificarTeoremaSaludo() ? "SÍ" : "NO"));
        System.out.println("  ¿Grado total par? (Corolario) " + (gradoTotal % 2 == 0 ? "SÍ" : "NO"));
        System.out.println();
    }

    // Ejemplo: "Grafo G1: |V| = 6, |E| = 6"
    @Override
    public String toString() {
        return "Grafo " + nombre + ": |V| = " + vertices.size() + ", |E| = " + aristas.size();
    }
}
