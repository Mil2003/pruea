from abc import ABC, abstractmethod

# Clase abstracta que define una interfaz para diferentes formas
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una forma"""
        pass

    @abstractmethod
    def calcular_perimetro(self):
        """Método abstracto para calcular el perímetro de una forma"""
        pass

# Implementaciones concretas de formas
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Demostración de uso
def main():
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)

    formas = [circulo, rectangulo]
    for forma in formas:
        print(f"Área: {forma.calcular_area()}")
        print(f"Perímetro: {forma.calcular_perimetro()}")

if __name__ == "__main__":
    main()
