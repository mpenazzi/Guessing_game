import random

print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual é o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}:".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))

    print("Você digitou ", chute)

    if chute < 1 or chute > 100:
        print("Você errou! Você deve digitar um número entre 1 e 100")
        continue

    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acerto:
        print("Parabéns, você acertou! Você fez {} pontos".format(pontos))
        break
    else:
        if maior:
            print("Você errou! O numéro secreto é menor do que isso ...")
        elif menor:
            print("Você errou! O número secreto é maior do que isso ... ")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim de jogo")
