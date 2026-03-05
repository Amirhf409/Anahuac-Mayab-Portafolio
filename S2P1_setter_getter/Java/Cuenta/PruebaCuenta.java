import java.util.Scanner;

public class PruebaCuenta {
        public static void main(String[] args) {
                Cuenta cuenta1 = new Cuenta("Jane Green", 50.00);
                Cuenta cuenta2 = new Cuenta("John Blue", -7.53);

                // muestra el saldo inicial de cada objeto
                System.out.printf("Saldo de %s: $%.2f%n",
                                cuenta1.getNombre(), cuenta1.getSaldo());
                System.out.printf("Saldo de %s: $%.2f%n%n",
                                cuenta2.getNombre(), cuenta2.getSaldo());

                // crea un Scanner para obtener información de la ventana de comandos
                Scanner entrada = new Scanner(System.in);

                System.out.print("Ingrese el monto del deposito para la cuenta1: ");
                // indicador
                double montoDeposito = entrada.nextDouble(); // obtener la entrada del usuario
                System.out.printf("%nagregando %.2f al saldo de la cuenta1%n%n",
                                montoDeposito);
                cuenta1.deposito(montoDeposito); // agregar al saldo de la cuenta1

                // mostrar saldos
                System.out.printf("Saldo de %s: $%.2f%n",
                                cuenta1.getNombre(), cuenta1.getSaldo());
                System.out.printf("Saldo de %s: $%.2f%n%n",
                                cuenta2.getNombre(), cuenta2.getSaldo());

                System.out.print("Ingrese el monto del deposito para la cuenta2: ");
                // indicador
                montoDeposito = entrada.nextDouble(); // obtener la entrada del usuario
                System.out.printf("%nagregando %.2f al saldo de la cuenta2%n%n",
                                montoDeposito);
                cuenta2.deposito(montoDeposito); // agregar al saldo de la cuenta2

                // mostrar saldos
                System.out.printf("%s saldo: $%.2f%n",
                                cuenta1.getNombre(), cuenta1.getSaldo());
                System.out.printf("%s saldo: $%.2f%n%n",
                                cuenta2.getNombre(), cuenta2.getSaldo());
                entrada.close();
        }
}