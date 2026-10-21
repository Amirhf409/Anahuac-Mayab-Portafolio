/**
 * Clase RegistroTemperaturas
 * Guarda en un arreglo las temperaturas del mes y las ordena
 * con el algoritmo de burbuja (bubble sort), de menor a mayor
 * y de mayor a menor.
 *
 * @author Amir Moisés Hernández Farah
 * Periodo 202660
 */
public class RegistroTemperaturas {

    // Atributos
    private String ciudad;
    private Temperatura[] temperaturas;  // arreglo con los registros
    private int cantidad;                // cuántas temperaturas llevamos guardadas

    // Constructor vacío
    public RegistroTemperaturas() {
        ciudad = "";
        temperaturas = new Temperatura[31];
        cantidad = 0;
    }

    // Constructor con la ciudad y el tamaño del arreglo
    public RegistroTemperaturas(String ciudad, int tamano) {
        this.ciudad = ciudad;
        temperaturas = new Temperatura[tamano];
        cantidad = 0;
    }

    // Getters
    public String getCiudad() {
        return ciudad;
    }

    public int getCantidad() {
        return cantidad;
    }

    // Agrega una temperatura al arreglo si todavía hay espacio
    public void agregar(Temperatura t) {
        if (cantidad < temperaturas.length) {
            temperaturas[cantidad] = t;
            cantidad++;
        } else {
            System.out.println("Ya no hay espacio en el arreglo.");
        }
    }

    // Hace una copia del arreglo para no perder el orden original
    private Temperatura[] copiarArreglo() {
        Temperatura[] copia = new Temperatura[cantidad];
        for (int i = 0; i < cantidad; i++) {
            copia[i] = temperaturas[i];
        }
        return copia;
    }

    // Bubble sort de menor a mayor
    // Va comparando pares de vecinos y si están al revés los intercambia.
    // En cada vuelta el más grande "sube" hasta el final, como una burbuja.
    public Temperatura[] ordenarAscendente() {
        Temperatura[] arr = copiarArreglo();
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            boolean huboCambio = false;

            // los últimos i ya quedaron en su lugar, por eso n - 1 - i
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j].getGrados() > arr[j + 1].getGrados()) {
                    intercambiar(arr, j, j + 1);
                    huboCambio = true;
                }
            }

            // si en una vuelta no se cambió nada, ya está ordenado
            if (!huboCambio) {
                break;
            }
        }
        return arr;
    }

    // Bubble sort de mayor a menor
    // Es igual que el de arriba, solo cambia el signo de la comparación (<)
    public Temperatura[] ordenarDescendente() {
        Temperatura[] arr = copiarArreglo();
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            boolean huboCambio = false;

            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j].getGrados() < arr[j + 1].getGrados()) {
                    intercambiar(arr, j, j + 1);
                    huboCambio = true;
                }
            }

            if (!huboCambio) {
                break;
            }
        }
        return arr;
    }

    // Cambia de lugar dos elementos del arreglo usando una variable auxiliar
    private void intercambiar(Temperatura[] arr, int a, int b) {
        Temperatura aux = arr[a];
        arr[a] = arr[b];
        arr[b] = aux;
    }

    // Imprime un arreglo de temperaturas con un título
    public void mostrar(String titulo, Temperatura[] arr) {
        System.out.println("--- " + titulo + " ---");
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        System.out.println();
    }

    // Imprime las temperaturas en el orden en que se registraron
    public void mostrarOriginal() {
        mostrar("Temperaturas registradas (orden original)", copiarArreglo());
    }
}
