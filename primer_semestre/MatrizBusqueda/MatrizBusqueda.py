# Definimos la matriz bidimensional de 3x3
matriz = [
    [5, 8, 10],
    [3, 6, 9],
    [4, 7, 2]
]

def buscar_en_matriz(matriz_input, valor_buscado):
    # Iteramos sobre la matriz para buscar el valor
    for i in range(len(matriz_input)):
        for j in range(len(matriz_input[i])):
            if matriz_input[i][j] == valor_buscado:
                return i, j  # Retorna la posición (fila, columna)
    return None  # Retorna None si no se encuentra el valor

# Valor a buscar
valor_buscado = 7

# Realizamos la búsqueda
resultado = buscar_en_matriz(matriz, valor_buscado)

# Verificamos si se encontró el valor
if resultado:
    print("Valor {} encontrado en la posición: {}".format(valor_buscado, resultado))
else:
    print("Valor {} no encontrado en la matriz.".format(valor_buscado))
