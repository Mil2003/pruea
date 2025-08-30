using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace TraductorBasico
{
    class Program
    {
        // Diccionario principal para almacenar las traducciones
        static Dictionary<string, string> diccionarioInglesEspanol = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        static Dictionary<string, string> diccionarioEspanolIngles = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);

        static void Main(string[] args)
        {
            Console.WriteLine("=== TRADUCTOR BÁSICO INGLÉS-ESPAÑOL ===\n");
            
            // Inicializar el diccionario con palabras base
            InicializarDiccionario();
            
            bool continuar = true;
            
            while (continuar)
            {
                MostrarMenu();
                string opcion = Console.ReadLine() ?? "";
                
                switch (opcion)
                {
                    case "1":
                        TraducirFrase();
                        break;
                    case "2":
                        AgregarPalabra();
                        break;
                    case "0":
                        continuar = false;
                        Console.WriteLine("¡Gracias por usar el traductor! ¡Hasta pronto!");
                        break;
                    default:
                        Console.WriteLine("Opción no válida. Por favor, seleccione una opción del menú.\n");
                        break;
                }
                
                if (continuar)
                {
                    Console.WriteLine("\nPresione cualquier tecla para continuar...");
                    Console.ReadKey();
                    Console.Clear();
                }
            }
        }
        
        static void InicializarDiccionario()
        {
            // Agregar palabras base al diccionario
            var palabrasBase = new Dictionary<string, string>
            {
                {"time", "tiempo"},
                {"person", "persona"},
                {"year", "año"},
                {"way", "camino"},
                {"day", "día"},
                {"thing", "cosa"},
                {"man", "hombre"},
                {"world", "mundo"},
                {"life", "vida"},
                {"hand", "mano"},
                {"part", "parte"},
                {"child", "niño"},
                {"eye", "ojo"},
                {"woman", "mujer"},
                {"place", "lugar"},
                {"work", "trabajo"},
                {"week", "semana"},
                {"case", "caso"},
                {"point", "punto"},
                {"government", "gobierno"},
                {"company", "empresa"}
            };
            
            // Llenar ambos diccionarios (inglés->español y español->inglés)
            foreach (var par in palabrasBase)
            {
                diccionarioInglesEspanol[par.Key] = par.Value;
                diccionarioEspanolIngles[par.Value] = par.Key;
            }
            
            Console.WriteLine($"Diccionario inicializado con {palabrasBase.Count} palabras base.\n");
        }
        
        static void MostrarMenu()
        {
            Console.WriteLine("==================== MENÚ ====================");
            Console.WriteLine("1. Traducir una frase");
            Console.WriteLine("2. Agregar palabras al diccionario");
            Console.WriteLine("0. Salir");
            Console.Write("Seleccione una opción: ");
        }
        
        static void TraducirFrase()
        {
            Console.Clear();
            Console.WriteLine("=== TRADUCTOR DE FRASES ===\n");
            
            Console.WriteLine("Idiomas disponibles:");
            Console.WriteLine("1. Inglés a Español");
            Console.WriteLine("2. Español a Inglés");
            Console.Write("Seleccione el idioma de origen: ");
            
            string opcionIdioma = Console.ReadLine() ?? "";
            
            Console.Write("\nIngrese la frase a traducir: ");
            string frase = Console.ReadLine() ?? "";
            
            if (string.IsNullOrWhiteSpace(frase))
            {
                Console.WriteLine("No se ingresó ninguna frase.");
                return;
            }
            
            string fraseTraducida;
            int palabrasTraducidas;
            
            if (opcionIdioma == "1")
            {
                (fraseTraducida, palabrasTraducidas) = TraducirTexto(frase, diccionarioInglesEspanol);
                Console.WriteLine($"\n--- TRADUCCIÓN (Inglés → Español) ---");
            }
            else if (opcionIdioma == "2")
            {
                (fraseTraducida, palabrasTraducidas) = TraducirTexto(frase, diccionarioEspanolIngles);
                Console.WriteLine($"\n--- TRADUCCIÓN (Español → Inglés) ---");
            }
            else
            {
                Console.WriteLine("Opción de idioma no válida.");
                return;
            }
            
            Console.WriteLine($"Texto original: {frase}");
            Console.WriteLine($"Texto traducido: {fraseTraducida}");
            Console.WriteLine($"Palabras traducidas: {palabrasTraducidas}");
        }
        
        static (string textoTraducido, int palabrasTraducidas) TraducirTexto(string texto, Dictionary<string, string> diccionario)
        {
            int contador = 0;
            
            // Usar expresión regular para encontrar palabras (conservando puntuación)
            string patron = @"\b\w+\b";
            
            string resultado = Regex.Replace(texto, patron, match =>
            {
                string palabra = match.Value;
                
                if (diccionario.ContainsKey(palabra.ToLower()))
                {
                    contador++;
                    // Mantener la capitalización original
                    string traduccion = diccionario[palabra.ToLower()];
                    
                    if (char.IsUpper(palabra[0]))
                    {
                        traduccion = char.ToUpper(traduccion[0]) + traduccion.Substring(1);
                    }
                    
                    return traduccion;
                }
                
                return palabra; // Devolver la palabra original si no se encuentra traducción
            });
            
            return (resultado, contador);
        }
        
        static void AgregarPalabra()
        {
            Console.Clear();
            Console.WriteLine("=== AGREGAR PALABRAS AL DICCIONARIO ===\n");
            
            Console.Write("Ingrese la palabra en inglés: ");
            string palabraIngles = (Console.ReadLine() ?? "").Trim().ToLower();
            
            Console.Write("Ingrese la traducción en español: ");
            string palabraEspanol = (Console.ReadLine() ?? "").Trim().ToLower();
            
            if (string.IsNullOrWhiteSpace(palabraIngles) || string.IsNullOrWhiteSpace(palabraEspanol))
            {
                Console.WriteLine("Error: Debe ingresar ambas palabras.");
                return;
            }
            
            // Verificar si ya existe
            if (diccionarioInglesEspanol.ContainsKey(palabraIngles))
            {
                Console.Write($"La palabra '{palabraIngles}' ya existe con la traducción '{diccionarioInglesEspanol[palabraIngles]}'. ");
                Console.Write("¿Desea sobrescribirla? (s/n): ");
                string respuesta = (Console.ReadLine() ?? "").ToLower();
                
                if (respuesta != "s" && respuesta != "sí" && respuesta != "si")
                {
                    Console.WriteLine("Palabra no agregada.");
                    return;
                }
                
                // Eliminar la traducción anterior del diccionario inverso
                string traduccionAnterior = diccionarioInglesEspanol[palabraIngles];
                diccionarioEspanolIngles.Remove(traduccionAnterior);
            }
            
            // Agregar la nueva palabra a ambos diccionarios
            diccionarioInglesEspanol[palabraIngles] = palabraEspanol;
            diccionarioEspanolIngles[palabraEspanol] = palabraIngles;
            
            Console.WriteLine($"✓ Palabra agregada exitosamente:");
            Console.WriteLine($"  {palabraIngles} → {palabraEspanol}");
            Console.WriteLine($"Total de palabras en el diccionario: {diccionarioInglesEspanol.Count}");
        }
    }
}