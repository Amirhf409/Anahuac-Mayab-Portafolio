// Clase Nodo
class Nodo {
    int clave;
    Nodo izquierdo, derecho;

    public Nodo(int elemento) {
        clave = elemento;
        izquierdo = derecho = null;
    }
}

public class ArbolBinario {
    Nodo raiz;

    public ArbolBinario() { raiz = null; }

    // INSERCIÓN
    public void insertar(int clave) {
        raiz = insertarRec(raiz, clave);
    }

    private Nodo insertarRec(Nodo raiz, int clave) {
        if (raiz == null) return new Nodo(clave);
        if (clave < raiz.clave)
            raiz.izquierdo = insertarRec(raiz.izquierdo, clave);
        else if (clave > raiz.clave)
            raiz.derecho = insertarRec(raiz.derecho, clave);
        return raiz;
    }

    // RECORRIDOS
    public void inorden() { inordenRec(raiz); }
    private void inordenRec(Nodo raiz) {
        if (raiz != null) {
            inordenRec(raiz.izquierdo);
            System.out.print(raiz.clave + " ");
            inordenRec(raiz.derecho);
        }
    }

    public void preorden() { preordenRec(raiz); }
    private void preordenRec(Nodo raiz) {
        if (raiz != null) {
            System.out.print(raiz.clave + " ");
            preordenRec(raiz.izquierdo);
            preordenRec(raiz.derecho);
        }
    }

    public void postorden() { postordenRec(raiz); }
    private void postordenRec(Nodo raiz) {
        if (raiz != null) {
            postordenRec(raiz.izquierdo);
            postordenRec(raiz.derecho);
            System.out.print(raiz.clave + " ");
        }
    }

    // BÚSQUEDA: ACTIVIDAD 1
    public boolean buscar(int clave) {
        return buscarRec(raiz, clave);
    }

    private boolean buscarRec(Nodo raiz, int clave) {
        // Caso 1: llegamos a un lugar vacío, la clave no está
        if (raiz == null) return false;

        // Caso 2: la clave es la del nodo actual
        if (clave == raiz.clave) return true;

        // Caso 3: si es menor buscamos a la izquierda, si es mayor a la derecha
        if (clave < raiz.clave)
            return buscarRec(raiz.izquierdo, clave);
        else
            return buscarRec(raiz.derecho, clave);
    }

    // ELIMINACIÓN: ACTIVIDAD 2
    public void eliminar(int clave) {
        raiz = eliminarRec(raiz, clave);
    }

    private Nodo eliminarRec(Nodo raiz, int clave) {
        // Si llegamos a null, la clave no existe y no se cambia nada
        if (raiz == null) return null;

        // Primero buscamos el nodo
        if (clave < raiz.clave) {
            raiz.izquierdo = eliminarRec(raiz.izquierdo, clave);
        } else if (clave > raiz.clave) {
            raiz.derecho = eliminarRec(raiz.derecho, clave);
        } else {
            // Lo encontramos

            // Caso 1 y 2: es hoja o tiene un solo hijo
            // (si es hoja, los dos son null y se regresa null)
            if (raiz.izquierdo == null) return raiz.derecho;
            if (raiz.derecho == null) return raiz.izquierdo;

            // Caso 3: tiene dos hijos
            // Se copia el menor valor del subárbol derecho
            raiz.clave = minimo(raiz.derecho);
            // y se elimina ese valor de su lugar original
            raiz.derecho = eliminarRec(raiz.derecho, raiz.clave);
        }
        return raiz;
    }

    // ACTIVIDAD 3: método auxiliar
    // El menor valor siempre está lo más a la izquierda posible
    private int minimo(Nodo raiz) {
        while (raiz.izquierdo != null) {
            raiz = raiz.izquierdo;
        }
        return raiz.clave;
    }

    public static void main(String[] args) {
        ArbolBinario arbol = new ArbolBinario();
        arbol.insertar(50); arbol.insertar(30); arbol.insertar(20);
        arbol.insertar(40); arbol.insertar(70); arbol.insertar(60);
        arbol.insertar(80);

        System.out.println("Inorden:"); arbol.inorden();
        System.out.println("\nPreorden:"); arbol.preorden();
        System.out.println("\nPostorden:"); arbol.postorden();

        int claveBuscada = 40;
        System.out.println("\n\nBÚSQUEDA");
        if (arbol.buscar(claveBuscada))
            System.out.println("La clave " + claveBuscada + " se encontró.");
        else
            System.out.println("La clave " + claveBuscada + " no se encontró.");

        // Prueba extra: una clave que no existe
        claveBuscada = 90;
        if (arbol.buscar(claveBuscada))
            System.out.println("La clave " + claveBuscada + " se encontró.");
        else
            System.out.println("La clave " + claveBuscada + " no se encontró.");

        System.out.println("\nELIMINACIÓN");
        int nodo = 20; arbol.eliminar(nodo);
        System.out.println("Después de eliminar " + nodo); arbol.inorden();
        nodo = 70; arbol.eliminar(nodo);
        System.out.println("\nDespués de eliminar " + nodo); arbol.inorden();
        nodo = 50; arbol.eliminar(nodo);
        System.out.println("\nDespués de eliminar " + nodo); arbol.inorden();

        // Prueba extra: eliminar una clave que no existe
        nodo = 100; arbol.eliminar(nodo);
        System.out.println("\nDespués de eliminar " + nodo + " (no existe)"); arbol.inorden();

        System.out.println("\nNueva raíz: " + arbol.raiz.clave);
    }
}
