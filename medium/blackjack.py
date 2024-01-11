import random


class Jogadores:
    def __init__(self, nome, idade, fichas):
        self.__nome = nome
        self.__idade = idade
        self.__fichas = fichas


class Jogo:
    def __init__(self):
        self.__baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4
        self.__lista_jogadores = []

    def menu(self):
        print("Seja bem-vindo ao Jogo!\n"
              "[1] Jogar | [2] Regras | [3] Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            print("Todos começam com 200 fichas.")
            self.dados()
            self.iniciar_jogo()

    def dados(self):
        try:
            jogadores_jogando = int(input("Quantos jogadores vão jogar? "))
            if jogadores_jogando >= 2:
                for i in range(jogadores_jogando):
                    nome = str(input(f"Jogador {i + 1}, qual seu nome? "))
                    idade = int(input(f"Jogador {nome}, qual sua idade? "))
                    if idade < 18:
                        print("Você deve ter pelo menos 18 anos para jogar.")
                        exit()
                    jogador = Jogadores(nome, idade, 200)
                    self.__lista_jogadores.append(jogador)
            else:
                print("Número mínimo de jogadores: 2\n"
                      "Digite novamente!")
                self.dados()
        except ValueError:
            print("Número inválido."
                  "Tente novamente.")
            self.dados()

    def distribuir_cartas(self):
        random.shuffle(self.__baralho)
        for jogador in self.__lista_jogadores:
            carta = self.__baralho.pop(0)
            print(f"{jogador._Jogadores__nome} recebeu a carta {carta}")

    def iniciar_jogo(self):
        pass


jogo = Jogo()
jogo.menu()
