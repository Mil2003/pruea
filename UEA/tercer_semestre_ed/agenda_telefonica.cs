using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text.Json;

namespace AgendaTelefonica
{
    // Clase principal para representar un contacto
    public class Contacto
    {
        public string Nombre { get; set; }
        public string Apellido { get; set; }
        public string Telefono { get; set; }
        public string Email { get; set; }
        public string Direccion { get; set; }
        public DateTime FechaCreacion { get; set; }
        
        public Contacto()
        {
            FechaCreacion = DateTime.Now;
        }
        
        public Contacto(string nombre, string apellido, string telefono, string email = "", string direccion = "")
        {
            Nombre = nombre;
            Apellido = apellido;
            Telefono = telefono;
            Email = email;
            Direccion = direccion;
            FechaCreacion = DateTime.Now;
        }
        
        public string NombreCompleto => $"{Nombre} {Apellido}";
        
        public override string ToString()
        {
            return $"Nombre: {NombreCompleto}\n" +
                   $"Teléfono: {Telefono}\n" +
                   $"Email: {Email}\n" +
                   $"Dirección: {Direccion}\n" +
                   $"Fecha de creación: {FechaCreacion:dd/MM/yyyy HH:mm}";
        }
    }
    
    // Clase para manejar la agenda con diferentes estructuras de datos
    public class AgendaTelefonica
    {
        // Vector para almacenar contactos
        private List<Contacto> contactos;
        
        // Matriz para organizar contactos por categorías (Familia, Trabajo, Amigos)
        private Dictionary<string, List<Contacto>> categorias;
        
        // Estructura para estadísticas
        public struct EstadisticasAgenda
        {
            public int TotalContactos;
            public int ContactosConEmail;
            public int ContactosConDireccion;
            public DateTime UltimaModificacion;
            public string CategoriaConMasContactos;
        }
        
        private const string ARCHIVO_DATOS = "agenda_contactos.json";
        
        public AgendaTelefonica()
        {
            contactos = new List<Contacto>();
            categorias = new Dictionary<string, List<Contacto>>
            {
                {"Familia", new List<Contacto>()},
                {"Trabajo", new List<Contacto>()},
                {"Amigos", new List<Contacto>()},
                {"Otros", new List<Contacto>()}
            };
            CargarDatos();
        }
        
        // Método para agregar contacto
        public bool AgregarContacto(Contacto contacto, string categoria = "Otros")
        {
            try
            {
                // Validar que no exista el número
                if (contactos.Any(c => c.Telefono == contacto.Telefono))
                {
                    Console.WriteLine("❌ Error: Ya existe un contacto con ese número de teléfono.");
                    return false;
                }
                
                contactos.Add(contacto);
                
                if (categorias.ContainsKey(categoria))
                {
                    categorias[categoria].Add(contacto);
                }
                else
                {
                    categorias["Otros"].Add(contacto);
                }
                
                GuardarDatos();
                Console.WriteLine("✅ Contacto agregado exitosamente.");
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Error al agregar contacto: {ex.Message}");
                return false;
            }
        }
        
        // Método para buscar contactos
        public List<Contacto> BuscarContacto(string termino)
        {
            var resultados = new List<Contacto>();
            
            foreach (var contacto in contactos)
            {
                if (contacto.Nombre.ToLower().Contains(termino.ToLower()) ||
                    contacto.Apellido.ToLower().Contains(termino.ToLower()) ||
                    contacto.Telefono.Contains(termino) ||
                    contacto.Email.ToLower().Contains(termino.ToLower()))
                {
                    resultados.Add(contacto);
                }
            }
            
            return resultados;
        }
        
        // Método para eliminar contacto
        public bool EliminarContacto(string telefono)
        {
            var contacto = contactos.FirstOrDefault(c => c.Telefono == telefono);
            if (contacto != null)
            {
                contactos.Remove(contacto);
                
                // Remover de todas las categorías
                foreach (var categoria in categorias.Values)
                {
                    categoria.Remove(contacto);
                }
                
                GuardarDatos();
                Console.WriteLine("✅ Contacto eliminado exitosamente.");
                return true;
            }
            
            Console.WriteLine("❌ No se encontró el contacto.");
            return false;
        }
        
        // Método para actualizar contacto
        public bool ActualizarContacto(string telefonoOriginal, Contacto contactoActualizado)
        {
            var contacto = contactos.FirstOrDefault(c => c.Telefono == telefonoOriginal);
            if (contacto != null)
            {
                contacto.Nombre = contactoActualizado.Nombre;
                contacto.Apellido = contactoActualizado.Apellido;
                contacto.Telefono = contactoActualizado.Telefono;
                contacto.Email = contactoActualizado.Email;
                contacto.Direccion = contactoActualizado.Direccion;
                
                GuardarDatos();
                Console.WriteLine("✅ Contacto actualizado exitosamente.");
                return true;
            }
            
            Console.WriteLine("❌ No se encontró el contacto.");
            return false;
        }
        
        // Reportería - Mostrar todos los contactos
        public void MostrarTodosLosContactos()
        {
            if (contactos.Count == 0)
            {
                Console.WriteLine("📋 No hay contactos en la agenda.");
                return;
            }
            
            Console.WriteLine("\n📋 === TODOS LOS CONTACTOS ===");
            Console.WriteLine($"Total de contactos: {contactos.Count}");
            Console.WriteLine(new string('=', 50));
            
            var contactosOrdenados = contactos.OrderBy(c => c.Apellido).ThenBy(c => c.Nombre);
            
            foreach (var contacto in contactosOrdenados)
            {
                Console.WriteLine(contacto);
                Console.WriteLine(new string('-', 30));
            }
        }
        
        // Reportería - Mostrar contactos por categoría
        public void MostrarContactosPorCategoria(string categoria)
        {
            if (!categorias.ContainsKey(categoria))
            {
                Console.WriteLine("❌ Categoría no válida.");
                return;
            }
            
            var contactosCategoria = categorias[categoria];
            
            Console.WriteLine($"\n📂 === CONTACTOS - {categoria.ToUpper()} ===");
            Console.WriteLine($"Total en esta categoría: {contactosCategoria.Count}");
            Console.WriteLine(new string('=', 50));
            
            if (contactosCategoria.Count == 0)
            {
                Console.WriteLine("No hay contactos en esta categoría.");
                return;
            }
            
            foreach (var contacto in contactosCategoria.OrderBy(c => c.Apellido))
            {
                Console.WriteLine(contacto);
                Console.WriteLine(new string('-', 30));
            }
        }
        
        // Reportería - Estadísticas
        public EstadisticasAgenda ObtenerEstadisticas()
        {
            var stats = new EstadisticasAgenda
            {
                TotalContactos = contactos.Count,
                ContactosConEmail = contactos.Count(c => !string.IsNullOrEmpty(c.Email)),
                ContactosConDireccion = contactos.Count(c => !string.IsNullOrEmpty(c.Direccion)),
                UltimaModificacion = contactos.Any() ? contactos.Max(c => c.FechaCreacion) : DateTime.MinValue,
                CategoriaConMasContactos = categorias.OrderByDescending(c => c.Value.Count).First().Key
            };
            
            return stats;
        }
        
        // Método para mostrar estadísticas
        public void MostrarEstadisticas()
        {
            var stats = ObtenerEstadisticas();
            
            Console.WriteLine("\n📊 === ESTADÍSTICAS DE LA AGENDA ===");
            Console.WriteLine($"Total de contactos: {stats.TotalContactos}");
            Console.WriteLine($"Contactos con email: {stats.ContactosConEmail}");
            Console.WriteLine($"Contactos con dirección: {stats.ContactosConDireccion}");
            Console.WriteLine($"Categoría con más contactos: {stats.CategoriaConMasContactos}");
            
            if (stats.UltimaModificacion != DateTime.MinValue)
            {
                Console.WriteLine($"Última modificación: {stats.UltimaModificacion:dd/MM/yyyy HH:mm}");
            }
            
            Console.WriteLine("\n📂 Contactos por categoría:");
            foreach (var categoria in categorias)
            {
                Console.WriteLine($"  • {categoria.Key}: {categoria.Value.Count} contactos");
            }
        }
        
        // Persistencia de datos
        private void GuardarDatos()
        {
            try
            {
                var json = JsonSerializer.Serialize(contactos, new JsonSerializerOptions { WriteIndented = true });
                File.WriteAllText(ARCHIVO_DATOS, json);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Error al guardar datos: {ex.Message}");
            }
        }
        
        private void CargarDatos()
        {
            try
            {
                if (File.Exists(ARCHIVO_DATOS))
                {
                    var json = File.ReadAllText(ARCHIVO_DATOS);
                    var contactosCargados = JsonSerializer.Deserialize<List<Contacto>>(json);
                    
                    if (contactosCargados != null)
                    {
                        contactos = contactosCargados;
                        
                        // Reorganizar en categorías (simplificado para este ejemplo)
                        foreach (var categoria in categorias.Keys.ToList())
                        {
                            categorias[categoria].Clear();
                        }
                        
                        // Asignar aleatoriamente a categorías para demostración
                        var random = new Random();
                        var categoriasKeys = categorias.Keys.ToArray();
                        
                        foreach (var contacto in contactos)
                        {
                            var categoriaAleatoria = categoriasKeys[random.Next(categoriasKeys.Length)];
                            categorias[categoriaAleatoria].Add(contacto);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"❌ Error al cargar datos: {ex.Message}");
            }
        }
        
        // Método para obtener todas las categorías
        public string[] ObtenerCategorias()
        {
            return categorias.Keys.ToArray();
        }
    }
    
    // Clase principal del programa
    public class Program
    {
        private static AgendaTelefonica agenda;
        
        public static void Main(string[] args)
        {
            Console.WriteLine("📱 === AGENDA TELEFÓNICA ===");
            Console.WriteLine("Desarrollado por: Milton Manuel Mosquera Quiñones");
            Console.WriteLine("Universidad Estatal Amazónica - Tecnologías de la Información");
            Console.WriteLine(new string('=', 60));
            
            agenda = new AgendaTelefonica();
            
            // Agregar algunos contactos de ejemplo si la agenda está vacía
            InicializarDatosEjemplo();
            
            MostrarMenu();
        }
        
        private static void InicializarDatosEjemplo()
        {
            // Verificar si ya hay contactos
            var stats = agenda.ObtenerEstadisticas();
            if (stats.TotalContactos == 0)
            {
                Console.WriteLine("🔄 Inicializando con datos de ejemplo...");
                
                agenda.AgregarContacto(new Contacto("María", "González", "0987654321", "maria.gonzalez@email.com", "Av. Amazonas 123"), "Familia");
                agenda.AgregarContacto(new Contacto("Carlos", "Rodríguez", "0976543210", "carlos.rodriguez@empresa.com", "Calle 10 de Agosto 456"), "Trabajo");
                agenda.AgregarContacto(new Contacto("Ana", "Martínez", "0965432109", "ana.martinez@gmail.com"), "Amigos");
                agenda.AgregarContacto(new Contacto("Luis", "Pérez", "0954321098", "luis.perez@outlook.com", "Barrio La Floresta"), "Otros");
                
                Console.WriteLine("✅ Datos de ejemplo agregados.\n");
            }
        }
        
        private static void MostrarMenu()
        {
            int opcion;
            
            do
            {
                Console.WriteLine("\n📋 === MENÚ PRINCIPAL ===");
                Console.WriteLine("1. Agregar contacto");
                Console.WriteLine("2. Buscar contacto");
                Console.WriteLine("3. Mostrar todos los contactos");
                Console.WriteLine("4. Mostrar contactos por categoría");
                Console.WriteLine("5. Actualizar contacto");
                Console.WriteLine("6. Eliminar contacto");
                Console.WriteLine("7. Ver estadísticas");
                Console.WriteLine("0. Salir");
                Console.Write("\nSeleccione una opción: ");
                
                if (int.TryParse(Console.ReadLine(), out opcion))
                {
                    Console.Clear();
                    
                    switch (opcion)
                    {
                        case 1:
                            AgregarContacto();
                            break;
                        case 2:
                            BuscarContacto();
                            break;
                        case 3:
                            agenda.MostrarTodosLosContactos();
                            break;
                        case 4:
                            MostrarContactosPorCategoria();
                            break;
                        case 5:
                            ActualizarContacto();
                            break;
                        case 6:
                            EliminarContacto();
                            break;
                        case 7:
                            agenda.MostrarEstadisticas();
                            break;
                        case 0:
                            Console.WriteLine("👋 ¡Gracias por usar la Agenda Telefónica!");
                            break;
                        default:
                            Console.WriteLine("❌ Opción no válida.");
                            break;
                    }
                }
                else
                {
                    Console.WriteLine("❌ Por favor, ingrese un número válido.");
                }
                
                if (opcion != 0)
                {
                    Console.WriteLine("\nPresione cualquier tecla para continuar...");
                    Console.ReadKey();
                    Console.Clear();
                }
                
            } while (opcion != 0);
        }
        
        private static void AgregarContacto()
        {
            Console.WriteLine("➕ === AGREGAR NUEVO CONTACTO ===");
            
            Console.Write("Nombre: ");
            string nombre = Console.ReadLine();
            
            Console.Write("Apellido: ");
            string apellido = Console.ReadLine();
            
            Console.Write("Teléfono: ");
            string telefono = Console.ReadLine();
            
            Console.Write("Email (opcional): ");
            string email = Console.ReadLine();
            
            Console.Write("Dirección (opcional): ");
            string direccion = Console.ReadLine();
            
            Console.WriteLine("\nCategorías disponibles:");
            var categorias = agenda.ObtenerCategorias();
            for (int i = 0; i < categorias.Length; i++)
            {
                Console.WriteLine($"{i + 1}. {categorias[i]}");
            }
            
            Console.Write("Seleccione categoría (número): ");
            if (int.TryParse(Console.ReadLine(), out int categoriaIndex) && 
                categoriaIndex > 0 && categoriaIndex <= categorias.Length)
            {
                var contacto = new Contacto(nombre, apellido, telefono, email, direccion);
                agenda.AgregarContacto(contacto, categorias[categoriaIndex - 1]);
            }
            else
            {
                var contacto = new Contacto(nombre, apellido, telefono, email, direccion);
                agenda.AgregarContacto(contacto, "Otros");
            }
        }
        
        private static void BuscarContacto()
        {
            Console.WriteLine("🔍 === BUSCAR CONTACTO ===");
            Console.Write("Ingrese término de búsqueda (nombre, apellido, teléfono o email): ");
            string termino = Console.ReadLine();
            
            var resultados = agenda.BuscarContacto(termino);
            
            if (resultados.Count == 0)
            {
                Console.WriteLine("❌ No se encontraron contactos con ese término.");
            }
            else
            {
                Console.WriteLine($"\n✅ Se encontraron {resultados.Count} contacto(s):");
                Console.WriteLine(new string('=', 50));
                
                foreach (var contacto in resultados)
                {
                    Console.WriteLine(contacto);
                    Console.WriteLine(new string('-', 30));
                }
            }
        }
        
        private static void MostrarContactosPorCategoria()
        {
            Console.WriteLine("📂 === CONTACTOS POR CATEGORÍA ===");
            var categorias = agenda.ObtenerCategorias();
            
            Console.WriteLine("Categorías disponibles:");
            for (int i = 0; i < categorias.Length; i++)
            {
                Console.WriteLine($"{i + 1}. {categorias[i]}");
            }
            
            Console.Write("Seleccione categoría (número): ");
            if (int.TryParse(Console.ReadLine(), out int categoriaIndex) && 
                categoriaIndex > 0 && categoriaIndex <= categorias.Length)
            {
                agenda.MostrarContactosPorCategoria(categorias[categoriaIndex - 1]);
            }
            else
            {
                Console.WriteLine("❌ Categoría no válida.");
            }
        }
        
        private static void ActualizarContacto()
        {
            Console.WriteLine("✏️ === ACTUALIZAR CONTACTO ===");
            Console.Write("Ingrese el teléfono del contacto a actualizar: ");
            string telefonoOriginal = Console.ReadLine();
            
            var contactos = agenda.BuscarContacto(telefonoOriginal);
            if (contactos.Count == 0)
            {
                Console.WriteLine("❌ No se encontró el contacto.");
                return;
            }
            
            var contactoOriginal = contactos[0];
            Console.WriteLine("\nContacto encontrado:");
            Console.WriteLine(contactoOriginal);
            
            Console.WriteLine("\nIngrese los nuevos datos (presione Enter para mantener el valor actual):");
            
            Console.Write($"Nombre [{contactoOriginal.Nombre}]: ");
            string nuevoNombre = Console.ReadLine();
            if (string.IsNullOrEmpty(nuevoNombre)) nuevoNombre = contactoOriginal.Nombre;
            
            Console.Write($"Apellido [{contactoOriginal.Apellido}]: ");
            string nuevoApellido = Console.ReadLine();
            if (string.IsNullOrEmpty(nuevoApellido)) nuevoApellido = contactoOriginal.Apellido;
            
            Console.Write($"Teléfono [{contactoOriginal.Telefono}]: ");
            string nuevoTelefono = Console.ReadLine();
            if (string.IsNullOrEmpty(nuevoTelefono)) nuevoTelefono = contactoOriginal.Telefono;
            
            Console.Write($"Email [{contactoOriginal.Email}]: ");
            string nuevoEmail = Console.ReadLine();
            if (string.IsNullOrEmpty(nuevoEmail)) nuevoEmail = contactoOriginal.Email;
            
            Console.Write($"Dirección [{contactoOriginal.Direccion}]: ");
            string nuevaDireccion = Console.ReadLine();
            if (string.IsNullOrEmpty(nuevaDireccion)) nuevaDireccion = contactoOriginal.Direccion;
            
            var contactoActualizado = new Contacto(nuevoNombre, nuevoApellido, nuevoTelefono, nuevoEmail, nuevaDireccion);
            agenda.ActualizarContacto(telefonoOriginal, contactoActualizado);
        }
        
        private static void EliminarContacto()
        {
            Console.WriteLine("🗑️ === ELIMINAR CONTACTO ===");
            Console.Write("Ingrese el teléfono del contacto a eliminar: ");
            string telefono = Console.ReadLine();
            
            var contactos = agenda.BuscarContacto(telefono);
            if (contactos.Count == 0)
            {
                Console.WriteLine("❌ No se encontró el contacto.");
                return;
            }
            
            var contacto = contactos[0];
            Console.WriteLine("\nContacto encontrado:");
            Console.WriteLine(contacto);
            
            Console.Write("\n¿Está seguro de que desea eliminar este contacto? (s/n): ");
            string confirmacion = Console.ReadLine();
            
            if (confirmacion?.ToLower() == "s" || confirmacion?.ToLower() == "si")
            {
                agenda.EliminarContacto(telefono);
            }
            else
            {
                Console.WriteLine("❌ Eliminación cancelada.");
            }
        }
    }
}