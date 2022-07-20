import random

def jogar():

    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("             JOGO DA FORCA              ")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]


    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        palpite = input("Digite um letra: ")
        palpite = palpite.strip().upper()
        print("Jogando...")

        if (palpite in palavra_secreta):
            index = 0

            for letra in palavra_secreta:

                if (palpite == letra):
                    letras_acertadas[index] = letra

                index += 1

        else:
            erros += 1
            print("Você errou! faltam {} tentativas".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)




    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")



    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("              FIM DO JOGO               ")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

if __name__ == ("__main__"):
    jogar()
