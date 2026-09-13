class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Carrito:
    def __init__(self):
        self.productos = []

    def agregarAlCarrito(self, producto):
        if producto.stock > 0:
            self.productos.append(producto)
            producto.stock -= 1

    def calcularTotal(self):
        return sum(p.precio for p in self.productos)

p1 = Producto("Mouse", 50000, 10)
p2 = Producto("Teclado", 120000, 5)
carrito = Carrito()
carrito.agregarAlCarrito(p1)
carrito.agregarAlCarrito(p2)
print(f"Total: {carrito.calcularTotal()}")