package Java.sesion;

import javax.swing.JOptionPane; // Ventanas graficas para recibir/mostrar datos

public class Test {

    public static void main(String[] args) {
        // Crear una instancia de Usuario (Objeto)
        Usuario maestra = new Usuario();
        String no = JOptionPane.showInputDialog(null, "Ingresa el nombre", "Objeto maestra", 1);
        String ap = JOptionPane.showInputDialog(null, "Ingrese su apellido", "Objeto maestra", 1);
        int ed = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese la edad", "Objeto maestra", 1));

        // Asignar valores a los atributos
        maestra.setNombre(no);
        maestra.setApellidos(ap);
        maestra.setEdad(ed);

        // Llamar a los métodos para probarlos
        JOptionPane.showMessageDialog(null, maestra.iniciarSesion());
        JOptionPane.showMessageDialog(null, maestra.hacerReporte());
        JOptionPane.showMessageDialog(null, maestra.cerrarSesion());

        System.out.println("");

        // ----------------------- 2da parte ----------------------- //
        no = JOptionPane.showInputDialog(null, "Ingresa el nombre", "Objeto alumno", 1);
        ap = JOptionPane.showInputDialog(null, "Ingrese su apellido", "Objeto alumno", 1);
        ed = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese la edad", "Objeto alumno", 1));

        Usuario alumno = new Usuario(no, ap, ed);

        JOptionPane.showMessageDialog(null, alumno.iniciarSesion());
        JOptionPane.showMessageDialog(null, alumno.hacerReporte());
        JOptionPane.showMessageDialog(null, alumno.cerrarSesion());
    }
}