/**
 * Representa un documento guardado en el sistema (ej. reporte.pdf).
 * Hereda de ElementoSistema. Un archivo siempre debe ser HOJA del arbol,
 * o sea, no puede tener hijos.
 */
public class Archivo extends ElementoSistema {

    // extension del archivo, ej: "pdf", "txt", "jpg"
    private String extension;

    // tamano del archivo en bytes
    private long tamano;

    public Archivo(String nombre, String extension, long tamano) {
        super(nombre);
        this.extension = extension;
        this.tamano = tamano;
    }

    @Override
    public String getTipo() {
        return "Archivo";
    }

    @Override
    public String getExtension() {
        return extension;
    }

    @Override
    public long getTamano() {
        return tamano;
    }

    // un archivo NO puede contener otros elementos
    @Override
    public boolean puedeTenerHijos() {
        return false;
    }
}
