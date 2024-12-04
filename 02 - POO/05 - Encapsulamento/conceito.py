class Conta:
    def __init__(self, saldo = 0):
        self._saldo = saldo

    def depositar(self, valor):
        """Realiza depósito.

        Args:
            valor (float): Valor a ser depositado
        """
        self._saldo += valor

    def sacar(self, valor):
        """Realiza saque.

        Args:
            valor (float): Valor a ser sacado
        """
        self._saldo -= valor
    # end def
    def mostrar_saldo(self):
        """
        Purpose: self    
        """
        return self._saldo
    # end def

conta = Conta(100)
print(conta.mostrar_saldo())