package Java.Autor;

public class Libro {
    String titulo;
    int anioPublicacion;
    Autor autor;

    public Libro(String titulo, int anioPublicacion, Autor autor) {
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
        this.autor = autor;
    }

    @Override
    public String toString() {
        return autor + "\nTitulo: " + this.titulo + "\nAnio Publicacion: " + this.anioPublicacion;

    }
}
