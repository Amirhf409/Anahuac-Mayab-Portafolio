#ifndef AUTOF1_H
#define AUTOF1_H

class AutoF1 {
private:
  // Atributos
  int vueltasCompletadas;
  double tiempoTotalSegundos;
  double longitudCircuitoKm;

public:
  // Constructor
  AutoF1();

  // Setters
  void setVueltasCompletadas(int vc);
  void setTiempoTotalSegundos(double tts);
  void setLongitudCircuitoKm(double lck);

  // Getters
  int getVueltasCompletadas();
  double getTiempoTotalSegundos();
  double getLongitudCircuitoKm();

  // Métodos de cálculo
  double calcularDistanciaTotal();
  double calcularVelocidadMedia();
  double calcularTiempoPromedioVuelta();
};

#endif