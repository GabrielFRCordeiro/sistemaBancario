class Conta:
    def __init__(self, saldo: float):
        self.__id = 1
        self.idCliente = 1
        self.__saldo = saldo

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, novoSaldo: float) -> None:
        self.__saldo = novoSaldo
