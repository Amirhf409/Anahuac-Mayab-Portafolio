#include "Biblioteca.h"
#include <string>
using namespace std;

Autor::Autor(string nombre, string nacionalidad){
    this->nombre = nombre;
    this->nacionalidad = nacionalidad;
}

string Autor::toString(){
    return "Nombre: " + this->nombre + "\nNacionalidad: " this->nacionalidad;
}

Libro::Libro(string titulo, int anioPublicacion, Autor a): autor(a){
    this->titulo = titulo;
    this->anioPublicacion = anioPublicacion;
    //this->autor = autor;

}
string Libro::toString(){
    return this->autor.toString() + "\nTitulo: " + this->titulo + "\nAnio Publicacion: " + to_string(this->anioPublicacion);
}