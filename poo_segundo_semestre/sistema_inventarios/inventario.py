# inventario.py
from producto import Producto

class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar los productos.
        """
        self.productos = []

    def añadir_producto(self, id, nombre, cantidad, precio):
        """
        Añade un nuevo producto al inventario.
        :param id: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en el inventario.
        :param precio: Precio del producto.
        """
        if any(producto.get_id() == id for producto in self.productos):
            print("Error: El ID ya existe.")
        else:
            nuevo_producto = Producto(id, nombre, cantidad, precio)
            self.productos.append(nuevo_producto)
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        :param id: Identificador único del producto.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.
        :param id: Identificador único del producto.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos por nombre.
        :param nombre: Nombre del producto a buscar.
        :return: Lista de productos que coinciden con el nombre.
        """
        productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return productos_encontrados

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)