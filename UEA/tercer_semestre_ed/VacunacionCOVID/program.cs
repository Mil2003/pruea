using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static HashSet<int> GenerarPoblacion(int total) =>
        Enumerable.Range(1, total).ToHashSet();

    static HashSet<int> GenerarMuestraAleatoria(int cantidad, int minIncl, int maxIncl, int seed)
    {
        var rnd = new Random(seed);
        var universo = Enumerable.Range(minIncl, maxIncl - minIncl + 1).ToList();
        var muestra = new HashSet<int>();

        while (muestra.Count < cantidad && universo.Count > 0)
        {
            int idx = rnd.Next(universo.Count);
            muestra.Add(universo[idx]);
            universo.RemoveAt(idx);
        }
        return muestra;
    }

    static IEnumerable<string> FormatearCiudadanos(IEnumerable<int> ids) =>
        ids.OrderBy(x => x).Select(id => $"Ciudadano {id}");

    static void ImprimirListado(string titulo, IEnumerable<int> conjunto)
    {
        var lista = FormatearCiudadanos(conjunto).ToList();
        Console.WriteLine($"\n=== {titulo} ===");
        Console.WriteLine($"Total: {lista.Count}");
        Console.WriteLine(string.Join(", ", lista));
    }

    static void Main()
    {
        const int TOTAL = 500;

        var ciudadanos = GenerarPoblacion(TOTAL);

        var pfizer = GenerarMuestraAleatoria(75, 1, TOTAL, seed: 20250823);
        var astra  = GenerarMuestraAleatoria(75, 1, TOTAL, seed: 20250824);

        var vacunadosUnion = pfizer.Union(astra);
        var noVacunados    = ciudadanos.Except(vacunadosUnion);
        var ambasDosis     = pfizer.Intersect(astra);
        var soloPfizer     = pfizer.Except(astra);
        var soloAstra      = astra.Except(pfizer);

        ImprimirListado("Ciudadanos que NO se han vacunado", noVacunados);
        ImprimirListado("Ciudadanos con AMBAS dosis", ambasDosis);
        ImprimirListado("Ciudadanos vacunados SOLO con Pfizer", soloPfizer);
        ImprimirListado("Ciudadanos vacunados SOLO con AstraZeneca", soloAstra);

        Console.WriteLine("\n--- Resumen ---");
        Console.WriteLine("Pfizer: " + pfizer.Count);
        Console.WriteLine("AstraZeneca: " + astra.Count);
        Console.WriteLine("Unión (al menos una dosis): " + vacunadosUnion.Count());
        Console.WriteLine("No vacunados: " + noVacunados.Count());
        Console.WriteLine("Ambas dosis: " + ambasDosis.Count());
    }
}
