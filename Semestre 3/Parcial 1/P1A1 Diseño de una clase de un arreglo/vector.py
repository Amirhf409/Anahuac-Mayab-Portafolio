class Vector():

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = [None] * capacidad  
        self.tamano = 0                  

    
    def seleccion_numero(self):
        for i in range(self.capacidad):
            numero = int(input("Ingresa un numero entero: "))
            self.datos[i] = numero
            self.tamano += 1

    
    def recorrer(self):
        if self.tamano == 0:
            print("El vector esta vacio.")
            return
        print("Vector: [", end=" ")
        for i in range(self.tamano):
            print(self.datos[i], end=" ")
        print("]")

    
    def insertar(self, valor, indice):
        if self.tamano >= self.capacidad:
            print("No se puede insertar: vector lleno.")
            return False
        if indice < 0 or indice > self.tamano:
            print("Indice invalido para insertar.")
            return False

        
        i = self.tamano
        while i > indice:
            self.datos[i] = self.datos[i - 1]
            i -= 1

        self.datos[indice] = valor
        self.tamano += 1
        return True

    
    def eliminar(self, indice):
        if self.tamano == 0:
            print("No se puede eliminar: vector vacio.")
            return False
        if indice < 0 or indice >= self.tamano:
            print("Indice invalido para eliminar.")
            return False

        
        for i in range(indice, self.tamano - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.tamano - 1] = None
        self.tamano -= 1
        return True

    
    def ordenar_ascendente(self):
        for i in range(self.tamano - 1):
            if self.datos[i] > self.datos[i + 1]:
                j = i
                while j >= 0 and self.datos[j] > self.datos[j + 1]:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux
                    j -= 1

    
    def ordenar_descendente(self):
        for i in range(self.tamano - 1):
            if self.datos[i] < self.datos[i + 1]:
                j = i
                while j >= 0 and self.datos[j] < self.datos[j + 1]:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux
                    j -= 1

    
    def buscar(self, valor):
        for i in range(self.tamano):
            if self.datos[i] == valor:
                return i
        return -1