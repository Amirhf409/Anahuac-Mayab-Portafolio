class Mamifero: #Clase padre - clase base - superclase
    def __init__(self, n="", p=0.0):
        self.__nombre = n #privado
        self._peso = p #protegido

    @property #getter
    def nombre(self):
        return self.__nombre

    @nombre.setter #setter
    def nombre(self, n):
        self.__nombre = n

    def __str__(self): #equivalente a toString
        return f"Mamifero\n [ {self.nombre},{self._peso} kg]"


class Gato(Mamifero):

    def __init__(self, n="", p=0.0, b=0):
        super().__init__(n, p)
        self.__nBigotes = b
        
    def __str__(self):
        return f"{super().__str__()} [Bigotes:{self.__nBigotes}]"


class Vaca(Mamifero):

    def __init__(self, n="", p=0.0, l=0.0):
        super().__init__(n, p)
        self.__litrosDeLeche = l
    
    def calcularCantidadComida(self):
        print(f"{self._peso * 0.03} kg de alimento")

    def __str__(self):
        return f"{super().__str__()} [Litros de leche:{self.__litrosDeLeche}]"


class Ballena(Mamifero):

    def __init__(self, n="", p=0.0):
        super().__init__(n, p)

    def __str__(self):
        return f"{super().__str__()}"