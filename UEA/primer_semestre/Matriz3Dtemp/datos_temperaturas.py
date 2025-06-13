# datos_temperaturas.py

from Dtemps import temperaturas


def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad y cada semana.

    Parámetros:
    temperaturas (list): Una matriz 3D donde la primera dimensión es ciudades, la segunda es semanas y la tercera es días de la semana.

    Retorna:
    dict: Un diccionario donde las claves son nombres de ciudades y los valores son listas con los promedios de cada semana.
    """
    resultados = {}

    for i, ciudad in enumerate(temperaturas):
        ciudad_key = f"Ciudad {chr(65 + i)}"
        resultados[ciudad_key] = []

        for semana in ciudad:
            total_temp = 0
            num_dias = len(semana)
            for dia in semana:
                total_temp += dia['temperatura']
            promedio_temp = total_temp / num_dias
            resultados[ciudad_key].append(promedio_temp)

    return resultados


if __name__ == "__main__":
    resultados = calcular_promedio_temperaturas(temperaturas)
    for ciudad, promedios in resultados.items():
        print(f"{ciudad}:")
        for i, promedio in enumerate(promedios):
            print(f"  Promedio de temperatura en la Semana {i + 1}: {promedio:.1f}°C")
        print()
