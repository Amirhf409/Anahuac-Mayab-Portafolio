package Practicas.Java;

public class Computadora {

    private String marca;
    private int memoriaRam;
    private double precio;

    // Constructor por defecto
    public Computadora() {
        marca = "Desconocida";
        memoriaRam = 0;
        precio = 0.0;
    }

    // Constructor parametrizado
    public Computadora(String marca, int memoriaRam, double precio) {
        this.marca = marca;
        this.memoriaRam = memoriaRam;
        setPrecio(precio);
        ;
    }

    // Getter
    public double getPrecio() {
        return precio;
    }

    // Setter con validación
    public void setPrecio(double p) {
        if (p >= 0)
            precio = p;
        else
            precio = 0;
    }

    public void mostrarInformacion() {
        System.out.println("Marca: " + marca);
        System.out.println("Memoria RAM: " + memoriaRam);
        System.out.println("Precio: " + precio);
    }
}