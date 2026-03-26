using System;

class Program
{
    static void Main(string[] args)
    {
        Triangulo t = new Triangulo(3, 5.0, 4.0);
        Circunferencia c = new Circunferencia(0, 3.0);

        Console.WriteLine("Triángulo:");
        Console.WriteLine("Área: " + t.calcularArea());
        Console.WriteLine("Perímetro: " + t.calcularPerimetro());

        Console.WriteLine("\nCircunferencia:");
        Console.WriteLine("Área: " + c.calcularArea());
        Console.WriteLine("Perímetro: " + c.calcularPerimetro());
    }
}