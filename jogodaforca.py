def jogar():

    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("             JOGO DA FORCA              ")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

    palavra_secreta ="caramelo"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    print(letras_acertadas)
    while (not acertou and not enforcou):
        palpite = input("Digite um letra: ")
        palpite = palpite.strip()
        print("Jogando...")

        index = 0

        for letra in palavra_secreta:

            if (palpite.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
                letras_faltando = str(letras_acertadas.count("_"))
                print("Ainda faltam {} letras".format(letras_faltando))
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("              FIM DO JOGO               ")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

if __name__ == ("__main__"):
    jogar()
