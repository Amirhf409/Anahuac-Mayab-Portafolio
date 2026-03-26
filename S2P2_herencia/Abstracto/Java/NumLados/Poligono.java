package S2P2_herencia.Abstracto.Java.NumLados;

public abstract class Poligono {
    protected int numLados;

    public void setNumLados(int n) {
        this.numLados = n > 0 ? n : 0;
    }

    public int getNumLados() {
        return this.numLados;
    }

    public abstract double calcularArea();

    public abstract double calcularPerimetro();
}