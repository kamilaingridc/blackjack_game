import random


class Jogo:
    def __init__(self):
        self.__fichas = 100
        self.__aposta = 0
        self.__min_pontos_parar = {
            15: 0, 16: 60, 17: 70, 18: 80, 19: 90, 20: 95, 21: 100
        }
        self.__baralho = {
            'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
        }
        self.__cartas_jogador = []
        self.__cartas_computador = []
        self.__pontos_jogador = 0
        self.__pontos_computador = 0

    def __str__(self):
        return f"Fichas: {self.__fichas}, Aposta: {self.__aposta}"

    @property
    def fichas(self):
        return self.__fichas

    @fichas.setter
    def fichas(self, valor):
        self.__fichas = valor

    @property
    def aposta(self):
        return self.__aposta

    @aposta.setter
    def aposta(self, valor):
        if valor <= self.__fichas:
            self.__aposta = valor
        else:
            print("Você não possui fichas suficientes para essa aposta!")

    def __calcular_pontos(self, cartas):
        pontos = 0
        ases = 0
        for carta in cartas:
            pontos += self.__baralho[carta]
            if carta == 'A':
                ases += 1
        while pontos > 21 and ases:
            pontos -= 10
            ases -= 1
        return pontos

    def __pegar_carta(self):
        carta = random.choice(list(self.__baralho.keys()))
        return carta

    def __jogar_computador(self):
        while self.__pontos_computador < 15 or (
                self.__pontos_computador <= 21 and random.randint(1, 100) > self.__min_pontos_parar[
            self.__pontos_computador]):
            carta = self.__pegar_carta()
            self.__cartas_computador.append(carta)
            self.__pontos_computador = self.__calcular_pontos(self.__cartas_computador)

    def jogar(self):
        print("Bem-vindo ao Blackjack!")
        while self.__fichas > 0:
            print("\nNovo Jogo!")
            self.__pontos_jogador = 0
            self.__pontos_computador = 0
            self.__cartas_jogador = []
            self.__cartas_computador = []

            while True:
                self.aposta = int(input(f"\nFichas disponíveis: {self.__fichas}. Faça sua aposta (mínimo de 20): "))
                if self.aposta >= 20:
                    break
                else:
                    print("Aposta mínima é de 20 fichas!")

            self.__cartas_jogador.append(self.__pegar_carta())
            self.__cartas_jogador.append(self.__pegar_carta())
            self.__pontos_jogador = self.__calcular_pontos(self.__cartas_jogador)

            self.__jogar_computador()

            print(f"\nSuas cartas: {self.__cartas_jogador} - Pontos: {self.__pontos_jogador}")
            while True:
                escolha = input("\nDeseja pedir mais uma carta? (s/n): ")
                if escolha.lower() == 's':
                    nova_carta = self.__pegar_carta()
                    self.__cartas_jogador.append(nova_carta)
                    self.__pontos_jogador = self.__calcular_pontos(self.__cartas_jogador)
                    print(f"Nova carta: {nova_carta} - Pontos: {self.__pontos_jogador}")
                    if self.__pontos_jogador > 21:
                        print("Você estourou 21! Você perdeu.")
                        self.__fichas -= self.__aposta
                        break
                else:
                    break

            if self.__pontos_jogador <= 21:
                print(f"\nComputador: {self.__cartas_computador} - Pontos: {self.__pontos_computador}")
                if self.__pontos_computador > 21 or self.__pontos_computador < self.__pontos_jogador:
                    print("Você ganhou!")
                    self.__fichas += self.__aposta
                elif self.__pontos_computador > self.__pontos_jogador:
                    print("Você perdeu.")
                    self.__fichas -= self.__aposta
                else:
                    print("Empate!")
            print(f"\nFichas restantes: {self.__fichas}")

        print("Você ficou sem fichas. Fim de jogo!")


jogo = Jogo()
jogo.jogar()
