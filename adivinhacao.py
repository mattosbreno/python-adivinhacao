import random

print('Bem-vindo ao jogo da adivinhação')

# Seletor de dificuldades
nivel = input("Selecione o nível de dificuldade (Muito Fácil, Fácil, Médio, Difícil, Muito Difícil): ")

if nivel == "Muito Fácil":
    max_tentativas = 20
elif nivel == "Fácil":
    max_tentativas = 15
elif nivel == "Médio":
    max_tentativas = 10
elif nivel == "Difícil":
    max_tentativas = 5
elif nivel == "Muito Difícil":
    max_tentativas = 3
else:
    print("Opção inválida. Será definido o nível Médio por padrão.")
    max_tentativas = 10

# Sistema de pontos + Seletor randomico de número secreto entre 0 e 100
pontos = 1000
numero_secreto = random.randint(0, 100)

# Início do looping para checar o acerto do número
for tentativa in range(1, max_tentativas + 1):
    chute = int(input(f"Tentativa {tentativa}\nDigite um número: "))
    diferenca = abs(chute - numero_secreto)
    pontos -= diferenca

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número secreto em", tentativa, "tentativa(s)!")
        break
    elif chute > numero_secreto:
        print("O chute é maior do que o número secreto.")
    else:
        print("O chute é menor do que o número secreto.")

if tentativa == max_tentativas and chute != numero_secreto:
    print("Suas tentativas acabaram. O número secreto era", numero_secreto)

# Fim do jogo + pontuação total do jogador
print("Pontuação final:", pontos)
print("O jogo foi encerrado.")