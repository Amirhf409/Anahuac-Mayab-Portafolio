/**
 * Arbol Binario de Busqueda (ABB) que simula el sistema de archivos.
 * La raiz SIEMPRE es un Directorio y no se puede borrar.
 * Los elementos se ordenan alfabeticamente por su nombre.
 */
public class ArbolSistemaArchivos {

    // la raiz es de tipo Directorio, asi nunca puede ser un archivo
    private Directorio raiz;

    // cuantos elementos hay en total en el arbol
    private int cantidad;

    // el sistema empieza creando el directorio raiz
    public ArbolSistemaArchivos(String nombreRaiz) {
        this.raiz = new Directorio(nombreRaiz);
        this.cantidad = 1;
    }

    // ================= INSERTAR =================

    // mete un elemento nuevo al arbol siguiendo las reglas del sistema de archivos
    // regresa un mensaje diciendo si se pudo o no
    public String insertar(ElementoSistema nuevo) {
        ElementoSistema actual = raiz;

        while (true) {
            int comparacion = nuevo.compararCon(actual.getNombre());

            // regla 2: no puede haber dos elementos con el mismo nombre
            if (comparacion == 0) {
                return "ERROR: El elemento '" + nuevo.getNombre() + "' ya existe en el sistema.";
            }

            // regla 3: si llegamos a un archivo ya no podemos bajar mas
            if (!actual.puedeTenerHijos()) {
                return "ERROR: No se puede insertar el elemento.\n"
                     + "Un archivo no puede contener otros elementos.";
            }

            // regla 1 y 4: es directorio, seguimos a la izquierda o derecha
            if (comparacion < 0) {
                if (actual.getIzquierdo() == null) {
                    actual.setIzquierdo(nuevo);
                    cantidad++;
                    return "'" + nuevo.getNombre() + "' insertado como hijo izquierdo de '" + actual.getNombre() + "'.";
                }
                actual = actual.getIzquierdo();
            } else {
                if (actual.getDerecho() == null) {
                    actual.setDerecho(nuevo);
                    cantidad++;
                    return "'" + nuevo.getNombre() + "' insertado como hijo derecho de '" + actual.getNombre() + "'.";
                }
                actual = actual.getDerecho();
            }
        }
    }

    // ================= BUSCAR =================

    // busca un elemento por nombre, regresa null si no existe
    public ElementoSistema buscar(String nombre) {
        ElementoSistema actual = raiz;
        while (actual != null) {
            int comparacion = actual.compararCon(nombre);
            if (comparacion == 0) {
                return actual;
            } else if (comparacion > 0) {
                actual = actual.getIzquierdo();   // el nombre buscado va antes
            } else {
                actual = actual.getDerecho();     // el nombre buscado va despues
            }
        }
        return null;
    }

    // ================= ELIMINAR =================

    // borra un elemento usando las 3 situaciones del ABB
    // TODO: situacion 1 (hoja), situacion 2 (un hijo) y situacion 3 (dos hijos, sucesor inorden)
    // TODO: no dejar borrar la raiz
    public String eliminar(String nombre) {
        return "Opcion en desarrollo.";
    }

    // ================= RECORRIDOS =================

    // inorden: izquierda -> raiz -> derecha
    // TODO: falta hacerlo recursivo e imprimir nombre, extension, tamano y tipo
    public void inorden() {
        System.out.println("Opcion en desarrollo.");
    }

    // preorden: raiz -> izquierda -> derecha
    // TODO
    public void preorden() {
        System.out.println("Opcion en desarrollo.");
    }

    // postorden: izquierda -> derecha -> raiz
    // TODO
    public void postorden() {
        System.out.println("Opcion en desarrollo.");
    }

    // ================= OTROS =================

    public Directorio getRaiz() {
        return raiz;
    }

    public int getCantidad() {
        return cantidad;
    }
}
