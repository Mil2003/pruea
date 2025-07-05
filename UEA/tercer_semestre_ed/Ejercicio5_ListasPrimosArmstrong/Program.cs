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

class Lista
{
    public Nodo cabeza;

    public void InsertarAlInicio(int valor)
    {
        Nodo nuevo = new Nodo(valor);
        nuevo.siguiente = cabeza;
        cabeza = nuevo;
    }

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

    public int Contar()
    {
        int contador = 0;
        Nodo actual = cabeza;
        while (actual != null)
        {
            contador++;
            actual = actual.siguiente;
        }
        return contador;
    }

    public void Mostrar()
    {
        Nodo actual = cabeza;
        while (actual != null)
        {
            Console.Write(actual.dato + " -> ");
            actual = actual.siguiente;
        }
        Console.WriteLine("null");
    }
}

class Programa
{
    static bool EsPrimo(int n)
    {
        if (n < 2) return false;
        for (int i = 2; i <= Math.Sqrt(n); i++)
        {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    static bool EsArmstrong(int n)
    {
        int suma = 0, temp = n;
        int digitos = n.ToString().Length;

        while (temp > 0)
        {
            int digito = temp % 10;
            suma += (int)Math.Pow(digito, digitos);
            temp /= 10;
        }

        return suma == n;
    }

    static void Main()
    {
        Lista listaPrimos = new Lista();
        Lista listaArmstrong = new Lista();

        int[] numeros = { 2, 3, 5, 10, 11, 153, 370, 371, 407, 20, 7 };

        foreach (int numero in numeros)
        {
            if (EsPrimo(numero))
                listaPrimos.InsertarAlFinal(numero);

            if (EsArmstrong(numero))
                listaArmstrong.InsertarAlInicio(numero);
        }

        Console.WriteLine("🔢 Lista de Números Primos:");
        listaPrimos.Mostrar();

        Console.WriteLine("\n💠 Lista de Números Armstrong:");
        listaArmstrong.Mostrar();

        int totalPrimos = listaPrimos.Contar();
        int totalArmstrong = listaArmstrong.Contar();

        Console.WriteLine($"\n✅ Total Primos: {totalPrimos}");
        Console.WriteLine($"✅ Total Armstrong: {totalArmstrong}");

        if (totalPrimos > totalArmstrong)
            Console.WriteLine("📣 La lista de primos tiene más elementos.");
        else if (totalPrimos < totalArmstrong)
            Console.WriteLine("📣 La lista de Armstrong tiene más elementos.");
        else
            Console.WriteLine("📣 Ambas listas tienen la misma cantidad de elementos.");
    }
}