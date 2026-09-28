import java.util.Scanner;

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

            // Conectar el nuevo nodo al padre
            if (info < anterior.info) {
                anterior.izq = nuevo;
            } else {
                anterior.der = nuevo;
            }
        }
    }

    // PREORDEN: raíz -> izquierda -> derecha
    private void preorden(Nodo reco) {
        if (reco != null) {
            System.out.print(reco.info + " ");
            preorden(reco.izq);
            preorden(reco.der);
        }
    }

    // INORDEN: izquierda -> raíz -> derecha (sale ordenado de menor a mayor)
    private void inorden(Nodo reco) {
        if (reco != null) {
            inorden(reco.izq);
            System.out.print(reco.info + " ");
            inorden(reco.der);
        }
    }

    // POSORDEN: izquierda -> derecha -> raíz
    private void posorden(Nodo reco) {
        if (reco != null) {
            posorden(reco.izq);
            posorden(reco.der);
            System.out.print(reco.info + " ");
        }
    }

    // Métodos públicos que arrancan el recorrido desde la raíz
    public void imprimirPreorden() {
        preorden(raiz);
        System.out.println();
    }

    public void imprimirInorden() {
        inorden(raiz);
        System.out.println();
    }

    public void imprimirPosorden() {
        posorden(raiz);
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArbolBinario arbol = new ArbolBinario();

        System.out.println("Ingresa los números del árbol, uno por uno.");
        System.out.println("Escribe \"fin\" para terminar de insertar.");

        while (true) {
            System.out.print("Número: ");
            String entrada = sc.next();

            // Condición para terminar de insertar
            if (entrada.equalsIgnoreCase("fin")) {
                break;
            }

            try {
                int numero = Integer.parseInt(entrada);
                arbol.insertar(numero);
            } catch (NumberFormatException e) {
                System.out.println("Eso no es un número válido, intenta de nuevo.");
            }
        }

        if (arbol.raiz == null) {
            System.out.println("El árbol está vacío, no hay nada que imprimir.");
        } else {
            System.out.print("Preorden:  ");
            arbol.imprimirPreorden();
            System.out.print("Inorden:   ");
            arbol.imprimirInorden();
            System.out.print("Posorden:  ");
            arbol.imprimirPosorden();
        }

        sc.close();
    }
}