// Nueva clase: TrabajadorPiezas
// Representa a un empleado que cobra por pieza producida

public class TrabajadorPiezas : Empleado {
    private double salarioPorPieza; // pago por cada pieza
    private int piezas; // número de piezas producidas

    // constructor
    public TrabajadorPiezas(string nombre, string apellido, string nss,
            double salarioPorPieza, int piezas)
        : base(nombre, apellido, nss)
    {
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
    public override double Ingresos() {
        return salarioPorPieza * piezas;
    }

    // toString
    public override string ToString() {
        return string.Format(
                "trabajador por piezas: {0}\n{1}: {2:C2}; {3}: {4}",
                base.ToString(),
                "salario por pieza", obtenerSalarioPorPieza(),
                "piezas producidas", obtenerPiezas());
    }
}