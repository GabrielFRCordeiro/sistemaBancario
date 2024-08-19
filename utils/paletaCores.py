class CoresAplicacao:
    def __init__(self) -> None:
        self.__corPrimaria: str = '#27debf'
        self.__corSecundaria: str = '#9febde'
        self.__corHover: str = '#1b9b85'
        self.__corDefault: str = '#21bda3'
        self.__corBranca: str = '#ffffff'

    @property
    def corPrimaria(self) -> str:
        """
        Constante para retornar a cor primaria
        :return: str
        """
        return self.__corPrimaria

    @property
    def corSecundaria(self) -> str:
        """
        Constante para retornar a cor secundaria
        :return: str
        """
        return self.__corSecundaria

    @property
    def corHover(self) -> str:
        """
        Constante para retornar a cor hover dos botões
        :return: str
        """
        return self.__corHover

    @property
    def corDefault(self) -> str:
        """
        Constante para retornar a cor default dos botões
        :return: str
        """
        return self.__corDefault

    @property
    def corBranca(self) -> str:
        """
        Constante para retornar a cor branca
        :return: str
        """
        return self.__corBranca
