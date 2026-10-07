/**
 * Clase Main
 * Aquí armo dos grafos de prueba y muestro su análisis.
 *
 * @author Amir Moisés Hernández Farah
 * Periodo 202660
 */
public class Main {

    public static void main(String[] args) {

        // ===== Grafo 1: tiene un bucle, dos paralelas y un vértice aislado =====
        Vertice v1 = new Vertice("v1", 1);
        Vertice v2 = new Vertice("v2", 2);
        Vertice v3 = new Vertice("v3", 3);
        Vertice v4 = new Vertice("v4", 4); // este no tiene aristas
        Vertice v5 = new Vertice("v5", 5);
        Vertice v6 = new Vertice("v6", 6);

        Grafo g1 = new Grafo("G1");
        g1.agregarVertice(v1);
        g1.agregarVertice(v2);
        g1.agregarVertice(v3);
        g1.agregarVertice(v4);
        g1.agregarVertice(v5);
        g1.agregarVertice(v6);

        g1.agregarArista(new Arista("e1", 1, v1, v2));
        g1.agregarArista(new Arista("e2", 2, v1, v3)); // e2 y e3 son paralelas
        g1.agregarArista(new Arista("e3", 3, v1, v3));
        g1.agregarArista(new Arista("e4", 4, v2, v3));
        g1.agregarArista(new Arista("e5", 5, v5, v6));
        g1.agregarArista(new Arista("e6", 6, v5, v5)); // bucle

        g1.mostrarAnalisisCompleto();

        System.out.println("Vértices (toString):");
        for (Vertice v : g1.getVertices()) {
            System.out.println("  " + v);
        }
        System.out.println("Aristas (toString):");
        for (Arista a : g1.getAristas()) {
            System.out.println("  " + a);
        }
        System.out.println();

        // ===== Grafo 2: dos bucles en c y tres aristas entre a y b =====
        Vertice a = new Vertice("a", 1);
        Vertice b = new Vertice("b", 2);
        Vertice c = new Vertice("c", 3);
        Vertice d = new Vertice("d", 4);

        Grafo g2 = new Grafo("G2");
        g2.agregarVertice(a);
        g2.agregarVertice(b);
        g2.agregarVertice(c);
        g2.agregarVertice(d);

        g2.agregarArista(new Arista("e1", 1, a, b));
        g2.agregarArista(new Arista("e2", 2, b, a));
        g2.agregarArista(new Arista("e3", 3, a, b));
        g2.agregarArista(new Arista("e4", 4, c, c));
        g2.agregarArista(new Arista("e5", 5, c, c));
        g2.agregarArista(new Arista("e6", 6, b, c));

        g2.mostrarAnalisisCompleto();

        // ===== Probar si puede existir un grafo con ciertos grados =====
        System.out.println("==================================================");
        System.out.println(" ¿PUEDE EXISTIR UN GRAFO CON ESTOS GRADOS?");
        System.out.println("==================================================");

        int[][] pruebas = {
            {3, 3, 2, 2},
            {1, 1, 3},
            {2, 2, 2},
            {4, 1, 1, 0},
            {1, 2, 3, 4}
        };

        for (int[] grados : pruebas) {
            int suma = 0;
            for (int g : grados) {
                suma = suma + g;
            }
            String respuesta;
            if (Grafo.puedeExistirGrafo(grados)) {
                respuesta = "SÍ puede existir";
            } else {
                respuesta = "NO puede existir (suma impar)";
            }
            System.out.println("  " + java.util.Arrays.toString(grados) + " -> suma = " + suma + " -> " + respuesta);
        }
    }
}
