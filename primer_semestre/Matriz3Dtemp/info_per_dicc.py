# Creación del diccionario
informacion_personal = {
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor de "ciudad" y modificarlo
print("Ciudad antes de la modificación:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Guayaquil"  # Cambio de ciudad
print("Ciudad después de la modificación:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor "telefono" si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número de teléfono ficticio

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminamos la edad

# Imprimir el diccionario final
print("Diccionario final después de todas las operaciones:")
print(informacion_personal)
