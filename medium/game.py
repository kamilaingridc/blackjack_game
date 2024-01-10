import random
import time
from players import Jogador


class Game:
    def __init__(self):
        self.__deck = [2, 3, 4, 5, 6, 7, 8, 9, 10] * 4
        self.__players = []

    def distribuir_cartas(self, jogadores):
        random.shuffle(self.__deck)
        for jogador in jogadores:
            carta = self.__deck.pop()
            jogador.receber_carta(carta)

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

    def vencedor(self, jogadores):
        pontuacoes = {jogador.nome: sum(jogador.mostrar_cartas()) for jogador in jogadores}
        pontuacoes_validas = {nome: pontuacao for nome, pontuacao in pontuacoes.items() if pontuacao <= 21}

        if not pontuacoes_validas:
            print("Todos os jogadores ultrapassaram 21. Não há vencedor.")
            return None

        pontuacao_maxima = max(pontuacoes_validas.values())
        vencedores = [nome for nome, pontuacao in pontuacoes_validas.items() if pontuacao == pontuacao_maxima]

        if len(vencedores) == 1:
            print(f"O vencedor é: {vencedores[0]} com um total de {pontuacao_maxima} pontos.")
        else:
            print(f"Empate! Os seguintes jogadores empataram com {pontuacao_maxima} pontos: {', '.join(vencedores)}")

    def jogo_jogadores(self, jogadores):
        for jogador in jogadores:
            print(f'Dados do jogador {jogador.nome}:\n'
                  f'Idade: {jogador.idade}\n'
                  f'Cartas: {jogador.mostrar_cartas()}\n')
            escolha = 0

            while escolha != 2:
                escolha = int(input(f'Jogador {jogador.nome}, o que você quer fazer:\n'
                                    f'[1] Pegar mais cartas | [2] Parar de pegar cartas\n'))
                if escolha == 1:
                    carta = random.choice(self.__deck)
                    jogador.receber_carta(carta)
                    print(f'{jogador.nome}, suas cartas atuais: {jogador.mostrar_cartas()}\n')

                    total_pontos = sum(jogador.mostrar_cartas())
                    if total_pontos > 21:
                        print(f'{jogador.nome}, você ultrapassou 21. Perdeu!\n')
                        break
                elif escolha == 2:
                    print(f'{jogador.nome}, suas cartas atuais: {jogador.mostrar_cartas()}.\n'
                          f'Fim do jogo!')
                    break
                elif escolha != 2:
                    print("Opção inválida. Tente novamente.")

    def dados_jogadores(self):
        jogadores_jogando = int(input("Quantos jogadores vão jogar?\n"))
        if jogadores_jogando >= 2:
            jogadores = []
            for i in range(jogadores_jogando):
                name = input(f"Jogador {i + 1}, qual seu nome?\n")
                try:
                    age = int(input(f"Jogador {name}, qual sua idade?\n"))
                    jogador = Jogador(name, age, 200)
                    jogadores.append(jogador)
                    if age < 18:
                        print("Você deve ter pelo menos 18 anos para jogar.")
                        exit()
                except ValueError:
                    print("Por favor, insira uma idade válida.")

            self.distribuir_cartas(jogadores)

            self.jogo_jogadores(jogadores)
            self.vencedor(jogadores)

        else:
            print("Número mínimo de jogadores: 2.\n"
                  "Tente novamente!\n")
            self.dados_jogadores()

    def menu(self):
        print("Bem-vindo ao nosso Blackjack Game!!")
        print("Escolha uma das opções:\n"
              "[1] Jogar | [2] Regras | [3] Sair")
        opcao = int(input("Digite a opção desejada:\n"))
        if opcao == 1:
            self.dados_jogadores()
            print("Ambos começam com 200 fichas.")
        elif opcao == 2:
            self.regras()
        elif opcao == 3:
            print("Saindo do jogo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            self.menu()


if __name__ == "__main__":
    jogo = Game()
    jogo.menu()
