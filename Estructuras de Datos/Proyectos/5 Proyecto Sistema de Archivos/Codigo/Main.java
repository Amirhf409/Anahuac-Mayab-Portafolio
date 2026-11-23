import javax.swing.JOptionPane;
import javax.swing.UIManager;

/**
 * Clase principal. Pide el nombre del directorio raiz y abre la ventana.
 * Proyecto: Sistema de Archivos con Arbol Binario de Busqueda (ABB)
 * Materia: Estructuras de Datos - Universidad Anahuac Mayab
 * Para correrlo: java Main   (la version de consola es: java MainConsola)
 */
public class Main {
    public static void main(String[] args) {
        // botones de los mensajes en espanol
        UIManager.put("OptionPane.yesButtonText", "Sí");
        UIManager.put("OptionPane.noButtonText", "No");
        UIManager.put("OptionPane.cancelButtonText", "Cancelar");
        UIManager.put("OptionPane.okButtonText", "Aceptar");

        String nombre = "";
        String error = "inicio";

        // el programa debe iniciar creando el directorio raiz (se repite hasta que sea valido)
        while (error != null) {
            nombre = JOptionPane.showInputDialog(null, "Nombre del directorio raíz:",
                                                 "Sistema de Archivos ABB", JOptionPane.QUESTION_MESSAGE);
            if (nombre == null) {
                return;   // el usuario le dio Cancelar
            }
            error = Validador.validarNombreDirectorio(nombre);
            if (error != null) {
                JOptionPane.showMessageDialog(null, error, "Error", JOptionPane.ERROR_MESSAGE);
            }
        }

        ArbolSistemaArchivos arbol = new ArbolSistemaArchivos(nombre.trim());
        VentanaSistemaArchivos ventana = new VentanaSistemaArchivos(arbol);
        ventana.setVisible(true);
    }
}
