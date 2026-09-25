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
        // Paso 1: crear el nuevo nodo
        Nodo nuevo;
        nuevo = new Nodo();
        nuevo.info = info;
        nuevo.izq = null;
        nuevo.der = null;

        // Paso 2: si el árbol está vacío, el nuevo nodo es la raíz
        if (raiz == null) {
            raiz = nuevo;
        } else {
            // Paso 3: referencias auxiliares, empezando desde la raíz
            Nodo anterior = null;
            Nodo reco = raiz;

            // Pasos 4 y 5: bajar por el árbol hasta encontrar un lugar vacío
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