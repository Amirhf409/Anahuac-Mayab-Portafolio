package S2P2_herencia.Java;

public class Vaca extends Mamifero {
    private double litrosDeLeche;

    public Vaca(String n, double p, double l) {
        super(n, p);
        this.litrosDeLeche = l;
    }

    public void calcularCantidadComida() {
        System.out.println(super.peso * 0.03 + " kg de alimento");
    }

    @Override
    public String toString() {
        return super.toString() + "[Litros de Leche:" + litrosDeLeche + "]";
    }
}
