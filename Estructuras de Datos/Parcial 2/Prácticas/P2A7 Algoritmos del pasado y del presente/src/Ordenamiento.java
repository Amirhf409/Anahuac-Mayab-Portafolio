/**
 * Clase Ordenamiento
 * Tiene los algoritmos que vimos en clase para ordenar los registros
 * de menor a mayor según su valor (edad o precio).
 *
 * @author Amir Moisés Hernández Farah
 */
public class Ordenamiento {

    // Cambia de lugar dos registros
    private static void intercambiar(Registro[] arr, int a, int b) {
        Registro aux = arr[a];
        arr[a] = arr[b];
        arr[b] = aux;
    }

    // Regresa una copia para que cada algoritmo ordene los mismos datos
    public static Registro[] copiar(Registro[] arr) {
        Registro[] copia = new Registro[arr.length];
        for (int i = 0; i < arr.length; i++) {
            copia[i] = arr[i];
        }
        return copia;
    }

    // BÁSICO - BURBUJA: compara vecinos y los cambia si están al revés
    public static void burbuja(Registro[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (arr[j].getValor() > arr[j + 1].getValor()) {
                    intercambiar(arr, j, j + 1);
                }
            }
        }
    }

    // BÁSICO - INSERCIÓN: mete cada registro en su lugar, como acomodar tarjetas
    public static void insercion(Registro[] arr) {
        for (int i = 1; i < arr.length; i++) {
            Registro actual = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j].getValor() > actual.getValor()) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = actual;
        }
    }

    // AVANZADO - QUICKSORT: toma un pivote, pone los menores a la izquierda
    // y los mayores a la derecha, y repite con cada lado
    public static void quicksort(Registro[] arr, int inicio, int fin) {
        if (inicio < fin) {
            int pivote = arr[fin].getValor();
            int i = inicio - 1;
            for (int j = inicio; j < fin; j++) {
                if (arr[j].getValor() < pivote) {
                    i++;
                    intercambiar(arr, i, j);
                }
            }
            intercambiar(arr, i + 1, fin);

            quicksort(arr, inicio, i);       // lado izquierdo
            quicksort(arr, i + 2, fin);      // lado derecho
        }
    }
}
