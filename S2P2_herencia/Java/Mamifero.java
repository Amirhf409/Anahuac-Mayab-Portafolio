package S2P2_herencia.Java;
//Clase Padre - Clase Base - Super Clase

public class Mamifero {
    private String nombre;
    protected double peso;

    public Mamifero(String n, double p) {
        this.nombre = n;
        this.peso = p;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override // Indicar al compilador que lo vamos a sobreescribir
    public String toString() {
        return "Mamifero\n [" + nombre + "," + peso + " kg]";
    }
}
