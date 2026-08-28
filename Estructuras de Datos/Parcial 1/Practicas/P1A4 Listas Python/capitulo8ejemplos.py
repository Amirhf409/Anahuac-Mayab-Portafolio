"""
P1A4 - Listas en Python
Basado en el Capitulo 8 "Listas" - Python para Todos (py4e)
Ejemplos recreados con valores propios.
"""

# 8.1 Una lista es una secuencia
resistencias = [220, 330, 1000, 4700]
componentes = ['resistencia', 'capacitor', 'led']
vacia = []
print(resistencias, componentes, vacia)

mezcla = ['multimetro', 2.5, 10, [5, 12]]
print(mezcla)

# 8.2 Las listas son mutables
print(componentes[0])
pesos_gym = [15, 20]
pesos_gym[1] = 25
print(pesos_gym)
print('led' in componentes)
print('transistor' in componentes)

# 8.3 Recorriendo una lista
for componente in componentes:
    print(componente)

for i in range(len(resistencias)):
    resistencias[i] = resistencias[i] * 2
print(resistencias)

# 8.4 Operaciones de listas (+ y *)
dia1 = ['biceps', 'triceps']
dia2 = ['espalda', 'hombro']
rutina_semana = dia1 + dia2
print(rutina_semana)
print([12] * 4)

# 8.5 Rebanado de listas
dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
print(dias[1:3])
print(dias[:4])
print(dias[3:])
print(dias[:])
dias[1:3] = ['martes-cardio', 'miercoles-piernas']
print(dias)

# 8.6 Metodos de listas
herramientas = ['pinza', 'cautin', 'estano']
herramientas.append('multimetro')
print(herramientas)

extra = ['cinta_aislante', 'protoboard']
herramientas.extend(extra)
print(herramientas)

alumnos = ['Diego', 'Ana', 'Bruno', 'Carla']
alumnos.sort()
print(alumnos)

# 8.7 Eliminando elementos
serie = ['R1', 'R2', 'R3']
eliminado = serie.pop(1)
print(serie, eliminado)

serie2 = ['C1', 'C2', 'C3']
del serie2[1]
print(serie2)

serie3 = ['D1', 'D2', 'D3']
serie3.remove('D2')
print(serie3)

serie4 = ['a', 'b', 'c', 'd', 'e', 'f']
del serie4[1:5]
print(serie4)

# 8.8 Listas y funciones internas
calificaciones = [85, 92, 78, 90, 88, 95]
print(len(calificaciones))
print(max(calificaciones))
print(min(calificaciones))
print(sum(calificaciones))
print(sum(calificaciones) / len(calificaciones))

# 8.9 Listas y cadenas
letras = list('ohmios')
print(letras)

frase = 'el capacitor almacena carga electrica'
palabras = frase.split()
print(palabras)
print(palabras[2])

codigo = 'R1-R2-R3'
print(codigo.split('-'))

lista_palabras = ['el', 'led', 'enciende', 'rapido']
print(' '.join(lista_palabras))

# 8.11 Objetos y valores
x = 'protoboard'
y = 'protoboard'
print(x is y)

lista_x = [1, 2, 3]
lista_y = [1, 2, 3]
print(lista_x is lista_y)

# 8.12 Alias
original = [10, 20, 30]
alias = original
print(alias is original)
alias[0] = 999
print(original)

# 8.13 Listas como argumentos
def remover_primero(t):
    del t[0]

def cola(t):
    return t[1:]

valores_sensor = [23.5, 24.1, 24.8]
remover_primero(valores_sensor)
print(valores_sensor)

valores_sensor2 = [23.5, 24.1, 24.8]
resto = cola(valores_sensor2)
print(valores_sensor2, resto)