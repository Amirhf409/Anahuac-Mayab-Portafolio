import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import java.util.ArrayList;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

/**
 * Ventana del programa (modo grafico).
 * A la izquierda se dibuja el arbol y a la derecha estan los datos y los botones.
 */
public class VentanaSistemaArchivos extends JFrame {

    private ArbolSistemaArchivos arbol;
    private PanelArbol panelArbol;

    private JTextField campoNombre;
    private JComboBox<String> comboTipo;
    private JTextField campoExtension;
    private JTextField campoTamano;
    private JTextArea areaResultado;
    private JLabel etiquetaEstado;

    public VentanaSistemaArchivos(ArbolSistemaArchivos arbol) {
        this.arbol = arbol;

        setTitle("Sistema de Archivos ABB");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));

        panelArbol = new PanelArbol(arbol);
        panelArbol.setBorder(BorderFactory.createTitledBorder("Árbol binario de búsqueda"));
        add(panelArbol, BorderLayout.CENTER);
        add(crearPanelDerecho(), BorderLayout.EAST);

        etiquetaEstado = new JLabel();
        etiquetaEstado.setBorder(BorderFactory.createEmptyBorder(0, 10, 8, 10));
        add(etiquetaEstado, BorderLayout.SOUTH);

        actualizar();
        pack();
        setLocationRelativeTo(null);   // la ventana aparece en medio de la pantalla
    }

    // ---------- armado de la ventana ----------

    private JPanel crearPanelDerecho() {
        JPanel derecho = new JPanel(new BorderLayout(0, 10));
        derecho.setBorder(BorderFactory.createEmptyBorder(10, 0, 0, 10));

        // datos del elemento
        JPanel datos = new JPanel(new GridLayout(4, 2, 5, 5));
        datos.setBorder(BorderFactory.createTitledBorder("Datos del elemento"));
        campoNombre = new JTextField(12);
        comboTipo = new JComboBox<>(new String[] {"Directorio", "Archivo"});
        campoExtension = new JTextField(12);
        campoTamano = new JTextField(12);
        datos.add(new JLabel("Nombre:"));
        datos.add(campoNombre);
        datos.add(new JLabel("Tipo:"));
        datos.add(comboTipo);
        datos.add(new JLabel("Extensión:"));
        datos.add(campoExtension);
        datos.add(new JLabel("Tamaño (bytes):"));
        datos.add(campoTamano);

        // un directorio no lleva extension ni tamano, entonces se desactivan
        comboTipo.addActionListener(e -> cambiarTipo());
        cambiarTipo();

        // botones (cada uno llama a su metodo)
        JPanel botones = new JPanel(new GridLayout(4, 2, 5, 5));
        botones.setBorder(BorderFactory.createTitledBorder("Operaciones"));
        agregarBoton(botones, "Insertar", "insertar");
        agregarBoton(botones, "Buscar", "buscar");
        agregarBoton(botones, "Eliminar", "eliminar");
        agregarBoton(botones, "Información", "informacion");
        agregarBoton(botones, "Inorden", "inorden");
        agregarBoton(botones, "Preorden", "preorden");
        agregarBoton(botones, "Postorden", "postorden");
        agregarBoton(botones, "Limpiar", "limpiar");

        JPanel arriba = new JPanel(new BorderLayout(0, 10));
        arriba.add(datos, BorderLayout.NORTH);
        arriba.add(botones, BorderLayout.CENTER);

        // area donde se muestran los mensajes y los recorridos
        areaResultado = new JTextArea(12, 42);
        areaResultado.setEditable(false);
        areaResultado.setFont(new Font("Monospaced", Font.PLAIN, 12));
        areaResultado.setLineWrap(true);         // los mensajes largos bajan de renglon
        areaResultado.setWrapStyleWord(true);
        JScrollPane scroll = new JScrollPane(areaResultado);
        scroll.setPreferredSize(new Dimension(390, 230));
        scroll.setBorder(BorderFactory.createTitledBorder("Resultado"));

        derecho.add(arriba, BorderLayout.NORTH);
        derecho.add(scroll, BorderLayout.CENTER);
        return derecho;
    }

    private void agregarBoton(JPanel panel, String texto, String accion) {
        JButton boton = new JButton(texto);
        boton.addActionListener(e -> ejecutar(accion));
        panel.add(boton);
    }

    // decide que metodo correr segun el boton que se presiono
    private void ejecutar(String accion) {
        switch (accion) {
            case "insertar": insertar(); break;
            case "buscar": buscar(); break;
            case "eliminar": eliminar(); break;
            case "informacion": informacion(); break;
            case "inorden": mostrarRecorrido("INORDEN", arbol.inorden()); break;
            case "preorden": mostrarRecorrido("PREORDEN", arbol.preorden()); break;
            case "postorden": mostrarRecorrido("POSTORDEN", arbol.postorden()); break;
            case "limpiar": limpiar(); break;
        }
    }

    private void cambiarTipo() {
        boolean esArchivo = comboTipo.getSelectedItem().equals("Archivo");
        campoExtension.setEnabled(esArchivo);
        campoTamano.setEnabled(esArchivo);
        if (!esArchivo) {
            campoExtension.setText("");
            campoTamano.setText("");
        }
    }

    // ---------- operaciones ----------

    private void insertar() {
        String nombre = campoNombre.getText().trim();
        String resultado;

        if (comboTipo.getSelectedItem().equals("Directorio")) {
            String error = Validador.validarNombreDirectorio(nombre);
            if (error != null) {
                mostrarError(error);
                return;
            }
            resultado = arbol.insertar(new Directorio(nombre));
        } else {
            String error = Validador.validarNombre(nombre);
            if (error == null) {
                error = Validador.validarExtensionArchivo(campoExtension.getText());
            }
            if (error == null && !Validador.esNumero(campoTamano.getText())) {
                error = "ERROR: El tamano debe ser un numero entero.";
            }
            if (error == null) {
                error = Validador.validarTamano(Long.parseLong(campoTamano.getText().trim()));
            }
            if (error != null) {
                mostrarError(error);
                return;
            }
            long tamano = Long.parseLong(campoTamano.getText().trim());
            resultado = arbol.insertar(new Archivo(nombre, campoExtension.getText().trim(), tamano));
        }

        mostrar(resultado);
        if (!resultado.startsWith("ERROR")) {
            campoNombre.setText("");
            campoExtension.setText("");
            campoTamano.setText("");
        }
        actualizar();
    }

    private void buscar() {
        String nombre = campoNombre.getText().trim();
        ElementoSistema encontrado = arbol.buscar(nombre);
        if (encontrado == null) {
            mostrar("El elemento no existe en el sistema de archivos.");
            panelArbol.setResaltado("");
        } else {
            mostrar("Elemento encontrado\n\n" + encontrado.informacion());
            panelArbol.setResaltado(encontrado.getNombre());
        }
    }

    private void eliminar() {
        String nombre = campoNombre.getText().trim();
        ElementoSistema elemento = arbol.buscar(nombre);

        // si es un directorio con elementos debajo, primero pedimos confirmacion
        if (elemento != null && elemento.puedeTenerHijos() && !elemento.esHoja()
                && elemento != arbol.getRaiz()) {
            int respuesta = JOptionPane.showConfirmDialog(this,
                    "El directorio '" + elemento.getNombre() + "' tiene elementos debajo.\nDesea eliminarlo?",
                    "Confirmar", JOptionPane.YES_NO_OPTION);
            if (respuesta != JOptionPane.YES_OPTION) {
                mostrar("Operacion cancelada.");
                return;
            }
        }
        mostrar(arbol.eliminar(nombre));
        panelArbol.setResaltado("");
        actualizar();
    }

    private void informacion() {
        String nombre = campoNombre.getText().trim();
        mostrar(arbol.informacionDe(nombre));
        panelArbol.setResaltado(nombre);
    }

    // muestra el recorrido como tabla: nombre, extension, tamano y tipo
    private void mostrarRecorrido(String titulo, ArrayList<ElementoSistema> lista) {
        String texto = "RECORRIDO " + titulo + "\n\n";
        texto = texto + String.format("%-15s %-6s %-10s %-10s", "Nombre", "Ext.", "Tamano", "Tipo") + "\n";
        for (ElementoSistema elemento : lista) {
            texto = texto + elemento.filaTabla() + "\n";
        }
        mostrar(texto);
    }

    private void limpiar() {
        campoNombre.setText("");
        campoExtension.setText("");
        campoTamano.setText("");
        comboTipo.setSelectedIndex(0);
        mostrar("");
        panelArbol.setResaltado("");
    }

    // ---------- apoyo ----------

    // escribe en el area de resultado y regresa el scroll al inicio
    private void mostrar(String texto) {
        areaResultado.setText(texto);
        areaResultado.setCaretPosition(0);
    }

    private void mostrarError(String mensaje) {
        JOptionPane.showMessageDialog(this, mensaje, "Error", JOptionPane.ERROR_MESSAGE);
    }

    // vuelve a dibujar el arbol y actualiza la barra de abajo
    private void actualizar() {
        etiquetaEstado.setText("Directorio raíz: " + arbol.getRaiz().getNombre()
                             + "   |   Elementos: " + arbol.getCantidad());
        panelArbol.repaint();
    }
}
