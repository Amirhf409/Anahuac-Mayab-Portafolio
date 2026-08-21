using System;

public class Juego {
    private Jugador jugador1;
    private Jugador jugador2;

    public Juego() {
        jugador1 = new Jugador("Jugador 1");
        jugador2 = new Jugador("Jugador 2");
    }

    public void iniciarJuego() {
        Console.WriteLine("Bienvenido al Juego Piedra Papel o Tijera");

        jugador1.elegir();
        jugador2.elegir();

        Console.WriteLine($"{jugador1.nombre} ha usado: {jugador1.eleccion}");
        Console.WriteLine($"{jugador2.nombre} ha usado: {jugador2.eleccion}");

        Console.WriteLine(determinarGanador());
    }

    public string determinarGanador() {
        if (jugador1.eleccion == jugador2.eleccion) {
            return "Empate";
        }

        if (
            (jugador1.eleccion == "piedra" && jugador2.eleccion == "tijera") ||
            (jugador1.eleccion == "tijera" && jugador2.eleccion == "papel") ||
            (jugador1.eleccion == "papel" && jugador2.eleccion == "piedra")
        ) {
            return "El ganador es: " + jugador1.nombre;
        }

        return "El ganador es: " + jugador2.nombre;
    }
}

public class Jugador {
    public string nombre;
    public string eleccion;

    private static Random rand = new Random();

    public Jugador(string n) {
        this.nombre = n;
    }

    public void elegir() {
        string[] opciones = { "piedra", "papel", "tijera" };
        eleccion = opciones[rand.Next(0, 3)];
    }
}