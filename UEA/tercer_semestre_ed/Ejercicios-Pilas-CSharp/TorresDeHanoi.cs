using System;
using System.Collections.Generic;

class Torre
{
    public Stack<int> discos = new Stack<int>();
    public string nombre;

    public Torre(string nombre)
    {
        this.nombre = nombre;
    }

    public void MoverDiscoA(Torre destino)
    {
        int disco = discos.Pop();
        destino.discos.Push(disco);
        Console.WriteLine($"Mover disco {disco} desde {nombre} a {destino.nombre}");
    }
}

class TorresHanoi
{
    public static void Resolver(int n, Torre origen, Torre auxiliar, Torre destino)
    {
        if (n == 1)
        {
            origen.MoverDiscoA(destino);
        }
        else
        {
            Resolver(n - 1, origen, destino, auxiliar);
            origen.MoverDiscoA(destino);
            Resolver(n - 1, auxiliar, origen, destino);
        }
    }

    static void Main()
    {
        Console.Write("Ingrese el número de discos: ");
        int n = int.Parse(Console.ReadLine());

        Torre A = new Torre("A");
        Torre B = new Torre("B");
        Torre C = new Torre("C");

        for (int i = n; i >= 1; i--)
        {
            A.discos.Push(i);
        }

        Console.WriteLine("\n--- Movimientos ---\n");
        Resolver(n, A, B, C);
    }
}
