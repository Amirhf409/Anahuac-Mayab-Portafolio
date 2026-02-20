using System;

public class Test {

    public static void Main(String[] args) {

        // Objeto con constructor por defecto
        Termometro t1 = new Termometro();
        Console.WriteLine("Termómetro 1 (aleatorio):");
        t1.mostrartemperaturas();

        // Pedir temperatura al usuario
        Console.WriteLine("Ingrese una temperatura en Celcius: ");
        float tempUsuario = float.Parse(Console.ReadLine());

        // Objeto con constructor parametrizado
        Termometro t2 = new Termometro(tempUsuario);
        Console.WriteLine("Termómetro 2 (Usuario): ");
        t2.mostrartemperaturas();

    }
}