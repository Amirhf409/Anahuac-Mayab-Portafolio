#include <iostream>
#include <string>
using namespace std;

class Computadora {
private:
    string marca;
    int memoriaRam;
    double precio;

public:
    //Constructor por defecto
    Computadora(){
        marca = "Desconocida";
        memoriaRam = 0;
        precio = 0.0;
    }

    //Constructor parametrizado
    Computadora(string m, int ram, double p){
        marca = m;
        memoriaRam = ram;
        setPrecio(p); //Usamos stter para validar
    }

    //getter
    double getPrecio(){
        return precio;
    }

    //Setter con validación
    void setPrecio(double p) {
        if (p >= 0)
            precio = p;
        else
        precio = 0;
    }

    void mostrarInformacion(){
        cout << "Marca: " << marca << endl;
        cout << "Memoria RAM: " << memoriaRam << endl;
        cout << "Precio: " << precio << endl;
    }
};