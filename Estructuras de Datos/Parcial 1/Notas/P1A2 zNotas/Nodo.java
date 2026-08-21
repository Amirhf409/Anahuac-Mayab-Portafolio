public class Nodo {
    Object dato; // Objet es la clase base de todas las clases de java
    Nodo siguiente;

    Nodo(Object objeto) {
        this(objeto, null);
    }

    Nodo(Object objeto, Nodo nodo) {
        dato = objeto;
        siguiente = nodo;
    }

}