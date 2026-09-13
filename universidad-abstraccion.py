class Estudiante:
    def __init__(self, nombre, codigo, carrera):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.notas = []

    def matricular(self, materia):
        print(f"{self.nombre} matriculado en {materia}")

    def calcularPromedio(self):
        if not self.notas: return 0
        return sum(self.notas) / len(self.notas)

est = Estudiante("Carlos", "2024-01", "Sistemas")
est.notas = [4.5, 3.8, 4.0]
est.matricular("POO")
print(est.calcularPromedio())