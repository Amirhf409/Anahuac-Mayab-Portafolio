/**
 * Clase con las funciones de validacion del sistema de archivos.
 * Todos sus metodos son static para poder usarlos sin crear un objeto.
 * Si algo esta mal, regresan el mensaje de error; si todo esta bien regresan null.
 */
public class Validador {

    // el nombre no puede estar vacio ni ser solo espacios
    public static String validarNombre(String nombre) {
        if (nombre == null || nombre.trim().isEmpty()) {
            return "ERROR: El nombre del elemento no puede estar vacio.";
        }
        return null;
    }

    // un archivo SI debe tener extension
    public static String validarExtensionArchivo(String extension) {
        if (extension == null || extension.trim().isEmpty()) {
            return "ERROR: Un archivo debe tener extension.";
        }
        return null;
    }

    // un directorio NO debe tener extension
    public static String validarExtensionDirectorio(String extension) {
        if (extension != null && !extension.trim().isEmpty()) {
            return "ERROR: Un directorio no debe tener extension.";
        }
        return null;
    }

    // el tamano de un archivo debe ser mayor o igual a cero
    public static String validarTamano(long tamano) {
        if (tamano < 0) {
            return "ERROR: El tamano de un archivo debe ser mayor o igual a cero.";
        }
        return null;
    }

    // revisa que el texto escrito sea un numero entero (para el tamano)
    public static boolean esNumero(String texto) {
        try {
            Long.parseLong(texto.trim());
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}
