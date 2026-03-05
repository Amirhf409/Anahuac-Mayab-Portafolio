#include <iostream>
#include "Computadora.h"

using namespace std;

int main(){
    
    //Objeto usando constructor por defecto
    Computadora c1;
    c1.mostrarInformacion();

    cout << "---------------" << endl;

    //Objeto usando constructor parametrizado
    Computadora c2("HP", 16, 15000);
    c2.mostrarInformacion();

    return 0;
}