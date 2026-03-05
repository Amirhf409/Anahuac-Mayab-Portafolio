package P1A11Termometro.JAVA;

import java.util.Random;

public class Termometro {

    // Atributo
    private float temperatura;

    // Constructor por defecto
    public Termometro() {
        Random rand = new Random();
        this.temperatura = rand.nextFloat() * 100; // El random va del 0 al 100
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
        return (temperatura + 273.15f);
    }

    public void mostrartemperaturas() {
        System.out.println("Temperatura en Celcius: " + temperaturaC());
        System.out.println("Temperatura en Fahrenheit: " + temperaturaF());
        System.out.println("Temperatura en Kelvin: " + temperaturaK());
    }

}