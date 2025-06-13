def bubble_sort(arr):
    """
    Ordena una lista usando el algoritmo de Bubble Sort.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sort_row(matrix, row_index):
    """
    Ordena una fila específica de la matriz en orden ascendente.
    """
    if row_index < 0 or row_index >= len(matrix):
        raise IndexError("El índice de la fila está fuera del rango de la matriz.")

    # Copiar la fila a ordenar y aplicar Bubble Sort
    row = matrix[row_index][:]
    bubble_sort(row)

    # Reemplazar la fila original con la fila ordenada
    matrix[row_index] = row


def print_matrix(matrix):
    """
    Imprime la matriz en formato de filas y columnas.
    """
    for row in matrix:
        print(row)


# Definimos la matriz bidimensional de 3x3
matrix = [
    [9, 3, 5],
    [6, 7, 2],
    [8, 1, 4]
]

# Mostrar la matriz original
print("Matriz original:")
print_matrix(matrix)

# Indicar el índice de la fila a ordenar
row_to_sort = 1  # Por ejemplo, ordenar la segunda fila (índice 1)

# Ordenar la fila especificada
sort_row(matrix, row_to_sort)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
print_matrix(matrix)
