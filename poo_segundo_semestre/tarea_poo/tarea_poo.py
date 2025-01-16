# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        # Atributos privados: encapsulación
        self.__nombre = nombre
        self.__edad = edad

    # Métodos para acceder a los atributos privados (getter y setter)
    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_edad(self):
        return self.__edad

    def establecer_edad(self, edad):
        if edad > 0:  # Validación simple
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo.")

    # Método común para mostrar información
    def mostrar_informacion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

# Clase derivada: Estudiante (herencia de Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        # Atributo adicional
        self.carrera = carrera

    # Sobrescritura de método (polimorfismo)
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Carrera: {self.carrera}"

# Clase derivada: Profesor (herencia de Persona)
class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    # Sobrescritura de método (polimorfismo)
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Especialidad: {self.especialidad}"

# Programa principal: Creación de objetos e interacción
def main():
    # Crear objetos de las clases derivadas
    estudiante = Estudiante("Juan", 20, "Ingeniería en Software")
    profesor = Profesor("Laura", 35, "Matemáticas")

    # Mostrar información de los objetos
    print("Información del Estudiante:")
    print(estudiante.mostrar_informacion())

    print("\nInformación del Profesor:")
    print(profesor.mostrar_informacion())

    # Demostración de encapsulación
    print("\nActualización de datos del estudiante:")
    estudiante.establecer_nombre("Juan Pérez")
    estudiante.establecer_edad(21)
    print(estudiante.mostrar_informacion())

# Ejecución del programa principal
if __name__ == "__main__":
    main()
