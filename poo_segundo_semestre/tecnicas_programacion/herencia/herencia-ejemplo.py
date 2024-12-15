class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def obtener_detalles(self):
        return f"{self.nombre} {self.apellido} - Salario: ${self.salario}"

class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, salario, lenguaje_programacion):
        super().__init__(nombre, apellido, salario)
        self.lenguaje_programacion = lenguaje_programacion

    def obtener_detalles(self):
        detalles_base = super().obtener_detalles()
        return f"{detalles_base}, Lenguaje: {self.lenguaje_programacion}"

class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario, departamento):
        super().__init__(nombre, apellido, salario)
        self.departamento = departamento

    def obtener_detalles(self):
        detalles_base = super().obtener_detalles()
        return f"{detalles_base}, Departamento: {self.departamento}"

# Demostración de uso
def main():
    desarrollador = Desarrollador("Ana", "García", 5000, "Python")
    gerente = Gerente("Carlos", "Rodríguez", 8000, "TI")

    empleados = [desarrollador, gerente]
    for empleado in empleados:
        print(empleado.obtener_detalles())

if __name__ == "__main__":
    main()
