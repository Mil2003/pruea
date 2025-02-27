class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en el inventario.
        :param precio: Precio del producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_dict(self):
        """
        Convierte el objeto Producto a un diccionario, para ser utilizado en JSON.
        :return: Diccionario con los atributos del producto.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Producto a partir de un diccionario, típicamente deserializado desde JSON.
        :param data: Diccionario con los datos del producto.
        :return: Un objeto Producto.
        """
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])
