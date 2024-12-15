class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau! Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau! Miau!"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu! Muuu!"

# Función que demuestra el polimorfismo
def sonido_animal(animal):
    print(animal.hacer_sonido())

# Demostración de uso
def main():
    perro = Perro()
    gato = Gato()
    vaca = Vaca()

    animales = [perro, gato, vaca]
    
    for animal in animales:
        sonido_animal(animal)

if __name__ == "__main__":
    main()
