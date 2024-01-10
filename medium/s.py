import random
from players import Jogador


class Jogo():
    def __init__(self):
        self.__jogadores = []
        self.__baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 5
        self.__num = 21
        self.__winner = None

    def menu(self):
        try:
            print("-" * 50)
            print("1- Start game")
            print("2- See value of cards")
            print("3- Rules")
            print("4- Exit game")
            option = int(input("What do you want to do? \n"))
            print("-" * 50)

            match option:
                case 1:
                    self.players()
                    print("Both of you start with 100 betting chips")
                    self.start_game()
                    self.play_again()

                case 2:
                    print("Value of cards:")
                    print(self.get_baralho())
                    self.menu()

                case 3:
                    self.regras()

                case 4:
                    exit()

        except ValueError:
            print("-" * 50)
            print("Invalid data")
            self.menu()

    @property
    def get_jogadores(self):
        return self.__jogadores

    def get_baralho(self):
        return self.__baralho

    def regras(self):
        print("Rules blackjack")
        print("\nObjective: Get as close as possible to 21 points without exceeding it."
              "\nCard Distribution:"
              "\nEach player and the dealer receive two cards."
              "\nWinning and Losing:"
              "\nBlackjack: Having 21 points with the first two cards automatically wins"
              "\nGoing Over 21: Immediate loss."
              "\nTies:"
              "\nThe bet is typically returned in case of a tie.")
        self.menu()

    def sortear_cartas(self, jogador):
        carta = random.choice(self.__baralho)
        jogador.cartas_jogador.append(carta)
        self.__baralho.remove(carta)

    def somar_cartas(self, jogador):
        return sum(jogador.cartas_jogador)

    def dif(self, soma_jogador):
        if soma_jogador > self.__num:
            return soma_jogador - self.__num
        else:
            return self.__num - soma_jogador

    def aposta(self, vencedor):
        for jogador in self.__jogadores:
            if vencedor == jogador:
                jogador.fichas += sum(jogador.fichas_apostadas)
                jogador.fichas_apostadas.clear()
            else:
                jogador.fichas_apostadas.clear()

    def players(self):
        qtd = int(input("How many players:"))

        if qtd >= 2:
            for i in range(1, qtd + 1):
                nome = input(f'What\'s the name of player {i}? ')
                jogador = Jogador(nome, 100)
                self.__jogadores.append(jogador)

            print("PLAYERS:")
            for i, jogador in enumerate(self.__jogadores, start=1):
                print(f'{i}. {jogador.nome}')

        else:
            print("The minimum to play is 2 players")
            print("-" * 50)
            self.players()

    def start_game(self):
        print("Let's start!")

        try:
            print("-" * 50)
            for jogador in self.__jogadores:
                aposta_jogador = float(input(f'{jogador.nome}, how many chips do you want to bet? R$'))

                if aposta_jogador > jogador.fichas:
                    print("You don't have enough chips for this bet, please re-bet.")
                    self.start_game()

                jogador.fichas -= aposta_jogador
                jogador.fichas_apostadas.append(aposta_jogador)
                self.sortear_cartas(jogador)

            while jogador in self.__jogadores:
                print("-" * 50)
                for jogador in self.__jogadores:
                    print(f'Cards {jogador.nome}: {self.somar_cartas(jogador)}')

                acao_jogadores = []
                for jogador in self.__jogadores:
                    print("-" * 50)
                    acao = int(input(f'{jogador.nome}, what do you want to do?:'
                                     f'\n1- Ask for cards'
                                     f'\n2- Stop'))
                    acao_jogadores.append((jogador, acao))

                for jogador, acao in acao_jogadores:
                    if acao == 1:
                        self.sortear_cartas(jogador)

                if all(acao == 2 for jogador, acao in acao_jogadores):
                    self.verificar_vencedor()
                    break

        except ValueError:
            print("Invalid data")
            self.start_game()

    def verificar_vencedor(self):
        soma_jogadores = [self.somar_cartas(jogador) for jogador in self.__jogadores]
        diferenca_jogadores = [self.dif(soma) for soma in soma_jogadores]

        menor_diferenca = float('inf')

        for i, jogador in enumerate(self.__jogadores):
            if diferenca_jogadores[i] < menor_diferenca and soma_jogadores[i] < self.__num:
                self.__winner = jogador
                menor_diferenca = diferenca_jogadores[i]
            elif diferenca_jogadores[i] == menor_diferenca and soma_jogadores[i] < self.__num:
                if soma_jogadores[i] > soma_jogadores[self.__jogadores.index(self.__winner)]:
                    self.__winner = jogador

        for i, jogador in enumerate(self.__jogadores):
            if soma_jogadores[i] == self.__num:
                print("-" * 50)
                print(f'{jogador.nome} you won with {soma_jogadores[i]} points!')
                self.aposta(jogador)
                print(f'Now {jogador.nome} has R${jogador.fichas} betting chips')

        if all(soma > self.__num for soma in soma_jogadores):
            print("-" * 50)
            print(f"It's a draw! All players exceeded the target value.")
            for i, jogador in enumerate(self.__jogadores):
                print(f'{jogador.nome}:{soma_jogadores[i]}')
        else:
            print("-" * 50)
            print(f'{self.__winner.nome} you won with {soma_jogadores[self.__jogadores.index(self.__winner)]} points!')
            self.aposta(self.__winner)
            print(f'Now {self.__winner.nome} has R${self.__winner.fichas} betting chips')

    def play_again(self):
        print("-" * 50)

    def play_again(self):
        # arrumar
        print("-" * 50)
        option = int(input("Do you want to play again?\n1- Yes\n2- No"))
        match option:
            case 1:
                self.menu()

            case 2:
                exit()


if __name__ == '__main__':
    jogo = Jogo()
    jogo.menu()
