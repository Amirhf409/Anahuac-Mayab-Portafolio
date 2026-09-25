public class ArbolBinario {

    class Nodo {
        int info;
        Nodo izq, der;
    }

    Nodo raiz;

    public ArbolBinario() {
        raiz = null;
    }

    public void insertar(int info) {
        Nodo nuevo;
        nuevo = new Nodo();
        nuevo.info = info;
        nuevo.izq = null;
        nuevo.der = null;

        // Condición para que si el árbol está vacío, el nuevo nodo será la raíz
        if (raiz == null) {
            raiz = nuevo;
        } else {
            // Para apuntar a los nodos que ya existen, reco es recorrer.
            Nodo anterior = null;
            Nodo reco = raiz;

            // Para bajar por el árbol a un lugar vacío
            while (reco != null) {
                anterior = reco; // guardar el nodo actual (el padre)
                if (info < reco.info) {
                    reco = reco.izq; // menor -> izquierda
                } else {
                    reco = reco.der; // mayor o igual -> derecha
                }
            }

            // Paso 6: conectar el nuevo nodo al padre
            if (info < anterior.info) {
                anterior.izq = nuevo;
            } else {
                anterior.der = nuevo;
            }
        }
    }

}