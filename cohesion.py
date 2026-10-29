
    #ALTA COHESION: tiene que ver con el estudiante y su promedio
class Estudiante:
    def __init__(self,nombre,nota1,nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_promedio(self):
        return (self.nota1 + self.nota2) /2

    def es_aprobado(self):
        return self.calcular_promedio()>=6

    def mostrar(self):
        print(f"{self.nombre}:promedio: {self.calcular_promedio()}")

e = Estudiante("Juan", 7, 8)
e.mostrar()
print(e.es_aprobado())
