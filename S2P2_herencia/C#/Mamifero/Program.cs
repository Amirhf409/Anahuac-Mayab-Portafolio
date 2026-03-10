using System;

class testMamifero
{

    public static void Main()
    {
        Gato mitch = new Gato("Mitch", 6.7, 10);
        Vaca nani = new Vaca("Nani", 350, 20);
        Ballena titi = new Ballena("Titi", 20000);

        Console.WriteLine(mitch);
        Console.WriteLine("");

        Console.WriteLine(nani);
        nani.calcularCantidadComida();
        Console.WriteLine("");

        Console.WriteLine(titi);
        Console.WriteLine("");
    }
}