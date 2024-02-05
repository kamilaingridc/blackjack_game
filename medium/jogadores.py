class Jogadores:
    def __init__(self, nome, idade, fichas):
        self.__nome = nome
        self.__idade = idade
        self.__fichas = fichas
        self.__cartas = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    @property
    def fichas(self):
        return self.__fichas

    @fichas.setter
    def fichas(self, novas_fichas):
        self.__fichas = novas_fichas

    def adicionar_fichas(self, quantidade):
        self.__fichas += quantidade

    def receber_carta(self, carta):
        self.__cartas.append(carta)

    def mostrar_cartas(self):
        return self.__cartas
