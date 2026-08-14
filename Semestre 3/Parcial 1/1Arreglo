import numpy as np 
import random

arreglo = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
vector = np.array(arreglo) #siempre poner el array para convertir la lista en un arreglo

asientodisponible = None #ningún asiento disponible

for i in range(len(vector)):
    if vector[i] == 0:
        asientodisponible = i + 1
        break

print(f"El cliente debe sentarse en el asiento número {asientodisponible}")