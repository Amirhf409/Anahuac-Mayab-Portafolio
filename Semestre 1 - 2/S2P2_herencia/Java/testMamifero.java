package S2P2_herencia.Java;

public class testMamifero {
    public static void main(String args[]) {
        Gato mitch = new Gato("Mitch", 6.7, 10);
        Vaca nani = new Vaca("nani", 350, 20);
        Ballena titi = new Ballena("Titi", 20000);

        System.out.println(mitch);
        System.out.println("");

        System.out.println(nani);
        nani.calcularCantidadComida();
        System.out.println("");

        System.out.println(titi);
        System.out.println("");
    }
}
