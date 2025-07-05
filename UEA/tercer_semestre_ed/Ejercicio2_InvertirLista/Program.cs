using System;

class Nodo
{
    public int dato;
    public Nodo siguiente;

    public Nodo(int valor)
    {
        dato = valor;
        siguiente = null;
    }
}

class ListaEnlazada
{
    private Nodo cabeza;

    public void InsertarAlFinal(int valor)
    {
        Nodo nuevo = new Nodo(valor);
        if (cabeza == null)
        {
            cabeza = nuevo;
        }
        else
        {
            Nodo actual = cabeza;
            while (actual.siguiente != null)
            {
                actual = actual.siguiente;
            }
            actual.siguiente = nuevo;
        }
    }

    public void Mostrar()
    {
        Nodo actual = cabeza;
        Console.WriteLine("Lista:");
        while (actual != null)
        {
            Console.Write(actual.dato + " -> ");
            actual = actual.siguiente;
        }
        Console.WriteLine("null");
    }

    public void Invertir()
    {
        Nodo anterior = null;
        Nodo actual = cabeza;
        Nodo siguiente = null;

        while (actual != null)
        {
            siguiente = actual.siguiente;
            actual.siguiente = anterior;
            anterior = actual;
            actual = siguiente;
        }

        cabeza = anterior;
    }
}

class Programa
{
    static void Main()
    {
        ListaEnlazada lista = new ListaEnlazada();

        lista.InsertarAlFinal(10);
        lista.InsertarAlFinal(20);
        lista.InsertarAlFinal(30);
        lista.InsertarAlFinal(40);

        Console.WriteLine("Lista original:");
        lista.Mostrar();

        lista.Invertir();
        Console.WriteLine("\nLista invertida:");
        lista.Mostrar();
    }
}