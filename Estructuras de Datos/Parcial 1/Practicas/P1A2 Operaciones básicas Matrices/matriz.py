#Declarar 2 matrices bidimensionales:

#Tamaño variable
#Implementar las operaciones de Suma, resta, Multiplicación por 1 producto escalar.

class Matriz():

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.datos = [None] * filas
        for i in range(filas):
            self.datos[i] = [0] * columnas

    def llenar(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                mensaje = "Elemento [" + str(i) + "][" + str(j) + "]: "
                valor = int(input(mensaje))
                self.datos[i][j] = valor

    def mostrar(self):
        for i in range(self.filas):
            fila_texto = ""
            for j in range(self.columnas):
                fila_texto = fila_texto + str(self.datos[i][j]) + "\t"
            print(fila_texto)

    def sumar(self, otra):
        if self.filas != otra.filas or self.columnas != otra.columnas:
            print("No se puede sumar: las matrices no tienen el mismo tamano.")
            return None

        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                suma = self.datos[i][j] + otra.datos[i][j]
                resultado.datos[i][j] = suma
        return resultado

    def restar(self, otra):
        if self.filas != otra.filas or self.columnas != otra.columnas:
            print("No se puede restar: las matrices no tienen el mismo tamano.")
            return None

        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resta = self.datos[i][j] - otra.datos[i][j]
                resultado.datos[i][j] = resta
        return resultado

    def multiplicar_escalar(self, escalar):
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                producto = self.datos[i][j] * escalar
                resultado.datos[i][j] = producto
        return resultado