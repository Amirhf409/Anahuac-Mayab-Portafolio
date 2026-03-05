#pragma once
#include <string>
using namespace std;

class Autor{
public:
    string nombre;
    string nacionalidad;

    Autor(string nombre, string nacionalidad);
    string toString();
};

class Libro {
public:
    string titulo;
    int anioPublicacion;
    Autor autor; //Atributo que es un objeto de la clase Autor

    Libro(string titulo, int anioPublicacion, Autor a);
    string toString();
};
