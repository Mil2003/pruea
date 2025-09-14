using System;
using System.Collections.Generic;

namespace CatalogoRevistas
{
    class Program
    {
        // Catálogo de revistas
        static List<string> catalogo = new List<string>
        {
            "National Geographic",
            "Science Today",
            "Tech World",
            "Sports Weekly",
            "Fashion Trends",
            "Health & Fitness",
            "Gaming Zone",
            "Travel Explorer",
            "Cine y Series",
            "Cocina Gourmet"
        };

        static void Main(string[] args)
        {
            int opcion;
            do
            {
                Console.WriteLine("\n=== MENÚ CATÁLOGO DE REVISTAS ===");
                Console.WriteLine("1. Ver catálogo completo");
                Console.WriteLine("2. Buscar revista");
                Console.WriteLine("3. Salir");
                Console.Write("Seleccione una opción: ");

                if (!int.TryParse(Console.ReadLine(), out opcion))
                {
                    Console.WriteLine("Opción inválida, intente de nuevo.");
                    continue;
                }

                switch (opcion)
                {
                    case 1:
                        MostrarCatalogo();
                        break;

                    case 2:
                        Console.Write("Ingrese el título a buscar: ");
                        string titulo = Console.ReadLine() ?? string.Empty;

                        // Llamada al método de búsqueda recursiva
                        bool encontrado = BuscarRevista(catalogo, titulo, 0);

                        Console.WriteLine(encontrado ? "Encontrado" : "No encontrado");
                        break;

                    case 3:
                        Console.WriteLine("Saliendo del programa...");
                        break;

                    default:
                        Console.WriteLine("Opción no válida.");
                        break;
                }
            } while (opcion != 3);
        }

        /// <summary>
        /// Muestra todos los títulos del catálogo.
        /// </summary>
        static void MostrarCatalogo()
        {
            Console.WriteLine("\n--- Catálogo de Revistas ---");
            foreach (string revista in catalogo)
            {
                Console.WriteLine("- " + revista);
            }
        }

        /// <summary>
        /// Búsqueda recursiva en la lista de revistas.
        /// </summary>
        /// <param name="lista">Lista de revistas</param>
        /// <param name="titulo">Título a buscar</param>
        /// <param name="indice">Índice actual en la recursión</param>
        /// <returns>True si se encuentra el título, false en caso contrario</returns>
        static bool BuscarRevista(List<string> lista, string titulo, int indice)
        {
            if (indice >= lista.Count)
                return false;

            if (lista[indice].Equals(titulo, StringComparison.OrdinalIgnoreCase))
                return true;

            // Llamada recursiva
            return BuscarRevista(lista, titulo, indice + 1);
        }
    }
}
