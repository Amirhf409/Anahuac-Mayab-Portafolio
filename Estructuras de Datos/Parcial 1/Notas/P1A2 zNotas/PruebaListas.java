public class PruebaListas {
    public static void main(String args[]) {
        Listas lista = new Listas();

        lista.insertarFinal(56);
        lista.imprimir();
        System.out.println("");
        lista.insertarFinal(21);
        lista.imprimir();
        System.out.println("");
        lista.insertarFinal(99);
        lista.imprimir();
        System.out.println("");
        lista.insertarFinal("Anahuac");
        lista.imprimir();
    }

}
