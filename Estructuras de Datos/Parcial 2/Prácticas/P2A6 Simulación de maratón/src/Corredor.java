/**
 * Clase Corredor
 * Guarda el número del corredor y su tiempo en segundos.
 *
 * @author Group 2: Amir Moisés Hernández Farah, Marco Antonio Gómez Fuentes,
 *         Emiliano Peniche Correa y Rodrigo Quijano López
 */
public class Corredor {

    private int numero;
    private int segundos;

    public Corredor(int numero, int segundos) {
        this.numero = numero;
        this.segundos = segundos;
    }

    public int getNumero() {
        return numero;
    }

    public int getSegundos() {
        return segundos;
    }

    // Convierte los segundos a min:seg (ejemplo: 245:07)
    public String getTiempo() {
        int min = segundos / 60;
        int seg = segundos % 60;
        if (seg < 10) {
            return min + ":0" + seg;
        }
        return min + ":" + seg;
    }

    @Override
    public String toString() {
        return "Corredor #" + numero + " - " + getTiempo();
    }
}
