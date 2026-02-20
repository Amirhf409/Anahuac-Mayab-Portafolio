from termometro import Termometro

# Objeto con temperatura aleatoria
t1 = Termometro()
print("Termómetro 1 (aleatorio):")
t1.mostrar_temperaturas()

# Pedir temperatura al usuario
temp_usuario = float(input("\nIngrese una temperatura en Celsius: "))

# Objeto con valor ingresado
t2 = Termometro(temp_usuario)
print("\nTermómetro 2 (Usuario):")
t2.mostrar_temperaturas()
