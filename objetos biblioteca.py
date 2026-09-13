class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
    
    def prestarLibro(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolverLibro(self):
        self.disponible = True

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
    
    def prestar(self):
        return self.libro.prestarLibro()

# Uso
libro1 = Libro("100 años de soledad", "García Márquez", "123")
user1 = Usuario("Ana", "1001")
p1 = Prestamo(libro1, user1)
print(p1.prestar()) # True