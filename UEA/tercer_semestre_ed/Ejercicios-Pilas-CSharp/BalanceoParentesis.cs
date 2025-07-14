using System;
using System.Collections.Generic;

class BalanceoSimbolos
{
    // Función que verifica si los símbolos están balanceados
    public static bool EstaBalanceada(string expresion)
    {
        Stack<char> pila = new Stack<char>();

        foreach (char c in expresion)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                pila.Push(c);
            }
            else if (c == ')' || c == ']' || c == '}')
            {
                if (pila.Count == 0) return false;

                char tope = pila.Pop();

                if ((c == ')' && tope != '(') ||
                    (c == ']' && tope != '[') ||
                    (c == '}' && tope != '{'))
                {
                    return false;
                }
            }
        }

        return pila.Count == 0;
    }

    static void Main()
    {
        Console.Write("Ingrese la expresión matemática: ");
        string expresion = Console.ReadLine();

        if (EstaBalanceada(expresion))
        {
            Console.WriteLine("Fórmula balanceada.");
        }
        else
        {
            Console.WriteLine("Fórmula no balanceada.");
        }
    }
}
