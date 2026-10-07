import java.util.ArrayList;

/**
 * Clase Grafo - Representa un grafo no dirigido G = (V, E).
 *
 * Conceptos reforzados:
 * - Grafo G con conjuntos V(G) de vértices y E(G) de aristas
 * - Función punto extremo-arista
 * - Grado de vértice (bucle cuenta doble)
 * - Teorema del Saludo de Mano: gradoTotal = 2 × |E|
 * - Corolario 10.1.2: El grado total de un grafo siempre es par
 *
 * @author Amir Moisés Hernández Farah
 * @version 1.0
 * Periodo 202660
 */
public class Grafo {

    // ============================
    // ATRIBUTOS
    // ============================
    private String nombre;                // Nombre del grafo
    private ArrayList<Vertice> vertices;  // Conjunto V(G)
    private ArrayList<Arista> aristas;    // Conjunto E(G)
    private int gradoTotal;               // Suma de todos los grados

    // ============================
    // CONSTRUCTORES
    // ============================

    /**
     * Constructor vacío.
     */
    public Grafo() {
        this.nombre = "";
        this.vertices = new ArrayList<>();
        this.aristas = new ArrayList<>();
        this.gradoTotal = 0;
    }

    /**
     * Constructor parametrizado.
     * @param nombre Nombre del grafo
     */
    public Grafo(String nombre) {
        this.nombre = nombre;
        this.vertices = new ArrayList<>();
        this.aristas = new ArrayList<>();
        this.gradoTotal = 0;
    }

    // ============================
    // GETTERS
    // ============================

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

    // ============================
    // MÉTODOS DE CONSTRUCCIÓN
    // ============================

    /**
     * Agrega un vértice al conjunto V(G) del grafo.
     * @param v Vértice a agregar
     */
    public void agregarVertice(Vertice v) {
        if (v != null && !vertices.contains(v)) {
            vertices.add(v);
        }
    }

    /**
     * Agrega una arista al conjunto E(G) del grafo.
     * Si sus extremos aún no están en V(G), también se agregan.
     * @param a Arista a agregar
     */
    public void agregarArista(Arista a) {
        if (a == null) {
            return;
        }
        agregarVertice(a.getExtremo1());
        agregarVertice(a.getExtremo2());
        aristas.add(a);
    }

    // ============================
    // MÉTODOS DE GRADO
    // ============================

    /**
     * Calcula el GRADO de un vértice.
     *
     * REGLA CLAVE: Un bucle contribuye con 2 al grado del vértice.
     * Una arista normal que incide en v contribuye con 1.
     *
     * @param v Vértice al que se le calculará el grado
     * @return El grado del vértice
     */
    public int calcularGrado(Vertice v) {
        int grado = 0;
        for (Arista a : aristas) {
            if (a.incideEn(v)) {
                if (a.esBucle()) {
                    grado += 2; // el bucle cuenta doble
                } else {
                    grado += 1;
                }
            }
        }
        v.setGrado(grado);
        v.setEsAislado(grado == 0);
        return grado;
    }

    /**
     * Calcula el GRADO TOTAL del grafo.
     * Es la suma de los grados de todos los vértices.
     *
     * @return El grado total del grafo
     */
    public int calcularGradoTotal() {
        gradoTotal = 0;
        for (Vertice v : vertices) {
            gradoTotal += calcularGrado(v);
        }
        return gradoTotal;
    }

    // ============================
    // MÉTODOS DE TERMINOLOGÍA
    // ============================

    /**
     * Obtiene todos los vértices ADYACENTES a un vértice dado.
     * Dos vértices son adyacentes si están conectados por una arista.
     * Si v tiene un bucle, v es adyacente a sí mismo.
     *
     * @param v Vértice de referencia
     * @return Lista de vértices adyacentes a v
     */
    public ArrayList<Vertice> obtenerAdyacentes(Vertice v) {
        ArrayList<Vertice> adyacentes = new ArrayList<>();
        for (Arista a : aristas) {
            if (!a.incideEn(v)) {
                continue;
            }
            Vertice otro;
            if (a.esBucle()) {
                otro = v; // adyacente a sí mismo
            } else if (a.getExtremo1().getId() == v.getId()) {
                otro = a.getExtremo2();
            } else {
                otro = a.getExtremo1();
            }
            if (!adyacentes.contains(otro)) {
                adyacentes.add(otro);
            }
        }
        return adyacentes;
    }

    /**
     * Obtiene todas las aristas que INCIDEN en un vértice dado.
     *
     * @param v Vértice de referencia
     * @return Lista de aristas incidentes en v
     */
    public ArrayList<Arista> obtenerAristasIncidentes(Vertice v) {
        ArrayList<Arista> incidentes = new ArrayList<>();
        for (Arista a : aristas) {
            if (a.incideEn(v)) {
                incidentes.add(a);
            }
        }
        return incidentes;
    }

    /**
     * Obtiene todas las aristas ADYACENTES a una arista dada.
     * Dos aristas son adyacentes si comparten al menos un punto extremo.
     *
     * @param a Arista de referencia
     * @return Lista de aristas adyacentes a la arista a
     */
    public ArrayList<Arista> obtenerAristasAdyacentes(Arista a) {
        ArrayList<Arista> adyacentes = new ArrayList<>();
        for (Arista b : aristas) {
            if (b.getId() == a.getId()) {
                continue; // no comparar consigo misma
            }
            if (b.incideEn(a.getExtremo1()) || b.incideEn(a.getExtremo2())) {
                adyacentes.add(b);
            }
        }
        return adyacentes;
    }

    /**
     * Obtiene todos los BUCLES del grafo.
     *
     * @return Lista de aristas que son bucles
     */
    public ArrayList<Arista> obtenerBucles() {
        ArrayList<Arista> bucles = new ArrayList<>();
        for (Arista a : aristas) {
            if (a.esBucle()) {
                bucles.add(a);
            }
        }
        return bucles;
    }

    /**
     * Obtiene los pares de aristas PARALELAS del grafo.
     *
     * @return Lista de cadenas describiendo los pares paralelos, formato "{e2, e3}"
     */
    public ArrayList<String> obtenerParalelas() {
        ArrayList<String> paralelas = new ArrayList<>();
        for (int i = 0; i < aristas.size(); i++) {
            for (int j = i + 1; j < aristas.size(); j++) {
                Arista ai = aristas.get(i);
                Arista aj = aristas.get(j);
                if (ai.esParalela(aj)) {
                    paralelas.add("{" + ai.getNombre() + ", " + aj.getNombre() + "}");
                }
            }
        }
        return paralelas;
    }

    /**
     * Obtiene todos los vértices AISLADOS del grafo (grado = 0).
     *
     * @return Lista de vértices aislados
     */
    public ArrayList<Vertice> obtenerVerticesAislados() {
        calcularGradoTotal(); // asegura que los grados estén actualizados
        ArrayList<Vertice> aislados = new ArrayList<>();
        for (Vertice v : vertices) {
            if (v.getGrado() == 0) {
                aislados.add(v);
            }
        }
        return aislados;
    }

    // ============================
    // TEOREMAS
    // ============================

    /**
     * Verifica el TEOREMA DEL SALUDO DE MANO:
     * la suma de los grados de todos los vértices es igual a 2 × |E|.
     * (Corolario: el grado total siempre es par.)
     *
     * @return true si gradoTotal == 2 * |E|
     */
    public boolean verificarTeoremaSaludo() {
        calcularGradoTotal();
        return gradoTotal == 2 * aristas.size();
    }

    /**
     * Determina si puede existir un grafo (permitiendo bucles y aristas
     * paralelas) con la sucesión de grados dada.
     * Por el teorema del saludo de mano, la suma de grados debe ser par;
     * además ningún grado puede ser negativo. Si se cumple, siempre se puede
     * construir: se emparejan los vértices de grado impar con una arista
     * y el resto del grado se completa con bucles (cada bucle aporta 2).
     *
     * @param grados Arreglo con los grados de cada vértice
     * @return true si existe un grafo con esos grados
     */
    public static boolean puedeExistirGrafo(int[] grados) {
        if (grados == null) {
            return false;
        }
        int suma = 0;
        for (int g : grados) {
            if (g < 0) {
                return false;
            }
            suma += g;
        }
        return suma % 2 == 0;
    }

    // ============================
    // MÉTODOS DE PRESENTACIÓN
    // ============================

    /**
     * Convierte una lista de vértices a texto: "{v1, v2}".
     */
    private String nombresVertices(ArrayList<Vertice> lista) {
        StringBuilder sb = new StringBuilder("{");
        for (int i = 0; i < lista.size(); i++) {
            sb.append(lista.get(i).getNombre());
            if (i < lista.size() - 1) {
                sb.append(", ");
            }
        }
        return sb.append("}").toString();
    }

    /**
     * Convierte una lista de aristas a texto: "{e1, e2}".
     */
    private String nombresAristas(ArrayList<Arista> lista) {
        StringBuilder sb = new StringBuilder("{");
        for (int i = 0; i < lista.size(); i++) {
            sb.append(lista.get(i).getNombre());
            if (i < lista.size() - 1) {
                sb.append(", ");
            }
        }
        return sb.append("}").toString();
    }

    /**
     * Muestra la TABLA DE FUNCIÓN PUNTO EXTREMO-ARISTA.
     */
    public void mostrarTablaExtremos() {
        System.out.println("\n--- Tabla Punto Extremo - Arista ---");
        System.out.printf("| %-8s | %-22s |%n", "Arista", "Punto(s) Extremo(s)");
        System.out.println("|----------|------------------------|");
        for (Arista a : aristas) {
            String extremos = a.extremosTexto();
            if (a.esBucle()) {
                extremos += " [BUCLE]";
            }
            System.out.printf("| %-8s | %-22s |%n", a.getNombre(), extremos);
        }
    }

    /**
     * Imprime un reporte con toda la información del grafo.
     */
    public void mostrarAnalisisCompleto() {
        calcularGradoTotal();

        System.out.println("==================================================");
        System.out.println(" ANÁLISIS COMPLETO DEL " + toString());
        System.out.println("==================================================");

        // Conjuntos V(G) y E(G)
        System.out.println("V(G) = " + nombresVertices(vertices));
        System.out.println("E(G) = " + nombresAristas(aristas));

        // Tabla de función punto extremo-arista
        mostrarTablaExtremos();

        // Grados
        System.out.println("\n--- Grado de cada vértice ---");
        for (Vertice v : vertices) {
            System.out.println("  deg(" + v.getNombre() + ") = " + v.getGrado()
                    + (v.esAislado() ? "  [AISLADO]" : ""));
        }
        System.out.println("  Grado total = " + gradoTotal);

        // Adyacencia e incidencia por vértice
        System.out.println("\n--- Adyacencia e incidencia por vértice ---");
        for (Vertice v : vertices) {
            System.out.println("  " + v.getNombre()
                    + " -> adyacentes: " + nombresVertices(obtenerAdyacentes(v))
                    + " | aristas incidentes: " + nombresAristas(obtenerAristasIncidentes(v)));
        }

        // Aristas adyacentes
        System.out.println("\n--- Aristas adyacentes ---");
        for (Arista a : aristas) {
            System.out.println("  " + a.getNombre() + " es adyacente a: "
                    + nombresAristas(obtenerAristasAdyacentes(a)));
        }

        // Bucles, paralelas y aislados
        System.out.println("\n--- Terminología ---");
        ArrayList<Arista> bucles = obtenerBucles();
        System.out.println("  Bucles: " + (bucles.isEmpty() ? "ninguno" : nombresAristas(bucles)));
        ArrayList<String> paralelas = obtenerParalelas();
        System.out.println("  Aristas paralelas: " + (paralelas.isEmpty() ? "ninguna" : String.join(", ", paralelas)));
        ArrayList<Vertice> aislados = obtenerVerticesAislados();
        System.out.println("  Vértices aislados: " + (aislados.isEmpty() ? "ninguno" : nombresVertices(aislados)));

        // Teorema del saludo de mano
        System.out.println("\n--- Teorema del Saludo de Mano ---");
        System.out.println("  Grado total = " + gradoTotal + ",  2 x |E| = 2 x " + aristas.size()
                + " = " + (2 * aristas.size()));
        System.out.println("  ¿Se cumple? " + (verificarTeoremaSaludo() ? "SÍ" : "NO"));
        System.out.println("  ¿Grado total par? (Corolario) " + (gradoTotal % 2 == 0 ? "SÍ" : "NO"));
        System.out.println();
    }

    // ============================
    // MÉTODOS AUXILIARES
    // ============================

    /**
     * Representación en texto del grafo.
     * Formato: "Grafo [nombre]: |V| = X, |E| = Y"
     */
    @Override
    public String toString() {
        return "Grafo " + nombre + ": |V| = " + vertices.size() + ", |E| = " + aristas.size();
    }
}
