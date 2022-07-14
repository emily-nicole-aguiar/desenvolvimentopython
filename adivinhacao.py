import random

print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print("Selecione o seu nível de dificuldade")
print("[1] Fácil  [2] Intermediário  [3] Difícil")
nivel = int(input("Digite o nível: "))

facil = nivel == 1
intermediario = nivel == 2
dificil = nivel == 3
pontos = 1000
if (facil):
    total_de_tentativas = 20
elif (intermediario):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {} restantes".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número de 1 a 100: ")
    print("O número digitado foi: ", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Número inválido!")
        continue

    acertou = chute == numero_secreto
    menor = numero_secreto > chute
    maior = numero_secreto < chute

    if acertou:
        print("---------------------------------")
        print("           Você acertou!")
        print("Sua pontuação final é: {} pontos".format(pontos))
        print("---------------------------------")
        break
    else:
        if menor:
            print("-----------------------------------------------------")
            print("Você errou! Seu número foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("Sua pontuação: {} pontos".format(pontos))

            print("-----------------------------------------------------")

        elif maior:
            print("-----------------------------------------------------")
            print("Você errou! Seu número foi maior que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("Sua pontuação: {} pontos".format(pontos))
            print("-----------------------------------------------------")
print("\n+++++++++++++++++++++++++++++++")
print("O número secreto era: {} ".format(numero_secreto))
print("+++++++++++++++++++++++++++++++\n")
print("---------------------------------")
print("           Fim do jogo           ")
print("---------------------------------")

