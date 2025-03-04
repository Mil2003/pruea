class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.usuario_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios = set()  # Conjunto para IDs únicos de usuarios
        self.registro_usuarios = {}  # Diccionario para mapear ID a objetos Usuario

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.usuario_id not in self.usuarios:
            self.usuarios.add(usuario.usuario_id)
            self.registro_usuarios[usuario.usuario_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            self.usuarios.remove(usuario_id)
            del self.registro_usuarios[usuario_id]
            print(f"Usuario con ID {usuario_id} dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios and isbn in self.libros:
            usuario = self.registro_usuarios[usuario_id]
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}")
        else:
            print("Usuario o libro no disponible.")

    def devolver_libro(self, usuario_id, isbn):
        if usuario_id in self.usuarios:
            usuario = self.registro_usuarios[usuario_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("El usuario no está registrado.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio, '').lower() == valor.lower()]
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, usuario_id):
        if usuario_id in self.usuarios:
            usuario = self.registro_usuarios[usuario_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("El usuario no está registrado.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("1984", "George Orwell", "Ficción", "12345")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "67890")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Milton Mosquera", "001")
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro("001", "12345")

# Listar libros prestados
biblioteca.listar_libros_prestados("001")

# Devolver libro
biblioteca.devolver_libro("001", "12345")

# Buscar libro por categoría
biblioteca.buscar_libro("categoria", "Ficción")
