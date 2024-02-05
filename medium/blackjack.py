import random
import time
from jogadores import Jogadores


class Jogo:
    def __init__(self):
        self.__baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4
        self.__lista_jogadores = []

    def menu(self):
        print("Seja bem-vindo ao Jogo!\n"
              "[1] Jogar | [2] Regras | [3] Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            self.dados()
        elif opcao == 2:
            self.regras()
        elif opcao == 3:
            print("Saindo do jogo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            self.menu()

    def regras(self):
        print("REGRAS DO BLACKJACK!\n"
              "O objetivo é obter uma mão com um valor total mais próximo de 21 do que o oponente, "
              "sem ultrapassar 21.\n"
              "\nCartas e Valores:\n"
              "As cartas têm o valor correspondente ao número nelas representado.\n"
              "\nJogabilidade:\n"
              "Os jogadores podem pedir cartas adicionais para se aproximar de 21 ou manter as "
              "cartas atuais. Se o total das cartas do jogador ultrapassar 21, ele perde automaticamente.\n")
        time.sleep(1)
        self.menu()

    def dados(self):
        try:
            jogadores_jogando = int(input("Quantos jogadores vão jogar? "))
            if jogadores_jogando >= 2:
                for i in range(jogadores_jogando):
                    nome = str(input(f"Jogador(a) {i + 1}, qual seu nome? "))
                    idade = int(input(f"Jogador(a) {nome}, qual sua idade? "))
                    print(40 * "-")
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
            print("Número inválido. Tente novamente.")
            self.dados()
        self.iniciar_jogo()

    def distribuir_cartas(self):
        for jogador in self.__lista_jogadores:
            random.shuffle(self.__baralho)
            carta = self.__baralho.pop()
            jogador.receber_carta(carta)
            print(f"{jogador.nome} recebeu a carta {carta}.")
        print(40 * '-')

    def exibir_fichas(self):
        for jogador in self.__lista_jogadores:
            print(f"{jogador.nome} tem {jogador.fichas} fichas.")

    def aposta(self):
        apostando = {}  # Dicionário para armazenar as apostas dos jogadores
        print("Ambos começam com 200 fichas.")
        for i, jogador in enumerate(self.__lista_jogadores):
            if jogador.fichas > 0:
                apostando[jogador] = int(input(f"{jogador.nome}, quanto você vai querer apostar? "))
                if 0 < apostando[jogador] <= jogador.fichas:
                    jogador.adicionar_fichas(-apostando[jogador])
                else:
                    print("Saldo insuficiente.")
                    self.aposta()
            else:
                print(f"{jogador.nome}, você não tem fichas suficientes.")
        print(40 * "-")
        return apostando

    def vencedor(self, jogadores, apostando):
        for jogador in jogadores:
            total_pontos = sum(jogador.mostrar_cartas())
            if total_pontos > 21:
                print(f'{jogador.nome} perdeu.')
                for vencedor, aposta in apostando.items():
                    if vencedor != jogador:
                        vencedor.adicionar_fichas(aposta)
                        jogador.adicionar_fichas(-aposta)
                        print(
                            f"{vencedor.nome} ganhou {aposta} fichas. Seu saldo atual é {vencedor.fichas + aposta}.")
            elif total_pontos == 21:
                print(f'{jogador.nome} venceu!! Parabéns.')
                jogador.adicionar_fichas(apostando[jogador])
                print(
                    f"{jogador.nome} ganhou {apostando[jogador]} fichas. Seu saldo atual é {jogador.fichas + aposta}.")

    def iniciar_jogo(self):
        print("Vamos começar!!")
        print(40 * "-")
        time.sleep(1)
        self.distribuir_cartas()
        apostando = self.aposta()

        num_jogadores = len(self.__lista_jogadores)
        index_jogador = 0

        while True:
            jogador = self.__lista_jogadores[index_jogador]
            escolha = int(input(f"{jogador.nome}, escolha:\n"
                                "[1] Pegar cartas | [2] Não pegar cartas "))

            if escolha == 1:
                carta = self.__baralho.pop()
                jogador.receber_carta(carta)
                print(f'{jogador.nome}, suas cartas atuais: {jogador.mostrar_cartas()}\n')

                total_pontos = sum(jogador.mostrar_cartas())
                if total_pontos > 21:
                    print(f'{jogador.nome}, você ultrapassou 21.\n')
                    self.vencedor(self.__lista_jogadores, apostando)
                    break
            elif escolha == 2:
                print(f'{jogador.nome}, suas cartas atuais: {jogador.mostrar_cartas()}.\n'
                      f'Fim do jogo!')
                self.vencedor(self.__lista_jogadores, apostando)
                break
            else:
                print("Opção inválida. Tente novamente.")

            index_jogador = (index_jogador + 1) % num_jogadores


jogo = Jogo()
jogo.menu()
