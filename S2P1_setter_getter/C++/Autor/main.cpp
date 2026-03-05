#include <iostream>
#include "Biblioteca.h"
using namespace std;

int main(){
    Autor obj("Deitel", "Aleman");
    Libro obj2("Como programar en C++", 2020, obj);
    cout << obj2.toString();
}