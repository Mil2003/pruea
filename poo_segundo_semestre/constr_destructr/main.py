# Clase principal: Archivo
class Archivo:
    def __init__(self, nombre, contenido):
        """
        Constructor de la clase Archivo.
        Este método se activa al momento de crear una instancia de la clase.
        Inicializa el nombre del archivo y su contenido.

        :param nombre: Nombre del archivo (str)
        :param contenido: Contenido del archivo (str)
        """
        self.nombre = nombre
        self.contenido = contenido
        print(f"Archivo '{self.nombre}' creado exitosamente.")
    
    def guardar(self):
        """
        Método para guardar el contenido del archivo en un archivo físico.
        """
        with open(self.nombre, 'w') as file:
            file.write(self.contenido)
        print(f"Contenido guardado en '{self.nombre}'.")
    
    def leer(self):
        """
        Método para leer y mostrar el contenido del archivo.
        """
        with open(self.nombre, 'r') as file:
            datos = file.read()
        print(f"Contenido de '{self.nombre}':\n{datos}")
    
    def __del__(self):
        """
        Destructor de la clase Archivo.
        Este método se activa automáticamente cuando el objeto es eliminado
        o cuando el programa finaliza.
        """
        print(f"El archivo '{self.nombre}' ha sido cerrado y limpiado de memoria.")


# Clase derivada: ArchivoTemporal (simula un archivo que se elimina automáticamente)
class ArchivoTemporal(Archivo):
    def __del__(self):
        """
        Destructor especializado para archivos temporales.
        Simula la eliminación del archivo al finalizar.
        """
        import os
        if os.path.exists(self.nombre):
            os.remove(self.nombre)
            print(f"Archivo temporal '{self.nombre}' eliminado del sistema.")
        super().__del__()


# Uso de las clases
if __name__ == "__main__":
    # Crear una instancia de Archivo
    archivo1 = Archivo("mi_archivo.txt", "Este es un ejemplo de contenido.")
    archivo1.guardar()
    archivo1.leer()

    # Crear un archivo temporal
    temp_file = ArchivoTemporal("archivo_temporal.txt", "Este archivo será eliminado al final.")
    temp_file.guardar()
    temp_file.leer()

    # Eliminar los objetos manualmente (para activar __del__)
    del archivo1
    del temp_file

    print("Fin del programa.")
