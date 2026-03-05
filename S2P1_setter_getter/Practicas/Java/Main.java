package Practicas.Java;

public class Main {
    public static void main(String[] args) {

        // Constructor por defecto
        Computadora c1 = new Computadora();
        c1.mostrarInformacion();

        System.out.println("------------");

        // Constructor parametrizado
        Computadora c2 = new Computadora("Lenovo", 16, 18000);
        c2.mostrarInformacion();
    }

}
