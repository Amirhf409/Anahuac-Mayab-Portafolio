using System;

class Persona {
    private string nombre;
    private string apellido;
    private string genero;
    private int edad;

    public Persona() {
        this.nombre = "";
        this.apellido = "";
        this.genero = "";
        this.edad = 0;
    }

    public Persona(string n, string a, string g, int e) {
        this.nombre = n;
        this.apellido = a;
        this.genero = g;
        this.edad = e;
    }

    public string Nombre {
        get { return this.nombre; }
        set { this.nombre = value; }
    }

    public string Apellido {
        get { return this.apellido; }
        set { this.apellido = value; }
    }

    public string Genero {
        get { return this.genero; }
        set { this.genero = value; }
    }

    public int Edad {
        get { return this.edad; }
        set { this.edad = value; }
    }

    public void printPersona() {
        Console.WriteLine(nombre + " " + apellido + " - " + genero + " - " + edad + " años");
    }
}

class Paciente : Persona {
    private double altura;
    private double peso;

    public Paciente(string n, string a, string g, int e, double alt, double p) : base(n, a, g, e) {
        this.altura = alt;
        this.peso = p;
    }

    public double Altura {
        get { return this.altura; }
        set { this.altura = value; }
    }

    public double Peso {
        get { return this.peso; }
        set { this.peso = value; }
    }

    public double imc(double peso, double altura) {
        return peso / (altura * altura);
    }

    public void printPaciente() {
        printPersona();
        Console.WriteLine("Altura: " + altura);
        Console.WriteLine("Peso: " + peso);
        Console.WriteLine("IMC: " + imc(peso, altura).ToString("F2"));
    }
}

class Medico : Persona {
    private string especialidad;
    private int cedulaProfesional;

    public Medico(){
        this.especialidad = "";
        this.cedulaProfesional = 0;
    }

    public Medico(string n, string a, string g, int e, string esp, int ced) : base(n, a, g, e){
        this.especialidad = esp;
        this.cedulaProfesional = ced;
    }

    public string Especialidad {
        get { return this.especialidad; }
        set { this.especialidad = value; }
    }

    public int CedulaProfesional {
        get { return this.cedulaProfesional; }
        set { this.cedulaProfesional = value; }
    }

    public void printMedico() {
        printPersona();
        Console.WriteLine("Especialidad: " + especialidad);
        Console.WriteLine("Cedula Profesional: " + cedulaProfesional);
    }
}

class PacienteExterno : Paciente {
    private int noConsultorio;
    private int horario;
    private string fecha;

    public PacienteExterno(string n, string a, string g, int e, double alt, double p, int cons, int hor, string fec) : base(n, a, g, e, alt, p) {
        this.noConsultorio = cons;
        this.horario = hor;
        this.fecha = fec;
    }

    public int NoConsultorio {
        get { return this.noConsultorio; }
        set { this.noConsultorio = value; }
    }

    public int Horario {
        get { return this.horario; }
        set { this.horario = value; }
    }

    public string Fecha {
        get { return this.fecha; }
        set { this.fecha = value; }
    }

    public void examenFisico() {
        Console.WriteLine("Realizando examen Fisico...");
    }

    public void printPacienteExterno() {
        printPaciente();
        Console.WriteLine("Consultorio: " + noConsultorio);
        Console.WriteLine("Horario: " + horario + " hrs");
        Console.WriteLine("Fecha: " + fecha);
        examenFisico();
    }
}

class PacienteHospitalizado : Paciente {
    private int habitacion;
    private string tipoCirugia;

    public PacienteHospitalizado() : base("", "", "", 0, 0, 0) { 
        this.habitacion = 0; // Cambiado "" por 0 porque es int
        this.tipoCirugia = "";
    }

    public PacienteHospitalizado(string n, string a, string g, int e, double alt, double p, int hab, string cirugia) : base(n, a, g, e, alt, p) {
        this.habitacion = hab;
        this.tipoCirugia = cirugia;
    }

    public int Habitacion {
        get { return this.habitacion; }
        set { this.habitacion = value; }
    }

    public string TipoCirugia {
        get { return this.tipoCirugia; }
        set { this.tipoCirugia = value; }
    }

    public void indicaciones() {
        Console.WriteLine("Indicaciones para el paciente: Guardar reposo.");
    }

    public void printPacienteHospitalizado() {
        printPaciente();
        Console.WriteLine("Habitación: " + habitacion);
        Console.WriteLine("Tipo de Cirugía: " + tipoCirugia);
        indicaciones();
    }
}