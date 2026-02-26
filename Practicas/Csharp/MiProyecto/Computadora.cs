public class Computadora { 
    private string marca; 
    private int memoriaRam; 
    private double precio; 
    
    //Constructor por defecto 
    public Computadora(){ 
        marca = "Desconocida"; 
        memoriaRam = 0; 
        precio = 0.0; 
    } 
    
    //Constructor parametrizado 
    public Computadora(string marca, int memoriaRam, double precio){
        this.marca = marca; 
        this.memoriaRam = memoriaRam; 
        SetPrecio(precio); //validación 
    }

    //Getter
    public double GetPrecio(){
        return precio;
    } 

    //Setter con validación
    public void SetPrecio(double p){
        if (p >= 0=)
            precio = p;
        else
            precio = 0;
    }
    
    public void MostrarInformacion(){ 
        Console.WriteLine("Marca: " + marca); 
        Console.WriteLine("Memoria RAM: " + memoriaRam); 
        Console.WriteLine("Precio : " + precio); } 

}