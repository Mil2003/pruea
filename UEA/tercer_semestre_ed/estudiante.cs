using System;

namespace RegistroEstudiante
{
    /// <summary>
    /// Clase que representa un estudiante con sus datos personales
    /// Incluye manejo de múltiples teléfonos mediante arrays
    /// </summary>
    public class Estudiante
    {
        // Campos privados para encapsular los datos
        private int id;
        private string nombres;
        private string apellidos;
        private string direccion;
        private string[] telefonos; // Array para almacenar 3 teléfonos

        /// <summary>
        /// Constructor de la clase Estudiante
        /// </summary>
        /// <param name="id">Identificador único del estudiante</param>
        /// <param name="nombres">Nombres del estudiante</param>
        /// <param name="apellidos">Apellidos del estudiante</param>
        /// <param name="direccion">Dirección de residencia</param>
        public Estudiante(int id, string nombres, string apellidos, string direccion)
        {
            this.id = id;
            this.nombres = nombres ?? throw new ArgumentNullException(nameof(nombres));
            this.apellidos = apellidos ?? throw new ArgumentNullException(nameof(apellidos));
            this.direccion = direccion ?? throw new ArgumentNullException(nameof(direccion));
            
            // Inicializar array de teléfonos con capacidad para 3 números
            this.telefonos = new string[3];
            
            // Inicializar con valores vacíos para evitar referencias nulas
            for (int i = 0; i < telefonos.Length; i++)
            {
                telefonos[i] = "";
            }
        }

        // Propiedades públicas para acceder a los datos (Get/Set)
        
        /// <summary>
        /// Identificador único del estudiante
        /// </summary>
        public int Id
        {
            get { return id; }
            set 
            { 
                if (value > 0)
                    id = value;
                else
                    throw new ArgumentException("El ID debe ser mayor a 0");
            }
        }

        /// <summary>
        /// Nombres del estudiante
        /// </summary>
        public string Nombres
        {
            get { return nombres; }
            set 
            { 
                if (!string.IsNullOrWhiteSpace(value))
                    nombres = value.Trim();
                else
                    throw new ArgumentException("Los nombres no pueden estar vacíos");
            }
        }

        /// <summary>
        /// Apellidos del estudiante
        /// </summary>
        public string Apellidos
        {
            get { return apellidos; }
            set 
            { 
                if (!string.IsNullOrWhiteSpace(value))
                    apellidos = value.Trim();
                else
                    throw new ArgumentException("Los apellidos no pueden estar vacíos");
            }
        }

        /// <summary>
        /// Dirección de residencia del estudiante
        /// </summary>
        public string Direccion
        {
            get { return direccion; }
            set 
            { 
                if (!string.IsNullOrWhiteSpace(value))
                    direccion = value.Trim();
                else
                    throw new ArgumentException("La dirección no puede estar vacía");
            }
        }

        /// <summary>
        /// Array de teléfonos del estudiante (máximo 3)
        /// </summary>
        public string[] Telefonos
        {
            get { return telefonos; }
        }

        // Métodos específicos para manejar los teléfonos

        /// <summary>
        /// Establece un teléfono en la posición especificada
        /// </summary>
        /// <param name="indice">Posición en el array (0, 1 o 2)</param>
        /// <param name="telefono">Número telefónico</param>
        public void SetTelefono(int indice, string telefono)
        {
            if (indice >= 0 && indice < telefonos.Length)
            {
                telefonos[indice] = telefono ?? "";
            }
            else
            {
                throw new IndexOutOfRangeException("Índice de teléfono debe estar entre 0 y 2");
            }
        }

        /// <summary>
        /// Obtiene un teléfono de la posición especificada
        /// </summary>
        /// <param name="indice">Posición en el array (0, 1 o 2)</param>
        /// <returns>Número telefónico en la posición especificada</returns>
        public string GetTelefono(int indice)
        {
            if (indice >= 0 && indice < telefonos.Length)
            {
                return telefonos[indice];
            }
            else
            {
                throw new IndexOutOfRangeException("Índice de teléfono debe estar entre 0 y 2");
            }
        }

        /// <summary>
        /// Método para mostrar toda la información del estudiante
        /// </summary>
        /// <returns>Cadena con toda la información formateada</returns>
        public override string ToString()
        {
            string info = $"ID: {id}\n";
            info += $"Nombres: {nombres}\n";
            info += $"Apellidos: {apellidos}\n";
            info += $"Dirección: {direccion}\n";
            info += "Teléfonos:\n";
            
            for (int i = 0; i < telefonos.Length; i++)
            {
                info += $"  Teléfono {i + 1}: {(string.IsNullOrEmpty(telefonos[i]) ? "No registrado" : telefonos[i])}\n";
            }
            
            return info;
        }

        /// <summary>
        /// Método para validar si todos los datos obligatorios están completos
        /// </summary>
        /// <returns>True si los datos están completos, False en caso contrario</returns>
        public bool DatosCompletos()
        {
            return id > 0 && 
                   !string.IsNullOrWhiteSpace(nombres) && 
                   !string.IsNullOrWhiteSpace(apellidos) && 
                   !string.IsNullOrWhiteSpace(direccion);
        }
    }

    /// <summary>
    /// Clase principal para demostrar el uso de la clase Estudiante
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== SISTEMA DE REGISTRO DE ESTUDIANTES ===\n");

            try
            {
                // Crear una instancia de estudiante
                Estudiante estudiante1 = new Estudiante(
                    1001, 
                    "Milton Manuel", 
                    "Mosquera Quiñones", 
                    "Esmeraldas, Ecuador"
                );

                // Asignar teléfonos usando el método SetTelefono
                estudiante1.SetTelefono(0, "0987654321");
                estudiante1.SetTelefono(1, "062345678");
                estudiante1.SetTelefono(2, "0991234567");

                // Mostrar información del estudiante
                Console.WriteLine("Información del Estudiante:");
                Console.WriteLine(estudiante1.ToString());

                // Verificar si los datos están completos
                Console.WriteLine($"Datos completos: {(estudiante1.DatosCompletos() ? "Sí" : "No")}");

                // Demostrar acceso individual a teléfonos
                Console.WriteLine("\nAcceso individual a teléfonos:");
                for (int i = 0; i < 3; i++)
                {
                    Console.WriteLine($"Teléfono {i + 1}: {estudiante1.GetTelefono(i)}");
                }

                // Crear un array de estudiantes para demostrar manejo múltiple
                Console.WriteLine("\n=== REGISTRO MÚLTIPLE DE ESTUDIANTES ===");
                
                Estudiante[] listaEstudiantes = new Estudiante[3];
                
                // Llenar el array con estudiantes de ejemplo
                listaEstudiantes[0] = estudiante1;
                
                listaEstudiantes[1] = new Estudiante(1002, "Ana María", "García López", "Quito, Ecuador");
                listaEstudiantes[1].SetTelefono(0, "0998877665");
                
                listaEstudiantes[2] = new Estudiante(1003, "Carlos Eduardo", "Ramírez Silva", "Guayaquil, Ecuador");
                listaEstudiantes[2].SetTelefono(0, "0987766554");
                listaEstudiantes[2].SetTelefono(1, "042234567");

                // Mostrar todos los estudiantes registrados
                for (int i = 0; i < listaEstudiantes.Length; i++)
                {
                    Console.WriteLine($"\n--- Estudiante {i + 1} ---");
                    Console.WriteLine(listaEstudiantes[i].ToString());
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }

            Console.WriteLine("\nPresione cualquier tecla para salir...");
            Console.ReadKey();
        }
    }
}