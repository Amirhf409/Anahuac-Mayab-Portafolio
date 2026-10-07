// Pruebas adicionales para ArbolBinario
public class PruebasExtra {
    public static void main(String[] args) {
        String prueba = args.length > 0 ? args[0] : "1";

        if (prueba.equals("1")) {
            // PRUEBA 1: eliminar un nodo con un solo hijo
            ArbolBinario arbol = new ArbolBinario();
            arbol.insertar(50); arbol.insertar(30); arbol.insertar(20);
            arbol.insertar(40); arbol.insertar(70); arbol.insertar(60);
            arbol.insertar(80);

            System.out.println("PRUEBA 1: nodo con un solo hijo");
            System.out.print("Inorden inicial: "); arbol.inorden();

            arbol.eliminar(20);
            System.out.print("\nDespués de eliminar 20: "); arbol.inorden();
            System.out.println("\n(ahora 30 solo tiene un hijo: 40)");

            arbol.eliminar(30);
            System.out.print("Después de eliminar 30: "); arbol.inorden();
            System.out.print("\nPreorden: "); arbol.preorden();

            System.out.println("\n¿Existe 30? " + arbol.buscar(30));
            System.out.println("¿Existe 40? " + arbol.buscar(40));
        } else {
            // PRUEBA 2: otro árbol con otros números
            ArbolBinario arbol = new ArbolBinario();
            int[] numeros = {45, 15, 79, 10, 20, 90, 12};
            for (int n : numeros) arbol.insertar(n);

            System.out.println("PRUEBA 2: otro árbol (45, 15, 79, 10, 20, 90, 12)");
            System.out.print("Inorden: "); arbol.inorden();
            System.out.print("\nPreorden: "); arbol.preorden();

            System.out.println("\n¿Existe 12? " + arbol.buscar(12));
            System.out.println("¿Existe 50? " + arbol.buscar(50));

            arbol.eliminar(15);
            System.out.print("Después de eliminar 15 (dos hijos): "); arbol.inorden();
            arbol.eliminar(45);
            System.out.print("\nDespués de eliminar 45 (la raíz): "); arbol.inorden();
            System.out.println("\nNueva raíz: " + arbol.raiz.clave);
        }
    }
}
