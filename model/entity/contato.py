class Contato:
    def __init__(self, telefone: str, email: str):
        self.__id = 1
        self.__telefone = telefone
        self.__email = email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, novoTelefone: str) -> None:
        self.__telefone = novoTelefone

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, novoEmail: str) -> None:
        self.__email = novoEmail
