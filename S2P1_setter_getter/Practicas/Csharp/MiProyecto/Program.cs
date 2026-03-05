using System;

class Program{

    static void Main(string[] args){

        //Constructor por defecto
        Computadora c1 = new Computadora();
        c1.MostrarInformacion();

        Console.WriteLine("-------------");

        //Constructor parametrizado
        Computadora c2 = new Computadora("Dell", 32, 25000);
        c2.MostrarInformacion();
    }
}