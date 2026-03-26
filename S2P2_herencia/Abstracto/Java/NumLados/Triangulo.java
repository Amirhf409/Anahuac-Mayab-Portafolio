package S2P2_herencia.Abstracto.Java.NumLados;

public class Triangulo extends Poligono {
    protected double base, altura;

    public Triangulo(int nLados, double base, double altura) {
        this.numLados = nLados;
        this.base = base;
        this.altura = altura;
    }

    @Override
    public double calcularArea() {
        return this.base * this.altura / 2.0;
    }

    @Override
    public double calcularPerimetro() {
        return 3 * this.base;
    }

    public static void main(String[] args) {
        Triangulo tr1 = new Triangulo(3, 2.0, 2.82);
    }
}
