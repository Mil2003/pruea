# Sistema de Registro de Artesanías
# Autor: Milton Mosquera
# Descripción: Este programa permite registrar y gestionar información básica sobre productos
# artesanales, incluyendo nombre, precio, disponibilidad y categoría.

def registrar_producto(nombre: str, precio: float, disponible: bool, categoria: str) -> dict:
    """
    Registra un nuevo producto artesanal con sus características.
    
    Args:
        nombre: Nombre del producto artesanal
        precio: Precio de venta del producto
        disponible: Estado de disponibilidad del producto
        categoria: Categoría del producto (ejemplo: 'tejido', 'madera', 'joyería')
    
    Returns:
        Diccionario con la información del producto
    """
    producto = {
        "nombre": nombre,
        "precio": precio,
        "disponible": disponible,
        "categoria": categoria
    }
    return producto

def calcular_precio_total(cantidad: int, precio_unitario: float) -> float:
    """
    Calcula el precio total de una venta incluyendo IVA.
    
    Args:
        cantidad: Número de unidades a vender
        precio_unitario: Precio por unidad del producto
    
    Returns:
        Precio total incluyendo IVA (12%)
    """
    iva = 0.12
    subtotal = cantidad * precio_unitario
    precio_total = subtotal + (subtotal * iva)
    return round(precio_total, 2)

def mostrar_detalles_producto(producto: dict) -> None:
    """
    Muestra los detalles de un producto en un formato legible.
    
    Args:
        producto: Diccionario con la información del producto
    """
    estado = "Disponible" if producto["disponible"] else "No disponible"
    print("\nDetalles del Producto:")
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoría: {producto['categoria']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Estado: {estado}")

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Registro de un nuevo producto usando diferentes tipos de datos
    nombre_producto = "Collar de Tagua"    # string
    precio_base = 25.50                    # float
    hay_stock = True                       # boolean
    tipo_producto = "joyería"             # string
    
    # Registrar el producto
    mi_producto = registrar_producto(nombre_producto, precio_base, hay_stock, tipo_producto)
    
    # Mostrar información del producto
    mostrar_detalles_producto(mi_producto)
    
    # Calcular precio de venta para 3 unidades
    cantidad_venta = 3                     # integer
    precio_venta = calcular_precio_total(cantidad_venta, precio_base)
    print(f"\nPrecio total por {cantidad_venta} unidades: ${precio_venta}")