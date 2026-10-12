import java.util.Scanner;

/**
 * Menu interactivo en consola.
 * Se encarga de pedirle los datos al usuario, validarlos
 * y mandarlos al arbol (ArbolSistemaArchivos).
 */
public class Menu {

    private Scanner teclado;
    private ArbolSistemaArchivos arbol;

    public Menu() {
        teclado = new Scanner(System.in);
    }

    // arranca el programa: primero crea la raiz y luego muestra el menu
    public void iniciar() {
        System.out.println("========================================");
        System.out.println("        SISTEMA DE ARCHIVOS ABB");
        System.out.println("========================================");
        crearRaiz();

        int opcion;
        do {
            mostrarOpciones();
            opcion = leerEntero("Seleccione una opcion: ");
            System.out.println();
            switch (opcion) {
                case 1: crearDirectorio(); break;
                case 2: insertarArchivo(); break;
                case 3: buscarElemento(); break;
                case 4: System.out.println(arbol.eliminar("")); break;   // TODO: pedir el nombre
                case 5: arbol.inorden(); break;
                case 6: arbol.preorden(); break;
                case 7: arbol.postorden(); break;
                case 8: System.out.println("Opcion en desarrollo."); break;  // TODO: mostrar informacion
                case 0: System.out.println("Gracias por usar el Sistema de Archivos ABB. Hasta pronto!"); break;
                default: System.out.println("Opcion no valida, intente de nuevo.");
            }
            System.out.println();
        } while (opcion != 0);
    }

    // el programa debe iniciar creando un directorio raiz
    private void crearRaiz() {
        String nombre;
        do {
            nombre = leerTexto("Nombre del directorio raiz: ");
        } while (!nombreDirectorioValido(nombre));
        arbol = new ArbolSistemaArchivos(nombre.trim());
        System.out.println("Directorio raiz '" + nombre.trim() + "' creado.\n");
    }

    private void mostrarOpciones() {
        System.out.println("Directorio raiz: " + arbol.getRaiz().getNombre()
                         + "   |   Elementos: " + arbol.getCantidad());
        System.out.println("1. Crear directorio");
        System.out.println("2. Insertar archivo");
        System.out.println("3. Buscar elemento");
        System.out.println("4. Eliminar elemento");
        System.out.println("5. Recorrido inorden");
        System.out.println("6. Recorrido preorden");
        System.out.println("7. Recorrido postorden");
        System.out.println("8. Informacion de un elemento");
        System.out.println("0. Salir");
    }

    // ---------- opcion 1 ----------
    private void crearDirectorio() {
        System.out.println("=== CREAR DIRECTORIO ===");
        String nombre = leerTexto("Nombre del directorio: ");
        if (nombreDirectorioValido(nombre)) {
            System.out.println(arbol.insertar(new Directorio(nombre.trim())));
        }
    }

    // ---------- opcion 2 ----------
    private void insertarArchivo() {
        System.out.println("=== INSERTAR ARCHIVO ===");
        String nombre = leerTexto("Nombre: ");
        String error = Validador.validarNombre(nombre);
        if (error != null) {
            System.out.println(error);
            return;
        }

        String extension = leerTexto("Extension (sin punto): ");
        error = Validador.validarExtensionArchivo(extension);
        if (error != null) {
            System.out.println(error);
            return;
        }

        String textoTamano = leerTexto("Tamano (bytes): ");
        if (!Validador.esNumero(textoTamano)) {
            System.out.println("ERROR: El tamano debe ser un numero entero.");
            return;
        }
        long tamano = Long.parseLong(textoTamano.trim());
        error = Validador.validarTamano(tamano);
        if (error != null) {
            System.out.println(error);
            return;
        }

        System.out.println(arbol.insertar(new Archivo(nombre.trim(), extension.trim(), tamano)));
    }

    // ---------- opcion 3 ----------
    private void buscarElemento() {
        System.out.println("=== BUSCAR ELEMENTO ===");
        String nombre = leerTexto("Nombre a buscar: ");
        ElementoSistema encontrado = arbol.buscar(nombre.trim());
        if (encontrado == null) {
            System.out.println("El elemento no existe en el sistema de archivos.");
        } else {
            System.out.println("Elemento encontrado");
            encontrado.mostrarInformacion();
        }
    }

    // ---------- metodos de apoyo ----------

    // un directorio no puede tener nombre vacio ni extension (ej. "Fotos.jpg" no es valido)
    private boolean nombreDirectorioValido(String nombre) {
        String error = Validador.validarNombre(nombre);
        if (error == null && nombre.contains(".")) {
            String extension = nombre.substring(nombre.lastIndexOf('.') + 1);
            error = Validador.validarExtensionDirectorio(extension);
        }
        if (error != null) {
            System.out.println(error);
            return false;
        }
        return true;
    }

    private String leerTexto(String mensaje) {
        System.out.print(mensaje);
        return teclado.nextLine();
    }

    // lee un numero del menu; si escriben letras regresa -1 (opcion no valida)
    private int leerEntero(String mensaje) {
        String texto = leerTexto(mensaje);
        try {
            return Integer.parseInt(texto.trim());
        } catch (NumberFormatException e) {
            return -1;
        }
    }
}
