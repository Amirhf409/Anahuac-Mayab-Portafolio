using System;

public class Test {
    public static void Main() {
        Autor obj = new Autor("Deitel", "Aleman");
        Libro obj2 = new Libro("Programacion en Java", 2017, obj);
        Console.WriteLine(obj2);
    }
}