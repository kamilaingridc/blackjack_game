class Jogador():
    def __init__(self, name, age, tokens):
        # Inicialização dos atributos privados do jogador
        self.__name = name
        self.__age = age
        self.__tokens = tokens

    # Getters e setters para os atributos privados do jogador
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def tokens(self):
        return self.__tokens

    @tokens.setter
    def tokens(self, value):
        self.__tokens = value
