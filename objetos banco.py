class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def consignar(self, valor: float):
        self.saldo += valor
        print(f"Consignado {valor}. Nuevo saldo: {self.saldo}")

    def retirar(self, valor: float) -> bool:
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Retirado {valor}. Nuevo saldo: {self.saldo}")
            return True
        else:
            print("Saldo insuficiente")
            return False

    def consultarSaldo(self) -> float:
        return self.saldo

# Herencia
class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0, interes=0.02):
        super().__init__(numero_cuenta, titular, saldo)
        self.interes = interes

    def aplicarInteres(self):
        self.saldo += self.saldo * self.interes
        print(f"Interés aplicado. Nuevo saldo: {self.saldo}")

# Prueba
cuenta = CuentaAhorros("001", "Juan", 100000)
cuenta.consignar(50000)
cuenta.retirar(20000)
cuenta.aplicarInteres()