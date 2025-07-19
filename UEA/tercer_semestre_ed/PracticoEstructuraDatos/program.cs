using System;
using System.Collections.Generic;

public class Atraccion
{
    private Queue<string> cola;
    private const int capacidad = 30;

    public Atraccion()
    {
        cola = new Queue<string>();
    }

    public bool AgregarPersona(string nombre)
    {
        if (cola.Count >= capacidad)
        {
            Console.WriteLine($"\n[!] No hay asientos disponibles para {nombre}.");
            return false;
        }
        cola.Enqueue(nombre);
        Console.WriteLine($"[+] {nombre} fue añadido a la cola.");
        return true;
    }

    public void IniciarAtraccion()
    {
        Console.WriteLine("\n=== Iniciando atracción ===");
        while (cola.Count > 0)
        {
            string persona = cola.Dequeue();
            Console.WriteLine($"{persona} ha ocupado un asiento.");
        }
    }

    public void MostrarCola()
    {
        Console.WriteLine("\nPersonas en la cola:");
        foreach (string persona in cola)
        {
            Console.WriteLine("- " + persona);
        }
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Atraccion atraccion = new Atraccion();

        for (int i = 1; i <= 35; i++)
        {
            atraccion.AgregarPersona("Persona" + i);
        }

        atraccion.MostrarCola();
        atraccion.IniciarAtraccion();
    }
}
