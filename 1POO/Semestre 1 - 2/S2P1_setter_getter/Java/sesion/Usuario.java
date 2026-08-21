package Java.sesion;

public class Usuario {

    // Atributos
    String nombre;
    String apellidos;
    int edad;

    // Constructor
    public Usuario() {
        this.nombre = "";
        this.apellidos = "";
        this.edad = 0;
    }

    // Sobrecarga de constructores
    public Usuario(String nombre, String apellidos, int edad) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.edad = edad;
    }

    // Declaración de los setter y getter
    void setNombre(String nombre) {
        this.nombre = nombre;
    }

    String getNombre() {
        return this.nombre;
    }

    void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    String getApellidos() {
        return this.apellidos;
    }

    void setEdad(int edad) {
        this.edad = edad;
    }

    int getEdad() {
        return this.edad;
    }

    // Métodos
    String iniciarSesion() {
        return ("El usuario " + this.nombre + " esta iniciando sesion.");
    }

    String cerrarSesion() {
        return ("El usuario " + this.nombre + " ha cerrado la sesion.");
    }

    String hacerReporte() {
        return ("Reporte de usuario") + ("\nNombre completo: " + this.nombre + " " + this.apellidos)
                + ("\nEdad: " + this.edad);
    }
}