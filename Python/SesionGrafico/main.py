from importlib.resources import simple
from ClaseUsuario import Usuario
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw() #Oculta la ventana principal solo veremos cuadros de dialogo

# Creación del objeto
# nombreObjeto = nombreClase()
maestra = Usuario()

maestra.nombre = simpledialog.askstring("Maestra", "Ingrese su nombre: ")
maestra.apellidos = simpledialog.askstring("Maestra", "Ingrese sus apellidos: ")
maestra.edad = simpledialog.askinteger("Maestra", "Ingrese su edad: ")

messagebox.showinfo("Maestra", maestra.iniciarSesion())
messagebox.showinfo("Maestra", maestra.hacerReporte())
messagebox.showinfo("Maestra", maestra.cerrarSesion())

"""
alumno = Usuario("Tom", "Cruise", 64)
# Asignar valores a los atributos
maestra.nombre = "Lizbeth"
maestra.apellidos = "Hernandez Olan"
maestra.edad = 42

# Llamada (invocación) de métodos
maestra.iniciarSesion()
maestra.cerrarSesion()
maestra.hacerReporte()

print()

alumno.iniciarSesion()
alumno.cerrarSesion()
alumno.hacerReporte()"""