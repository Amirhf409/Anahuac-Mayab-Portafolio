package Java.Autor;

public class test {
    public static void main(String args[]) {
        Autor obj = new Autor("Deitel", "Aleman");
        Libro obj2 = new Libro("Como programar en Java", 2017, obj);
        System.out.println(obj2);
    }

}
