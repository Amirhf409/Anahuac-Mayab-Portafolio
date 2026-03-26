using System;

public abstract class Poligono
{
    protected int numLados;

    public void setNumLados(int n)
    {
        this.numLados = n > 0 ? n : 0;
    }

    public int getNumLados()
    {
        return this.numLados;
    }

    public abstract double calcularArea();
    public abstract double calcularPerimetro();
}

// ---------------- TRIANGULO ----------------

public class Triangulo : Poligono
{
    protected double baseT, altura;

    public Triangulo(int nLados, double baseT, double altura)
    {
        this.numLados = nLados;
        this.baseT = baseT;
        this.altura = altura;
    }

    public override double calcularArea()
    {
        return this.baseT * this.altura / 2.0;
    }

    public override double calcularPerimetro()
    {
        return 3 * this.baseT;
    }
}

// ---------------- CIRCUNFERENCIA ----------------

public class Circunferencia : Poligono
{
    protected double radio;

    public Circunferencia(int nLados, double radio)
    {
        this.numLados = nLados;
        this.radio = radio;
    }

    public override double calcularArea()
    {
        return Math.PI * this.radio * this.radio;
    }

    public override double calcularPerimetro()
    {
        return 2 * Math.PI * this.radio;
    }
}