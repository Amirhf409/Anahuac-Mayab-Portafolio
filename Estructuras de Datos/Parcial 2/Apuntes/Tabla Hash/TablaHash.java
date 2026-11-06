import java.util.Scanner;

/**
 * Apuntes 06/11/2026 - Tabla Hash
 * Guarda números de empleados en un arreglo de 10 posiciones
 * usando la función hash h(x) = x mod 10.
 *
 * Si dos números caen en la misma posición (colisión),
 * el número se guarda en la siguiente posición libre.
 *
 * @author Amir Moisés Hernández Farah
 */
public class TablaHash {

    int[] tabla;
    int tamano = 10;

    // Inicializa el arreglo. -1 significa que la posición está vacía
    public TablaHash() {
        tabla = new int[tamano];
        for (int i = 0; i < tamano; i++) {
            tabla[i] = -1;
        }
    }

    // Función hash: h(x) = x mod 10
    public int hash(int x) {
        return x % tamano;
    }

    public void insertar(int x) {
        int pos = hash(x);
        int intentos = 0;

        // Si la posición está ocupada, pasamos a la siguiente
        while (tabla[pos] != -1 && intentos < tamano) {
            System.out.println("  Colisión: la posición " + pos + " ya está ocupada por " + tabla[pos]);
            pos = (pos + 1) % tamano; // el % hace que después del 9 regrese al 0
            intentos++;
        }

        // Si ya revisamos las 10 posiciones, la tabla está llena
        if (intentos == tamano) {
            System.out.println("  La tabla está llena, no se pudo guardar " + x);
        } else {
            tabla[pos] = x;
            System.out.println("  " + x + " -> h(" + x + ") = " + x + " mod 10 = " + hash(x) + " -> se guardó en la posición " + pos);
        }
    }

    public void mostrar() {
        System.out.println("\nPosición | Valor");
        System.out.println("---------+-------");
        for (int i = 0; i < tamano; i++) {
            if (tabla[i] == -1) {
                System.out.println("    " + i + "    | vacía");
            } else {
                System.out.println("    " + i + "    | " + tabla[i]);
            }
        }
    }

    // Busca un número empezando en la posición que da la función hash
    public int buscar(int x) {
        int pos = hash(x);
        int intentos = 0;

        while (tabla[pos] != -1 && intentos < tamano) {
            if (tabla[pos] == x) {
                return pos; // lo encontramos
            }
            pos = (pos + 1) % tamano; // pudo haberse movido por una colisión
            intentos++;
        }
        return -1; // llegamos a una casilla vacía: no existe
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TablaHash empleados = new TablaHash();

        System.out.println("=== TABLA HASH DE EMPLEADOS ===");
        System.out.println("Función hash: h(x) = x mod 10");
        System.out.println("Valores sugeridos: 25, 18, 42, 38, 13, 27\n");

        System.out.print("¿Cuántos números vas a guardar? (máximo 10): ");
        int n = sc.nextInt();
        while (n < 1 || n > 10) {
            System.out.print("Escribe un número del 1 al 10: ");
            n = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            System.out.print("Número de empleado " + (i + 1) + ": ");
            int num = sc.nextInt();
            empleados.insertar(num);
        }

        empleados.mostrar();

        // Búsqueda: se repite hasta que el usuario escriba -1
        System.out.print("\nNúmero a buscar (-1 para salir): ");
        int buscado = sc.nextInt();
        while (buscado != -1) {
            int pos = empleados.buscar(buscado);
            if (pos != -1) {
                System.out.println("El empleado " + buscado + " está en la posición " + pos);
            } else {
                System.out.println("El empleado " + buscado + " no está registrado");
            }
            System.out.print("\nNúmero a buscar (-1 para salir): ");
            buscado = sc.nextInt();
        }

        System.out.println("Fin del programa.");
        sc.close();
    }
}
