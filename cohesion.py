#baja cohesion:hace de todo y mezcla cosas que no tienen nada que ver 

class Estudiante:
    def __init__(self,nombre,nota1,nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_promedio(self):
        return (self.nota1 + self.nota2) /2

    def imprimir_factura_Cafeteria(self):
        print(" factura cafeteria")  #no tiene nada que ver con el estudiante


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