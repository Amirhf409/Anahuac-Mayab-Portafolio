// Fig. 7.8: Cuenta.java
// Clase Cuenta con una variable de instancia double llamada saldo y un
// constructor además de un método llamado deposito que realiza la validación.

public class Cuenta {
    private String nombre; // variable de instancia
    private double saldo; // variable de instancia

    // Constructor de cuenta que recibe dos parámetros
    public Cuenta(String nombre, double saldo) {
        this.nombre = nombre; // asigna nombre al nombre de la variable de instancia

        // valida que el saldo sea mayor que 0.0; si no lo es, el saldo de la
        // variable de instancia mantiene su valor inicial predeterminado de 0.0
        if (saldo > 0.0) { // si el saldo es válido
            this.saldo = saldo; // asignarlo al saldo de la variable de instancia
        }
    }

    // método que deposita (agrega) sólo una cantidad válida al saldo
    public void deposito(double montoDeposito) {
        if (montoDeposito > 0.0) { // si el montoDeposito es válido
            saldo += montoDeposito; // lo agrega al saldo
        }
    }

    // el método devuelve el saldo de la cuenta
    public double getSaldo() {
        return saldo;
    }

    // método que establece el nombre
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    // método que devuelve el nombre
    public String getNombre() {
        return nombre;
    }
}
