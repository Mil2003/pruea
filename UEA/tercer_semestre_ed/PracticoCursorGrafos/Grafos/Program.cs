using System;
using System.Collections.Generic;
using System.IO;

public class Grafo {
    private Dictionary<string, Dictionary<string, int>> listaAdy = new Dictionary<string, Dictionary<string, int>>();

    public void AgregarArista(string origen, string destino, int costo) {
        if (!listaAdy.ContainsKey(origen)) listaAdy[origen] = new Dictionary<string, int>();
        if (!listaAdy.ContainsKey(destino)) listaAdy[destino] = new Dictionary<string, int>();
        listaAdy[origen][destino] = costo;
    }

    public Dictionary<string, int> Dijkstra(string inicio) {
        var distancias = new Dictionary<string, int>();
        var pq = new SortedSet<(int, string)>();
        
        // Verificar que el nodo de inicio existe
        if (!listaAdy.ContainsKey(inicio)) {
            Console.WriteLine($"Error: El nodo '{inicio}' no existe en el grafo.");
            return distancias;
        }
        
        foreach (var nodo in listaAdy.Keys) distancias[nodo] = int.MaxValue;
        distancias[inicio] = 0;
        pq.Add((0, inicio));

        while (pq.Count > 0) {
            var (dist, u) = pq.Min; 
            pq.Remove((dist, u));
            if (dist > distancias[u]) continue;
            
            foreach (var (v, peso) in listaAdy[u]) {
                int alt = dist + peso;
                if (alt < distancias[v]) {
                    distancias[v] = alt;
                    pq.Add((alt, v));
                }
            }
        }
        return distancias;
    }

    public void ImprimirGrafo() {
        foreach (var origen in listaAdy) {
            Console.Write($"{origen.Key}: ");
            foreach (var destino in origen.Value) Console.Write($"{destino.Key}({destino.Value}) ");
            Console.WriteLine();
        }
    }
}

class Program {
    static void Main() {
        try {
            Grafo g = new Grafo();
            
            // Verificar que el archivo existe
            string archivo = "vuelos.txt";
            if (!File.Exists(archivo)) {
                Console.WriteLine($"Error: El archivo '{archivo}' no existe.");
                Console.WriteLine("Creando archivo de ejemplo...");
                CrearArchivoEjemplo(archivo);
            }
            
            string[] lineas = File.ReadAllLines(archivo);
            Console.WriteLine($"Procesando {lineas.Length} líneas del archivo...");
            
            foreach (string linea in lineas) {
                if (string.IsNullOrWhiteSpace(linea)) continue; // Saltar líneas vacías
                
                string[] partes = linea.Split(' ');
                if (partes.Length != 3) {
                    Console.WriteLine($"Error: Formato incorrecto en la línea: '{linea}'");
                    continue;
                }
                
                if (int.TryParse(partes[2], out int costo)) {
                    g.AgregarArista(partes[0], partes[1], costo);
                } else {
                    Console.WriteLine($"Error: No se pudo parsear el costo en la línea: '{linea}'");
                }
            }

            Console.WriteLine("\n=== Grafo construido ===");
            g.ImprimirGrafo();
            
            Console.WriteLine("\n=== Aplicando algoritmo de Dijkstra desde 'CiudadA' ===");
            var costos = g.Dijkstra("CiudadA");
            
            Console.WriteLine("Distancias mínimas:");
            foreach (var par in costos) {
                if (par.Value == int.MaxValue) {
                    Console.WriteLine($"{par.Key}: No alcanzable");
                } else {
                    Console.WriteLine($"{par.Key}: {par.Value}");
                }
            }
            
        } catch (Exception ex) {
            Console.WriteLine($"Error inesperado: {ex.Message}");
        }
        
        Console.WriteLine("\nPresiona cualquier tecla para salir...");
        Console.ReadKey();
    }
    
    static void CrearArchivoEjemplo(string archivo) {
        string[] lineasEjemplo = {
            "CiudadA CiudadB 4",
            "CiudadA CiudadC 2",
            "CiudadB CiudadC 1",
            "CiudadB CiudadD 5",
            "CiudadC CiudadD 8",
            "CiudadC CiudadE 10",
            "CiudadD CiudadE 2"
        };
        File.WriteAllLines(archivo, lineasEjemplo);
        Console.WriteLine($"Archivo de ejemplo '{archivo}' creado exitosamente.");
    }
}