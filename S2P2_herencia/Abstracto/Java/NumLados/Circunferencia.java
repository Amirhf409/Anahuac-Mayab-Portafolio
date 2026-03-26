package S2P2_herencia.Abstracto.Java.NumLados;

public class Circunferencia extends Poligono {
    protected double radio;

    public Circunferencia(int nLados, double radio) {
        this.numLados = nLados;
        this.radio = radio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * this.radio * this.radio;
    }

    @Override
    public double calcularPerimetro() {
        return 2 * Math.PI * this.radio;
    }
}