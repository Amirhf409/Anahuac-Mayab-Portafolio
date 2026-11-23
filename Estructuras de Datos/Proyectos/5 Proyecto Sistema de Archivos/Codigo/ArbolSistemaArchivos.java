import java.util.ArrayList;

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
    // regresa un mensaje que dice que se borro y que situacion se aplico
    public String eliminar(String nombre) {
        if (raiz.compararCon(nombre) == 0) {
            return "ERROR: No se puede eliminar el directorio raiz.";
        }

        // buscamos el nodo a borrar y guardamos quien es su padre
        ElementoSistema padre = null;
        ElementoSistema actual = raiz;
        while (actual != null && actual.compararCon(nombre) != 0) {
            padre = actual;
            if (actual.compararCon(nombre) > 0) {
                actual = actual.getIzquierdo();
            } else {
                actual = actual.getDerecho();
            }
        }
        if (actual == null) {
            return "El elemento no existe en el sistema de archivos.";
        }

        ElementoSistema reemplazo;
        String situacion;

        if (actual.esHoja()) {
            // situacion 1: no tiene hijos, solo se quita
            reemplazo = null;
            situacion = "situacion 1: nodo hoja";
        } else if (actual.getIzquierdo() == null || actual.getDerecho() == null) {
            // situacion 2: su unico hijo sube a su lugar
            if (actual.getIzquierdo() != null) {
                reemplazo = actual.getIzquierdo();
            } else {
                reemplazo = actual.getDerecho();
            }
            situacion = "situacion 2: nodo con un hijo";
        } else {
            // situacion 3: lo reemplaza el sucesor inorden (o el predecesor)
            reemplazo = tomarSucesor(actual);
            if (reemplazo == null) {
                reemplazo = tomarPredecesor(actual);
            }
            if (reemplazo == null) {
                return "ERROR: No se puede eliminar '" + actual.getNombre() + "'.\n"
                     + "El elemento que tomaria su lugar es un archivo y un archivo no puede tener elementos debajo.";
            }
            situacion = "situacion 3: nodo con dos hijos, lo reemplazo '" + reemplazo.getNombre() + "'";
        }

        // el padre ahora apunta al reemplazo en lugar del nodo borrado
        if (padre.getIzquierdo() == actual) {
            padre.setIzquierdo(reemplazo);
        } else {
            padre.setDerecho(reemplazo);
        }
        cantidad--;
        return "'" + actual.getNombre() + "' eliminado (" + situacion + ").";
    }

    // sucesor inorden: el menor del lado derecho
    // solo se usa si es directorio, porque va a quedar con dos hijos
    private ElementoSistema tomarSucesor(ElementoSistema nodo) {
        ElementoSistema padreSucesor = nodo;
        ElementoSistema sucesor = nodo.getDerecho();
        while (sucesor.getIzquierdo() != null) {
            padreSucesor = sucesor;
            sucesor = sucesor.getIzquierdo();
        }
        if (!sucesor.puedeTenerHijos()) {
            return null;
        }
        // lo sacamos de donde estaba y le pasamos los hijos del nodo borrado
        if (padreSucesor != nodo) {
            padreSucesor.setIzquierdo(sucesor.getDerecho());
            sucesor.setDerecho(nodo.getDerecho());
        }
        sucesor.setIzquierdo(nodo.getIzquierdo());
        return sucesor;
    }

    // predecesor inorden: el mayor del lado izquierdo (se usa si el sucesor es archivo)
    private ElementoSistema tomarPredecesor(ElementoSistema nodo) {
        ElementoSistema padrePredecesor = nodo;
        ElementoSistema predecesor = nodo.getIzquierdo();
        while (predecesor.getDerecho() != null) {
            padrePredecesor = predecesor;
            predecesor = predecesor.getDerecho();
        }
        if (!predecesor.puedeTenerHijos()) {
            return null;
        }
        if (padrePredecesor != nodo) {
            padrePredecesor.setDerecho(predecesor.getIzquierdo());
            predecesor.setIzquierdo(nodo.getIzquierdo());
        }
        predecesor.setDerecho(nodo.getDerecho());
        return predecesor;
    }

    // ================= RECORRIDOS =================
    // cada recorrido regresa una lista con los elementos en el orden en que se visitaron

    // inorden: izquierda -> raiz -> derecha (sale en orden alfabetico)
    public ArrayList<ElementoSistema> inorden() {
        ArrayList<ElementoSistema> lista = new ArrayList<>();
        inorden(raiz, lista);
        return lista;
    }

    private void inorden(ElementoSistema nodo, ArrayList<ElementoSistema> lista) {
        if (nodo != null) {
            inorden(nodo.getIzquierdo(), lista);
            lista.add(nodo);
            inorden(nodo.getDerecho(), lista);
        }
    }

    // preorden: raiz -> izquierda -> derecha
    public ArrayList<ElementoSistema> preorden() {
        ArrayList<ElementoSistema> lista = new ArrayList<>();
        preorden(raiz, lista);
        return lista;
    }

    private void preorden(ElementoSistema nodo, ArrayList<ElementoSistema> lista) {
        if (nodo != null) {
            lista.add(nodo);
            preorden(nodo.getIzquierdo(), lista);
            preorden(nodo.getDerecho(), lista);
        }
    }

    // postorden: izquierda -> derecha -> raiz
    public ArrayList<ElementoSistema> postorden() {
        ArrayList<ElementoSistema> lista = new ArrayList<>();
        postorden(raiz, lista);
        return lista;
    }

    private void postorden(ElementoSistema nodo, ArrayList<ElementoSistema> lista) {
        if (nodo != null) {
            postorden(nodo.getIzquierdo(), lista);
            postorden(nodo.getDerecho(), lista);
            lista.add(nodo);
        }
    }

    // ================= INFORMACION =================

    // datos del elemento, sus hijos y si es hoja
    public String informacionDe(String nombre) {
        ElementoSistema elemento = buscar(nombre);
        if (elemento == null) {
            return "El elemento no existe en el sistema de archivos.";
        }
        String texto = elemento.informacion();
        texto = texto + "\nHijo izquierdo: " + nombreDe(elemento.getIzquierdo());
        texto = texto + "\nHijo derecho: " + nombreDe(elemento.getDerecho());
        if (elemento.esHoja()) {
            texto = texto + "\nEs hoja: Si";
        } else {
            texto = texto + "\nEs hoja: No";
        }
        return texto;
    }

    private String nombreDe(ElementoSistema nodo) {
        if (nodo == null) {
            return "ninguno";
        }
        return nodo.getNombre();
    }

    // ================= OTROS =================

    public Directorio getRaiz() {
        return raiz;
    }

    public int getCantidad() {
        return cantidad;
    }
}
