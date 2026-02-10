package Java.Autor;

public class Autor {
    String nombre;
    String nacionalidad;

    public Autor(String nombre, String nacionalidad) {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
    }

    @Override
    public String toString() {
        return "Nombre: " + this.nombre + "\nNacionalidad: " + this.nacionalidad;
    }

}