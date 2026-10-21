/**
 * Clase Main
 * Aquí registro las temperaturas máximas de Mérida en septiembre
 * y las muestro ordenadas con bubble sort.
 *
 * @author Amir Moisés Hernández Farah
 * Periodo 202660
 */
public class Main {

    public static void main(String[] args) {

        RegistroTemperaturas merida = new RegistroTemperaturas("Mérida", 30);

        // temperaturas máximas (°C) de cada día de septiembre
        double[] grados = {
            36.8, 37.5, 38.9, 37.2, 36.4, 35.1, 34.6, 35.8, 35.2, 36.9,
            37.7, 38.6, 37.9, 36.3, 34.2, 33.8, 35.0, 36.1, 36.7, 35.5,
            34.4, 33.6, 34.9, 35.7, 36.2, 35.3, 34.1, 33.9, 34.8, 35.6
        };

        // cada posición del arreglo es un día (posición 0 = 1 sep)
        for (int i = 0; i < grados.length; i++) {
            merida.agregar(new Temperatura(grados[i], i + 1, "sep"));
        }

        System.out.println("==============================================");
        System.out.println(" TEMPERATURAS DE " + merida.getCiudad().toUpperCase() + " - SEPTIEMBRE");
        System.out.println(" Ordenamiento con Bubble Sort");
        System.out.println("==============================================");
        System.out.println("Total de registros: " + merida.getCantidad());
        System.out.println();

        merida.mostrarOriginal();
        merida.mostrar("Orden ascendente (menor a mayor)", merida.ordenarAscendente());
        merida.mostrar("Orden descendente (mayor a menor)", merida.ordenarDescendente());
    }
}
