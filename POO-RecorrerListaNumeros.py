class ListaDeNumeros:
    def __init__(self):
        self.numeros = []

    def agregar_numero(self, numero):
        self.numeros.append(numero)

    def recorrer_numeros(self):
        if not self.numeros:
            print("La lista está vacía.")
            return
        for numero in self.numeros:
            print(numero)

    def mostrar(self):
        if not self.numeros:
            print("no hay numeros para calcular.")
            return
        print("mayor:", max(self.numeros))
        print("menor:", min(self.numeros))
        print("promedio:", sum(self.numeros) / len(self.numeros))

def pedir_entero(mensaje):
    """pide un numero entero y repite la pregunta si el dato no es valido"""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

datos = ListaDeNumeros()

cantidad = pedir_entero("Ingrese la cantidad de números que desea agregar: ")
for _ in range(cantidad):
    numero = pedir_entero("Ingrese un número: ")
    datos.agregar_numero(numero)

print("\nNUMEROS INGRESADOS:")
datos.recorrer_numeros()

print("\nRESULTADOS:")
datos.mostrar()