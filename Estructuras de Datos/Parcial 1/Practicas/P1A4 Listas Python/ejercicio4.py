nombre_archivo = input('Ingresar nombre de archivo: ')
palabras_unicas = list()

archivo = open(nombre_archivo)
for linea in archivo:
    palabras = linea.split()
    for palabra in palabras:
        if palabra not in palabras_unicas:
            palabras_unicas.append(palabra)

palabras_unicas.sort()
print(palabras_unicas)