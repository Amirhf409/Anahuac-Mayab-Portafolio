#include "AutoF1.h"
#include <iostream>


using namespace std;

int main() {
  int vueltas;
  double tiempo, longitud;

  cout << "--- SISTEMA DE TELEMETRIA F1 ---" << endl;

  cout << "Ingrese vueltas completadas: ";
  cin >> vueltas;

  cout << "Ingrese tiempo total (en segundos): ";
  cin >> tiempo;

  cout << "Ingrese longitud del circuito (en km): ";
  cin >> longitud;

  // Crear objeto y asignar valores
  AutoF1 autoRedBull;
  autoRedBull.setVueltasCompletadas(vueltas);
  autoRedBull.setTiempoTotalSegundos(tiempo);
  autoRedBull.setLongitudCircuitoKm(longitud);

  cout << "\n------ RESUMEN DE RENDIMIENTO ------" << endl;
  cout << "Distancia total recorrida: " << autoRedBull.calcularDistanciaTotal()
       << " km" << endl;
  cout << "Velocidad media: " << autoRedBull.calcularVelocidadMedia() << " km/h"
       << endl;
  cout << "Tiempo promedio por vuelta: "
       << autoRedBull.calcularTiempoPromedioVuelta() << " seg" << endl;

  return 0;
}