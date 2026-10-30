import java.util.Random;

/**
 * Clase Maraton
 * Tiene el arreglo de corredores y los 5 métodos de ordenamiento.
 *
 * @author Group 2: Amir Moisés Hernández Farah, Marco Antonio Gómez Fuentes,
 *         Emiliano Peniche Correa y Rodrigo Quijano López
 */
public class Maraton {

    public static final double DISTANCIA = 42.195; // km

    private Corredor[] corredores;

    public Maraton(int cantidad) {
        corredores = new Corredor[cantidad];
    }

    // Le da a cada corredor un tiempo al azar entre 120 y 300 minutos
    public void generarTiempos() {
        Random random = new Random();
        for (int i = 0; i < corredores.length; i++) {
            // 120 min = 7200 seg y 300 min = 18000 seg
            int segundos = 7200 + random.nextInt(10801);  // de 7200 a 18000
            corredores[i] = new Corredor(i + 1, segundos);
        }
    }

    // Regresa una copia para que cada algoritmo ordene los mismos datos
    public Corredor[] copiar() {
        Corredor[] copia = new Corredor[corredores.length];
        for (int i = 0; i < corredores.length; i++) {
            copia[i] = corredores[i];
        }
        return copia;
    }

    // Cambia de lugar dos corredores
    private void intercambiar(Corredor[] arr, int a, int b) {
        Corredor aux = arr[a];
        arr[a] = arr[b];
        arr[b] = aux;
    }

    // 1. BURBUJA: compara vecinos y los cambia si están al revés
    public void burbuja(Corredor[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (arr[j].getSegundos() > arr[j + 1].getSegundos()) {
                    intercambiar(arr, j, j + 1);
                }
            }
        }
    }

    // 2. SELECCIÓN: busca el menor y lo pone al inicio
    public void seleccion(Corredor[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int menor = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j].getSegundos() < arr[menor].getSegundos()) {
                    menor = j;
                }
            }
            intercambiar(arr, i, menor);
        }
    }

    // 3. INSERCIÓN: mete cada corredor en su lugar, como acomodar cartas
    public void insercion(Corredor[] arr) {
        for (int i = 1; i < arr.length; i++) {
            Corredor actual = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j].getSegundos() > actual.getSegundos()) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = actual;
        }
    }

    // 4. SHELL: como inserción, pero empieza comparando elementos lejanos
    public void shell(Corredor[] arr) {
        for (int salto = arr.length / 2; salto > 0; salto = salto / 2) {
            for (int i = salto; i < arr.length; i++) {
                Corredor actual = arr[i];
                int j = i;
                while (j >= salto && arr[j - salto].getSegundos() > actual.getSegundos()) {
                    arr[j] = arr[j - salto];
                    j = j - salto;
                }
                arr[j] = actual;
            }
        }
    }

    // 5. QUICKSORT: toma un pivote, pone los menores a la izquierda
    // y los mayores a la derecha, y repite con cada lado
    public void quicksort(Corredor[] arr, int inicio, int fin) {
        if (inicio < fin) {
            int pivote = arr[fin].getSegundos();
            int i = inicio - 1;
            for (int j = inicio; j < fin; j++) {
                if (arr[j].getSegundos() < pivote) {
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
