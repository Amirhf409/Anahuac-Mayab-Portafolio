/**
 * Clase Temperatura
 * Guarda una temperatura registrada en Mérida y el día en que se registró.
 *
 * @author Amir Moisés Hernández Farah
 * Periodo 202660
 */
public class Temperatura {

    // Atributos
    private double grados;   // temperatura en °C
    private int dia;         // día del mes
    private String mes;      // ej: "sep"

    // Constructor vacío
    public Temperatura() {
        grados = 0;
        dia = 0;
        mes = "";
    }

    // Constructor con datos
    public Temperatura(double grados, int dia, String mes) {
        this.grados = grados;
        this.dia = dia;
        this.mes = mes;
    }

    // Getters
    public double getGrados() {
        return grados;
    }

    public int getDia() {
        return dia;
    }

    public String getMes() {
        return mes;
    }

    // Regresa la temperatura con su fecha, ej: "35.2, 9 sep"
    @Override
    public String toString() {
        return grados + ", " + dia + " " + mes;
    }
}
