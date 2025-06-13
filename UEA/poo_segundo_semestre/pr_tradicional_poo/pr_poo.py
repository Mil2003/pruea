class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar temperaturas diarias
    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas diarias de la semana:")
        for i in range(7):
            temp = float(input(f"Temperatura día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio_semanal = clima.calcular_promedio()
    print(f"\nEl promedio semanal de las temperaturas es: {promedio_semanal:.2f}°C")

if __name__ == "__main__":
    main()
