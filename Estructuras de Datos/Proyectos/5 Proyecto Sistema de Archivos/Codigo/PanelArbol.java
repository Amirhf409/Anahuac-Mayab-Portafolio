import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.util.ArrayList;
import javax.swing.JPanel;

/**
 * Panel que dibuja el arbol binario de busqueda.
 * Cada nodo se pone a lo ancho segun su lugar en el recorrido inorden
 * (asi quedan en orden alfabetico y nunca se enciman) y a lo alto segun su nivel.
 * Los directorios se pintan amarillos y los archivos azules.
 * El elemento que se busca se marca con borde naranja.
 */
public class PanelArbol extends JPanel {

    private static final int ANCHO = 84;     // tamano de cada caja
    private static final int ALTO = 28;
    private static final int NIVEL = 70;     // distancia entre un nivel y el siguiente

    private ArbolSistemaArchivos arbol;
    private String resaltado = "";           // nombre del elemento a marcar
    private ArrayList<ElementoSistema> ordenInorden;

    public PanelArbol(ArbolSistemaArchivos arbol) {
        this.arbol = arbol;
        setBackground(Color.WHITE);
        setPreferredSize(new Dimension(780, 430));
    }

    public void setResaltado(String nombre) {
        resaltado = nombre;
        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setFont(new Font("Arial", Font.PLAIN, 12));
        ordenInorden = arbol.inorden();
        dibujarNodo(g, arbol.getRaiz(), 1);
    }

    // posicion horizontal: el lugar del nodo en el inorden reparte el ancho del panel
    private int posicionX(ElementoSistema nodo) {
        int lugar = ordenInorden.indexOf(nodo) + 1;
        return lugar * getWidth() / (ordenInorden.size() + 1);
    }

    // posicion vertical: cada nivel baja un poco mas
    private int posicionY(int nivel) {
        return 20 + nivel * NIVEL - NIVEL / 2;
    }

    // dibuja un nodo y despues, de forma recursiva, a sus hijos
    private void dibujarNodo(Graphics g, ElementoSistema nodo, int nivel) {
        if (nodo == null) {
            return;
        }
        int x = posicionX(nodo);
        int y = posicionY(nivel);

        // primero las lineas hacia los hijos, para que queden debajo de las cajas
        g.setColor(Color.GRAY);
        if (nodo.getIzquierdo() != null) {
            g.drawLine(x, y, posicionX(nodo.getIzquierdo()), posicionY(nivel + 1));
            dibujarNodo(g, nodo.getIzquierdo(), nivel + 1);
        }
        if (nodo.getDerecho() != null) {
            g.drawLine(x, y, posicionX(nodo.getDerecho()), posicionY(nivel + 1));
            dibujarNodo(g, nodo.getDerecho(), nivel + 1);
        }

        // caja del nodo
        if (nodo.puedeTenerHijos()) {
            g.setColor(new Color(255, 236, 179));   // directorio
        } else {
            g.setColor(new Color(204, 229, 255));   // archivo
        }
        g.fillRect(x - ANCHO / 2, y - ALTO / 2, ANCHO, ALTO);

        if (nodo.getNombre().equalsIgnoreCase(resaltado)) {
            g.setColor(new Color(230, 120, 0));
            g.drawRect(x - ANCHO / 2 - 1, y - ALTO / 2 - 1, ANCHO + 2, ALTO + 2);
            g.drawRect(x - ANCHO / 2 - 2, y - ALTO / 2 - 2, ANCHO + 4, ALTO + 4);
        } else {
            g.setColor(Color.darkGray);
            g.drawRect(x - ANCHO / 2, y - ALTO / 2, ANCHO, ALTO);
        }

        // texto: los archivos muestran su extension
        String texto = nodo.getNombre();
        if (!nodo.puedeTenerHijos()) {
            texto = texto + "." + nodo.getExtension();
        }
        int anchoTexto = g.getFontMetrics().stringWidth(texto);
        g.setColor(Color.BLACK);
        g.drawString(texto, x - anchoTexto / 2, y + 5);
    }
}
