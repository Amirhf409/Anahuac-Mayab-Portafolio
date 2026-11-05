/**
 * Representa una carpeta del sistema.
 * Hereda de ElementoSistema. Un directorio SI puede tener hijos,
 * no tiene extension y su tamano siempre es 0.
 */
public class Directorio extends ElementoSistema {

    public Directorio(String nombre) {
        super(nombre);
    }

    @Override
    public String getTipo() {
        return "Directorio";
    }

    // los directorios no tienen extension
    @Override
    public String getExtension() {
        return "-";
    }

    // el tamano de un directorio es 0 bytes
    @Override
    public long getTamano() {
        return 0;
    }

    // un directorio si puede contener otros elementos
    @Override
    public boolean puedeTenerHijos() {
        return true;
    }
}
