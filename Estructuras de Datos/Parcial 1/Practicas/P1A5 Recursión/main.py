# Ejercicio 1: Sumatoria de n primeros números cuadrados
def sumatoria_cuadrados(n):
    if n <= 1:
        return n
    return (n ** 2) + sumatoria_cuadrados(n - 1)


# Ejercicio 2: Inversión de capital
# Estado básico (caso base): si n == 0, el capital final es el monto inicial m.
# Estado recursivo: capital(m, x, n) = capital(m, x, n - 1) * (1 + x / 100)
def calcular_capital(m, x, n):
    if n == 0:
        return m
    return calcular_capital(m, x, n - 1) * (1 + x / 100)


# Pruebas Ejercicio 1
print("--- Ejercicio 1 ---")
n1 = 3
n2 = 5

print(f"Entrada: {n1} | Salida: {sumatoria_cuadrados(n1)}")
print(f"Entrada: {n2} | Salida: {sumatoria_cuadrados(n2)}")

# Para una entrada n, el método realiza n llamadas/iteraciones recursivas antes de terminar.
print(f"Para una entrada n = {n1}, realiza {n1} iteraciones recursivas.")


# Pruebas Ejercicio 2
print("\n--- Ejercicio 2 ---")
m = 1000  # Capital inicial
x = 5     # Interés anual (%)
n = 3     # Años

resultado = calcular_capital(m, x, n)
print(f"Capital inicial (m): {m}")
print(f"Interés anual (x): {x}%")
print(f"Años (n): {n}")
print(f"Capital final: {round(resultado, 2)}")
