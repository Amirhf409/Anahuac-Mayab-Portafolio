import random

class Termometro:

    def __init__(self, temperatura=None):
        if temperatura is None:
            self.temperatura = random.uniform(0, 100)
        else:
            self.temperatura = temperatura

    def temperatura_c(self):
        return self.temperatura

    def temperatura_f(self):
        return (self.temperatura * 9/5) + 32

    def temperatura_k(self):
        return self.temperatura + 273.15

    def mostrar_temperaturas(self):
        print("Temperatura en Celsius:", self.temperatura_c())
        print("Temperatura en Fahrenheit:", self.temperatura_f())
        print("Temperatura en Kelvin:", self.temperatura_k())
