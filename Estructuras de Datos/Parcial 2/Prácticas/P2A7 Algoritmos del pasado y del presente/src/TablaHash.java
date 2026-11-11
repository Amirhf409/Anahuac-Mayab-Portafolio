/**
 * Clase TablaHash
 * Guarda registros en un arreglo usando la función hash h(x) = x mod tamaño.
 * Si dos claves caen en la misma posición (colisión), el registro
 * se guarda en la siguiente posición libre.
 *
 * @author Amir Moisés Hernández Farah
 */
public class TablaHash {

    private Registro[] tabla;
    private int tamano;
    private int pasos;   // cuántas casillas revisó la última búsqueda

    public TablaHash(int tamano) {
        this.tamano = tamano;
        tabla = new Registro[tamano];   // todas empiezan en null (vacías)
    }

    // Función hash: h(x) = x mod tamaño
    public int hash(int x) {
        return x % tamano;
    }

    public void insertar(Registro r) {
        int pos = hash(r.getClave());
        // Si la posición está ocupada, pasamos a la siguiente
        while (tabla[pos] != null) {
            pos = (pos + 1) % tamano;   // el % hace que después del final regrese al 0
        }
        tabla[pos] = r;
    }

    // Busca una clave empezando en la posición que da la función hash
    public Registro buscar(int clave) {
        int pos = hash(clave);
        pasos = 0;
        while (tabla[pos] != null) {
            pasos++;
            if (tabla[pos].getClave() == clave) {
                return tabla[pos];   // lo encontramos
            }
            pos = (pos + 1) % tamano;
        }
        return null;   // llegamos a una casilla vacía, no existe
    }

    public int getPasos() {
        return pasos;
    }
}
