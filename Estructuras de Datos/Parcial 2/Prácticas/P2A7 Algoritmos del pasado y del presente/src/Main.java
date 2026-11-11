import java.util.Random;

/**
 * Clase Main
 * Resuelve los dos problemas del reporte con los algoritmos de clase:
 *   1. Problema antiguo: el censo de 1890 (ordenar y buscar personas).
 *   2. Problema moderno: el catálogo de una tienda en línea.
 *
 * @author Amir Moisés Hernández Farah
 */
public class Main {

    public static void main(String[] args) {
        Random random = new Random();
        long inicio, fin;

        // ===================== PROBLEMA 1: CENSO =====================
        System.out.println("===== PROBLEMA 1: CENSO (1890) =====");
        int personas = 5000;
        Registro[] censo = new Registro[personas];
        for (int i = 0; i < personas; i++) {
            int edad = random.nextInt(91);   // de 0 a 90 años
            censo[i] = new Registro(i + 1, "Persona " + (i + 1), edad);
        }
        System.out.println("Personas registradas: " + personas);
        System.out.println();

        System.out.println("--- Ordenar por edad ---");
        Registro[] c1 = Ordenamiento.copiar(censo);
        inicio = System.nanoTime();
        Ordenamiento.insercion(c1);
        fin = System.nanoTime();
        System.out.println("Inserción: " + (fin - inicio) / 1000000 + " ms");

        Registro[] c2 = Ordenamiento.copiar(censo);
        inicio = System.nanoTime();
        Ordenamiento.quicksort(c2, 0, c2.length - 1);
        fin = System.nanoTime();
        System.out.println("Quicksort: " + (fin - inicio) / 1000000 + " ms");
        System.out.println("Persona más joven: " + c2[0]);
        System.out.println("Persona más grande: " + c2[personas - 1]);
        System.out.println();

        System.out.println("--- Buscar una persona por folio ---");
        int folio = 4321;
        // Sin hash: revisar tarjeta por tarjeta
        int pasosLineal = 0;
        for (int i = 0; i < personas; i++) {
            pasosLineal++;
            if (censo[i].getClave() == folio) {
                break;
            }
        }
        System.out.println("Búsqueda tarjeta por tarjeta: " + pasosLineal + " pasos");

        // Con hash: la función nos dice en qué casilla está
        TablaHash tablaCenso = new TablaHash(personas * 2);
        for (int i = 0; i < personas; i++) {
            tablaCenso.insertar(censo[i]);
        }
        Registro encontrada = tablaCenso.buscar(folio);
        System.out.println("Búsqueda con tabla hash: " + tablaCenso.getPasos() + " paso(s) -> " + encontrada);
        System.out.println();

        // ================== PROBLEMA 2: TIENDA EN LÍNEA ==================
        System.out.println("===== PROBLEMA 2: TIENDA EN LÍNEA =====");
        int productos = 20000;
        Registro[] catalogo = new Registro[productos];
        for (int i = 0; i < productos; i++) {
            int codigo = 100000 + i * 7;               // códigos distintos
            int precio = 50 + random.nextInt(19951);    // de $50 a $20,000
            catalogo[i] = new Registro(codigo, "Producto " + (i + 1), precio);
        }
        System.out.println("Productos en el catálogo: " + productos);
        System.out.println();

        System.out.println("--- Ordenar por precio (de menor a mayor) ---");
        Registro[] t1 = Ordenamiento.copiar(catalogo);
        inicio = System.nanoTime();
        Ordenamiento.burbuja(t1);
        fin = System.nanoTime();
        System.out.println("Burbuja:   " + (fin - inicio) / 1000000 + " ms");

        Registro[] t2 = Ordenamiento.copiar(catalogo);
        inicio = System.nanoTime();
        Ordenamiento.quicksort(t2, 0, t2.length - 1);
        fin = System.nanoTime();
        System.out.println("Quicksort: " + (fin - inicio) / 1000000 + " ms");
        System.out.println("Más barato: " + t2[0]);
        System.out.println("Más caro:   " + t2[productos - 1]);
        System.out.println();

        System.out.println("--- Buscar un producto por código ---");
        int codigoBuscado = catalogo[productos - 1].getClave();   // el último del catálogo
        int pasosTienda = 0;
        for (int i = 0; i < productos; i++) {
            pasosTienda++;
            if (catalogo[i].getClave() == codigoBuscado) {
                break;
            }
        }
        System.out.println("Búsqueda uno por uno: " + pasosTienda + " pasos");

        TablaHash tablaTienda = new TablaHash(productos * 2);
        for (int i = 0; i < productos; i++) {
            tablaTienda.insertar(catalogo[i]);
        }
        Registro producto = tablaTienda.buscar(codigoBuscado);
        System.out.println("Búsqueda con tabla hash: " + tablaTienda.getPasos() + " paso(s) -> " + producto);
    }
}
