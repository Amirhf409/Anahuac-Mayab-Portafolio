package P1A11Termometro.JAVA;

import java.util.Scanner;

public class Test {

    public static void main(String[] args) {

        // Objeto con constructor por defecto
        Termometro t1 = new Termometro();
        System.out.println("Termómetro 1 (aleatorio):");
        t1.mostrartemperaturas();

        // Pedir temperatura al usuario
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese una temperatura en Celcius: ");
        float tempUsuario = sc.nextFloat();

        // Objeto con constructor parametrizado
        Termometro t2 = new Termometro(tempUsuario);
        System.out.println("Termómetro 2 (Usuario): ");
        t2.mostrartemperaturas();

        sc.close();
    }
}