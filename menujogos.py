import adivinhacao
import jogodaforca

def menujogos():
    print("*************************************************")
    print("              SELECIONE SEU JOGO                 ")
    print("*************************************************")

    print("\nxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX")
    print("    [1] Adivinhação         [2] Forca")
    print("xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX\n")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        print("Você selecionou o jogo de Adivinhação!")
        adivinhacao.jogar()
    elif opcao == 2:
        print("Você selecionou o jogo da Forca!")
        jogodaforca.jogar()
    else:
        print("Opção inválida!")
        return menujogos()

if __name__ == ("__main__"):
    menujogos()


