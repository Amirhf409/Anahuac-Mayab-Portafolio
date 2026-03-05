package S2P2_herencia.Java;

public class Gato extends Mamifero { // porque gato es una extensión de mamífero, es hija
    private int nBigotes;

    public Gato(String n, double p, int b) { // Para poder inicializar estos atributos,
        // los valores se deben ir a la clase padre Mamifero
        super(n, p); // Invoca al constructor de la clase padre
        this.nBigotes = b;
    }

    @Override
    public String toString(){
        return super.toString()+"[Bigotes:"+nBigotes+"]";
} // el super.toString() llama al toString de la clase padre y concatenamos el
  // bigotes
}
