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

    // borra un elemento usando las 3 situaciones clasicas del ABB
    public String eliminar(String nombre) {
        // la raiz no se puede eliminar
        if (raiz.compararCon(nombre) == 0) {
            return "ERROR: No se puede eliminar el directorio raiz.";
        }

        // buscamos el nodo y tambien a su papa
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

        // Situacion 1: nodo hoja, se quita directo
        if (actual.esHoja()) {
            reemplazarEnPadre(padre, actual, null);
            cantidad--;
            return "'" + nombre + "' eliminado (situacion 1: nodo hoja).";
        }

        // Situacion 2: nodo con un solo hijo, el hijo toma su lugar
        if (actual.getIzquierdo() == null || actual.getDerecho() == null) {
            ElementoSistema hijo = (actual.getIzquierdo() != null) ? actual.getIzquierdo() : actual.getDerecho();
            reemplazarEnPadre(padre, actual, hijo);
            cantidad--;
            return "'" + nombre + "' eliminado (situacion 2: se reemplazo por su unico hijo '" + hijo.getNombre() + "').";
        }

        // Situacion 3: nodo con dos hijos
        // el que lo reemplace va a quedar con 2 hijos, asi que TIENE que ser directorio
        ElementoSistema reemplazo = quitarSucesorSiEsDirectorio(actual);
        String tipoReemplazo = "sucesor inorden";
        if (reemplazo == null) {
            reemplazo = quitarPredecesorSiEsDirectorio(actual);
            tipoReemplazo = "predecesor inorden";
        }
        if (reemplazo == null) {
            return "ERROR: No se puede eliminar '" + nombre + "'.\n"
                 + "Su sucesor y su predecesor son archivos y un archivo no puede tener hijos.";
        }

        // el reemplazo se queda con los hijos del nodo borrado
        reemplazo.setIzquierdo(actual.getIzquierdo());
        reemplazo.setDerecho(actual.getDerecho());
        reemplazarEnPadre(padre, actual, reemplazo);
        cantidad--;
        return "'" + nombre + "' eliminado (situacion 3: se reemplazo por su " + tipoReemplazo
             + " '" + reemplazo.getNombre() + "').";
    }

    // busca el sucesor inorden (el mas chico del lado derecho)
    // si es directorio lo desconecta de donde estaba y lo regresa, si es archivo regresa null
    private ElementoSistema quitarSucesorSiEsDirectorio(ElementoSistema nodo) {
        ElementoSistema padreSucesor = nodo;
        ElementoSistema sucesor = nodo.getDerecho();
        while (sucesor.getIzquierdo() != null) {
            padreSucesor = sucesor;
            sucesor = sucesor.getIzquierdo();
        }
        if (!sucesor.puedeTenerHijos()) {
            return null;
        }
        // el sucesor no tiene hijo izquierdo, su hijo derecho sube a su lugar
        if (padreSucesor == nodo) {
            nodo.setDerecho(sucesor.getDerecho());
        } else {
            padreSucesor.setIzquierdo(sucesor.getDerecho());
        }
        return sucesor;
    }

    // igual que el de arriba pero con el predecesor (el mas grande del lado izquierdo)
    private ElementoSistema quitarPredecesorSiEsDirectorio(ElementoSistema nodo) {
        ElementoSistema padrePredecesor = nodo;
        ElementoSistema predecesor = nodo.getIzquierdo();
        while (predecesor.getDerecho() != null) {
            padrePredecesor = predecesor;
            predecesor = predecesor.getDerecho();
        }
        if (!predecesor.puedeTenerHijos()) {
            return null;
        }
        if (padrePredecesor == nodo) {
            nodo.setIzquierdo(predecesor.getIzquierdo());
        } else {
            padrePredecesor.setDerecho(predecesor.getIzquierdo());
        }
        return predecesor;
    }

    // cambia el hijo "viejo" del padre por el "nuevo"
    private void reemplazarEnPadre(ElementoSistema padre, ElementoSistema viejo, ElementoSistema nuevo) {
        if (padre.getIzquierdo() == viejo) {
            padre.setIzquierdo(nuevo);
        } else {
            padre.setDerecho(nuevo);
        }
    }

    // ================= RECORRIDOS =================

    // inorden: izquierda -> raiz -> derecha (sale en orden alfabetico)
    public void inorden() {
        imprimirEncabezado();
        inorden(raiz);
    }

    private void inorden(ElementoSistema nodo) {
        if (nodo != null) {
            inorden(nodo.getIzquierdo());
            System.out.println(nodo.filaTabla());
            inorden(nodo.getDerecho());
        }
    }

    // preorden: raiz -> izquierda -> derecha
    public void preorden() {
        imprimirEncabezado();
        preorden(raiz);
    }

    private void preorden(ElementoSistema nodo) {
        if (nodo != null) {
            System.out.println(nodo.filaTabla());
            preorden(nodo.getIzquierdo());
            preorden(nodo.getDerecho());
        }
    }

    // postorden: izquierda -> derecha -> raiz
    public void postorden() {
        imprimirEncabezado();
        postorden(raiz);
    }

    private void postorden(ElementoSistema nodo) {
        if (nodo != null) {
            postorden(nodo.getIzquierdo());
            postorden(nodo.getDerecho());
            System.out.println(nodo.filaTabla());
        }
    }

    // encabezado de la tabla que sale en los recorridos
    private void imprimirEncabezado() {
        System.out.println(String.format("%-15s %-6s %-10s %-10s", "Nombre", "Ext", "Tamano", "Tipo"));
        System.out.println("---------------------------------------------");
    }

    // ================= OTROS =================

    // cuenta cuantos elementos hay debajo de un nodo (sin contarlo a el)
    public int contarDescendientes(ElementoSistema nodo) {
        return contarNodos(nodo.getIzquierdo()) + contarNodos(nodo.getDerecho());
    }

    private int contarNodos(ElementoSistema nodo) {
        if (nodo == null) {
            return 0;
        }
        return 1 + contarNodos(nodo.getIzquierdo()) + contarNodos(nodo.getDerecho());
    }

    // dibuja el arbol acostado (la raiz a la izquierda, el lado derecho arriba)
    public void mostrarEstructura() {
        mostrarEstructura(raiz, 0);
    }

    private void mostrarEstructura(ElementoSistema nodo, int nivel) {
        if (nodo != null) {
            mostrarEstructura(nodo.getDerecho(), nivel + 1);
            String espacios = "      ".repeat(nivel);
            String etiqueta = nodo.puedeTenerHijos() ? "[" + nodo.getNombre() + "]"
                                                      : nodo.getNombre() + "." + nodo.getExtension();
            System.out.println(espacios + etiqueta);
            mostrarEstructura(nodo.getIzquierdo(), nivel + 1);
        }
    }

    public Directorio getRaiz() {
        return raiz;
    }

    public int getCantidad() {
        return cantidad;
    }
}
