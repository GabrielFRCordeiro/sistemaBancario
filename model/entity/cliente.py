class Cliente:
    def __init__(self, login: str, senha: str):
        self.__id = 1
        self.__idContato = 1
        self.__login = login
        self.__senha = senha

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, login: str) -> None:
        self.__login = login

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, novaSenha: str) -> None:
        self.__senha = novaSenha
