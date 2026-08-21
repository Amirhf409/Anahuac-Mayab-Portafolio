// Nueva clase: TrabajadorPiezas
// Representa a un empleado que cobra por pieza producida

public class TrabajadorPiezas extends Empleado {
    private double salarioPorPieza; // pago por cada pieza
    private int piezas; // número de piezas producidas

    // constructor
    public TrabajadorPiezas(String nombre, String apellido, String nss,
            double salarioPorPieza, int piezas) {
        super(nombre, apellido, nss);
        establecerSalarioPorPieza(salarioPorPieza);
        establecerPiezas(piezas);
    }

    // establecer salario por pieza
    public void establecerSalarioPorPieza(double salario) {
        salarioPorPieza = (salario < 0.0) ? 0.0 : salario;
    }

    // obtener salario por pieza
    public double obtenerSalarioPorPieza() {
        return salarioPorPieza;
    }

    // establecer piezas producidas
    public void establecerPiezas(int piezasProducidas) {
        piezas = (piezasProducidas < 0) ? 0 : piezasProducidas;
    }

    // obtener piezas producidas
    public int obtenerPiezas() {
        return piezas;
    }

    // implementar método abstracto ingresos
    @Override
    public double ingresos() {
        return salarioPorPieza * piezas;
    }

    // toString
    @Override
    public String toString() {
        return String.format(
                "trabajador por piezas: %s\n%s: $%,.2f; %s: %d",
                super.toString(),
                "salario por pieza", obtenerSalarioPorPieza(),
                "piezas producidas", obtenerPiezas());
    }
}