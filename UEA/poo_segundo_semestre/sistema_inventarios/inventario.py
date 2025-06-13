import json
from producto import Producto

class Inventario:
    def __init__(self, archivo='inventario.json'):
        """
        Constructor de la clase Inventario.
        Inicializa un diccionario vacío para almacenar los productos y carga los productos desde el archivo.
        :param archivo: Nombre del archivo donde se almacena el inventario.
        """
        self.archivo = archivo
        self.productos = {}  # Usamos un diccionario para productos, usando el ID como clave
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los productos desde el archivo JSON de inventario.
        Si el archivo no existe, se crea uno nuevo.
        """
        try:
            with open(self.archivo, 'r') as f:
                productos_data = json.load(f)
                for producto_data in productos_data:
                    producto = Producto.from_dict(producto_data)
                    self.productos[producto.get_id()] = producto
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            open(self.archivo, 'w').close()
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. El archivo puede estar corrupto.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda los productos en el archivo JSON de inventario.
        """
        try:
            productos_data = [producto.to_dict() for producto in self.productos.values()]
            with open(self.archivo, 'w') as f:
                json.dump(productos_data, f, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, id, nombre, cantidad, precio):
        """
        Añade un nuevo producto al inventario y lo guarda en el archivo.
        :param id: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en el inventario.
        :param precio: Precio del producto.
        """
        if id in self.productos:
            print("Error: El ID ya existe.")
        else:
            nuevo_producto = Producto(id, nombre, cantidad, precio)
            self.productos[id] = nuevo_producto
            self.guardar_inventario()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID y actualiza el archivo.
        :param id: Identificador único del producto.
        """
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID y actualiza el archivo.
        :param id: Identificador único del producto.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print("Producto actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos por nombre.
        :param nombre: Nombre del producto a buscar.
        :return: Lista de productos que coinciden con el nombre.
        """
        productos_encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        return productos_encontrados

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)
