# Clase Producto: Representa un artículo en la tienda.
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.cantidad = cantidad  # Cantidad disponible

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Cantidad disponible: {self.cantidad})"


# Clase CarritoDeCompra: Representa el carrito de un cliente.
class CarritoDeCompra:
    def __init__(self):
        self.productos = []  # Lista de productos en el carrito

    def agregar_producto(self, producto, cantidad):
        if producto.cantidad >= cantidad:  # Verificar si hay suficiente stock
            producto.cantidad -= cantidad
            self.productos.append((producto, cantidad))
            print(f"Se ha agregado {cantidad} de {producto.nombre} al carrito.")
        else:
            print(f"No hay suficiente stock de {producto.nombre}. Solo hay {producto.cantidad} disponibles.")

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)
        return total

    def mostrar_carrito(self):
        print("Productos en tu carrito:")
        for producto, cantidad in self.productos:
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio total: ${producto.precio * cantidad}")
        print(f"Total a pagar: ${self.calcular_total()}")


# Clase Cliente: Representa un cliente que compra en la tienda.
class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = CarritoDeCompra()  # El cliente tiene un carrito de compra

    def agregar_producto_al_carrito(self, producto, cantidad):
        self.carrito.agregar_producto(producto, cantidad)

    def ver_carrito(self):
        self.carrito.mostrar_carrito()


# Clase Tienda: Representa la tienda con un inventario de productos.
class Tienda:
    def __init__(self):
        self.inventario = []  # Inventario de productos disponibles

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        print("Inventario de productos en la tienda:")
        for producto in self.inventario:
            print(producto)

# Crear una tienda
tienda = Tienda()

# Agregar productos a la tienda
producto1 = Producto("Camiseta", 15.99, 100)
producto2 = Producto("Pantalones", 39.99, 50)
producto3 = Producto("Zapatos", 49.99, 30)

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Mostrar el inventario de la tienda
tienda.mostrar_inventario()

# Crear un cliente
cliente1 = Cliente("Juan Perez", "juan@example.com")

# El cliente agrega productos al carrito
cliente1.agregar_producto_al_carrito(producto1, 2)  # 2 camisetas
cliente1.agregar_producto_al_carrito(producto2, 1)  # 1 pantalón

# Ver el carrito de compra del cliente
cliente1.ver_carrito()
