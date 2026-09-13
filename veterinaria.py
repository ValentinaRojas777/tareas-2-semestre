class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacerSonido(self): # Polimorfismo
        pass

    def vacunar(self):
        print(f"{self.nombre} vacunado")

class Perro(Animal):
    def hacerSonido(self):
        return "Guau!"

class Gato(Animal):
    def hacerSonido(self):
        return "Miau!"

animales = [Perro("Toby", 2), Gato("Michi", 1)]
for a in animales:
    print(f"{a.nombre}: {a.hacerSonido()}")
    a.vacunar()