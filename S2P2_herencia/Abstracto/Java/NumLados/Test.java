package S2P2_herencia.Abstracto.Java.NumLados;

public class Test {
    public static void main(String[] args) {

        Triangulo t = new Triangulo(3, 5.0, 4.0);
        Circunferencia c = new Circunferencia(0, 3.0);

        System.out.println("Triángulo:");
        System.out.println("Área: " + t.calcularArea());
        System.out.println("Perímetro: " + t.calcularPerimetro());

        System.out.println("\nCircunferencia:");
        System.out.println("Área: " + c.calcularArea());
        System.out.println("Perímetro: " + c.calcularPerimetro());
    }
}