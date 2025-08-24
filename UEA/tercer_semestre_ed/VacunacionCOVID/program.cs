using System;
using System.Collections.Generic;
using System.Linq;

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

const int TOTAL = 500;

// Universo de ciudadanos
var ciudadanos = GenerarPoblacion(TOTAL);

// Fijamos semillas para reproducibilidad del resultado
var pfizer = GenerarMuestraAleatoria(75, 1, TOTAL, seed: 20250823);
var astra  = GenerarMuestraAleatoria(75, 1, TOTAL, seed: 20250824);

// Operaciones de conjuntos
var vacunadosUnion      = pfizer.Union(astra);             // A ∪ B
var noVacunados         = ciudadanos.Except(vacunadosUnion); // U \ (A ∪ B)
var ambasDosis          = pfizer.Intersect(astra);         // A ∩ B
var soloPfizer          = pfizer.Except(astra);            // A \ B
var soloAstra           = astra.Except(pfizer);            // B \ A

void ImprimirListado(string titulo, IEnumerable<int> conjunto)
{
    var lista = FormatearCiudadanos(conjunto).ToList();
    Console.WriteLine($"\n=== {titulo} ===");
    Console.WriteLine($"Total: {lista.Count}");
    Console.WriteLine(string.Join(", ", lista));
}

// Salida solicitada
ImprimirListado("Ciudadanos que NO se han vacunado", noVacunados);
ImprimirListado("Ciudadanos con AMBAS dosis (aparición en ambos conjuntos)", ambasDosis);
ImprimirListado("Ciudadanos vacunados SOLO con Pfizer", soloPfizer);
ImprimirListado("Ciudadanos vacunados SOLO con AstraZeneca", soloAstra);

// (Opcional) Resumen rápido
Console.WriteLine("\n--- Resumen ---");
Console.WriteLine($"Pfizer: {pfizer.Count}, AstraZeneca: {astra.Count}, Unión (al menos una dosis): {vacunadosUnion.Count}, No vacunados: {noVacunados.Count}, Ambas dosis: {ambasDosis.Count}");
