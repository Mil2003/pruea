# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas diarias de la semana:")
    for i in range(7):
        temp = float(input(f"Temperatura día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Programa principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de las temperaturas es: {promedio_semanal:.2f}°C")

if __name__ == "__main__":
    main()
