using System;

public class Autor {
    public string Name { get; set; }
    public string Nacionalidad { get; set; }

    public Autor(string nombre, string nacionalidad) {
        this.Name = nombre;
        this.Nacionalidad = nacionalidad;
    }

    public override string ToString() {
        return "Nombre: " + this.Name + "\nNacionalidad: " + this.Nacionalidad;
    }
}