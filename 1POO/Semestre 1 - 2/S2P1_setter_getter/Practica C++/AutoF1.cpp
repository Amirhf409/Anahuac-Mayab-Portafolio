#include "AutoF1.h"

// Constructor por defecto
AutoF1::AutoF1() {
  vueltasCompletadas = 0;
  tiempoTotalSegundos = 0.0;
  longitudCircuitoKm = 0.0;
}

// Setters
void AutoF1::setVueltasCompletadas(int vc) { vueltasCompletadas = vc; }
void AutoF1::setTiempoTotalSegundos(double tts) { tiempoTotalSegundos = tts; }
void AutoF1::setLongitudCircuitoKm(double lck) { longitudCircuitoKm = lck; }

// Getters
int AutoF1::getVueltasCompletadas() { return vueltasCompletadas; }
double AutoF1::getTiempoTotalSegundos() { return tiempoTotalSegundos; }
double AutoF1::getLongitudCircuitoKm() { return longitudCircuitoKm; }

// Cálculos
double AutoF1::calcularDistanciaTotal() {
  return vueltasCompletadas * longitudCircuitoKm;
}

double AutoF1::calcularVelocidadMedia() {
  if (tiempoTotalSegundos == 0)
    return 0;
  // Distancia total / tiempo (convertido a horas para km/h)
  double distancia = calcularDistanciaTotal();
  double tiempoHoras = tiempoTotalSegundos / 3600.0;
  return distancia / tiempoHoras;
}

double AutoF1::calcularTiempoPromedioVuelta() {
  if (vueltasCompletadas == 0)
    return 0;
  return tiempoTotalSegundos / (double)vueltasCompletadas;
}