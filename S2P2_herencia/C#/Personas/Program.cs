using System;

class TestHospital
{

    public static void Main()
    {
        Persona p1 = new Persona("Emiliano", "Peniche", "Masculino", 35);
        Paciente pac1 = new Paciente("Marco", "Gomez", "Femenino", 28, 1.65, 60);
        Medico doc1 = new Medico("Rodrigo", "Quijano", "Masculino", 45, "Cardiologia", 12345);
        PacienteExterno pe1 = new PacienteExterno("Amir", "Hernandez", "Masculino", 22, 1.70, 55, 3, 10, "12/03/2026");
        PacienteHospitalizado ph1 = new PacienteHospitalizado("Luis", "Martinez", "Masculino", 50, 1.75, 80, 204, "Bypass");

        Console.WriteLine("=== PERSONA ===");
        p1.printPersona();
        Console.WriteLine("");

        Console.WriteLine("=== PACIENTE ===");
        pac1.printPaciente();
        Console.WriteLine("");

        Console.WriteLine("=== MEDICO ===");
        doc1.printMedico();
        Console.WriteLine("");

        Console.WriteLine("=== PACIENTE EXTERNO ===");
        pe1.printPacienteExterno();
        Console.WriteLine("");

        Console.WriteLine("=== PACIENTE HOSPITALIZADO ===");
        ph1.printPacienteHospitalizado();
        Console.WriteLine("");
    }
}