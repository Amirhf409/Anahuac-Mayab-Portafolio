using System;

public class Libro
{
    string titulo;
    int anioPublicacion;
    Autor autor;

    public Libro(string titulo, int anioPublicacion, Autor autor)
    {
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
        this.autor = autor;
    }

    public override string ToString()
    {
        return autor + "\nTitulo: " + this.titulo + "\nAnio Publicacion: " + this.anioPublicacion;
    }
}