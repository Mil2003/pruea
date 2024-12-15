class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    # Getter para el titular
    def get_titular(self):
        return self.__titular

    # Getter para el saldo
    def get_saldo(self):
        return self.__saldo

    # Método para depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito de ${monto} realizado.")
        else:
            print("Monto inválido.")

    # Método para retirar dinero
    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro de ${monto} realizado.")
        else:
            print("Saldo insuficiente o monto inválido.")

# Demostración de uso
def main():
    cuenta = CuentaBancaria("Juan Pérez", 1000)
    
    print(f"Titular: {cuenta.get_titular()}")
    print(f"Saldo inicial: ${cuenta.get_saldo()}")
    
    cuenta.depositar(500)
    cuenta.retirar(200)
    
    print(f"Saldo final: ${cuenta.get_saldo()}")

if __name__ == "__main__":
    main()
