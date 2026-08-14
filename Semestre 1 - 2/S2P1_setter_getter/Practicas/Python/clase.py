class Computadora:
    def __init__(self, marca="Desconocida", memoriaRam=0, precio=0):
        self.marca = marca
        self.memoriaRam = memoriaRam
        self.setPrecio(precio) #validación

    #Getter
    def getPrecio(self):
        return self._precio

    #Setter con validación
    def setPrecio(self, p):
        if p >= 0:
            self._precio = p
        else:
            self.precio = 0
    


    def mostrarInformacion(self):
        print("Marca: " + self.marca)
        print("Memoria RAM: " + str(self.memoriaRam))
        print("Precio: " + str(self.precio))
        

