/**
 * Clase Main
 * Simula un maratón de 150 corredores y ordena sus tiempos
 * con 5 algoritmos, midiendo cuánto tarda cada uno.
 *
 * @author Group 2: Amir Moisés Hernández Farah, Marco Antonio Gómez Fuentes,
 *         Emiliano Peniche Correa y Rodrigo Quijano López
 */
public class Main {

    public static void main(String[] args) {

        Maraton maraton = new Maraton(150);
        maraton.generarTiempos();

        System.out.println("===== SIMULACIÓN DE MARATÓN =====");
        System.out.println("Corredores: 150");
        System.out.println("Distancia: " + Maraton.DISTANCIA + " km");
        System.out.println();

        System.out.println("--- Tiempo de cada algoritmo ---");
        long inicio, fin;

        // Burbuja
        Corredor[] arr1 = maraton.copiar();
        inicio = System.nanoTime();
        maraton.burbuja(arr1);
        fin = System.nanoTime();
        System.out.println("Burbuja:   " + (fin - inicio) + " ns");

        // Selección
        Corredor[] arr2 = maraton.copiar();
        inicio = System.nanoTime();
        maraton.seleccion(arr2);
        fin = System.nanoTime();
        System.out.println("Selección: " + (fin - inicio) + " ns");

        // Inserción
        Corredor[] arr3 = maraton.copiar();
        inicio = System.nanoTime();
        maraton.insercion(arr3);
        fin = System.nanoTime();
        System.out.println("Inserción: " + (fin - inicio) + " ns");

        // Shell
        Corredor[] arr4 = maraton.copiar();
        inicio = System.nanoTime();
        maraton.shell(arr4);
        fin = System.nanoTime();
        System.out.println("Shell:     " + (fin - inicio) + " ns");

        // Quicksort
        Corredor[] arr5 = maraton.copiar();
        inicio = System.nanoTime();
        maraton.quicksort(arr5, 0, arr5.length - 1);
        fin = System.nanoTime();
        System.out.println("Quicksort: " + (fin - inicio) + " ns");
        System.out.println();

        // Ganador
        System.out.println("Mejor tiempo: " + arr5[0]);
        System.out.println();

        // Posiciones finales (todos los arreglos quedan igual, usamos uno)
        System.out.println("--- POSICIONES FINALES ---");
        for (int i = 0; i < arr5.length; i++) {
            System.out.println((i + 1) + ". " + arr5[i]);
        }
    }
}
