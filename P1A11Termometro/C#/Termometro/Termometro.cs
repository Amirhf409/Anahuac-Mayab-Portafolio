using System;

class Termometro {

    // Atributo
    private float temperatura;

    // Constructor por defecto
    public Termometro() {
        Random rand = new Random();
        temperatura = (float)(rand.NextDouble() * 100); // El random va del 0 al 100
    }

    // Constructor parametrizado (recibe temperatura en °C)
    public Termometro(float temperatura) {
        this.temperatura = temperatura;
    }

    // Temperatura en Celcius
    public float temperaturaC() {
        return temperatura;
    }

    // Temperatura en F
    public float temperaturaF() {
        return (temperatura * 9 / 5) + 32;
    }

    // Temperatura en K
    public float temperaturaK() {
        return temperatura + 273.15f;
    }

    public void mostrartemperaturas() {
        Console.WriteLine("Temperatura en Celcius: " + temperaturaC());
        Console.WriteLine("Temperatura en Fahrenheit: " + temperaturaF());
        Console.WriteLine("Temperatura en Kelvin: " + temperaturaK());
    }

}