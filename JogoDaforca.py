import random


def carregaPalavra():
    palavras = []

    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    sorteio = random.randrange(0, len(palavras))
    palavra_escolhida = palavras[sorteio].upper()

    return palavra_escolhida


def mostraCamposVazios(palavra):
    lista = []

    for letra in palavra:
        lista.append("_")

    return lista


def recebeJogada():
    jogada = input("\n\nQual letra? ")
    print("\n")
    jogada = jogada.strip().upper()
    return jogada


def preencheJogadaCorreta(jogada, letras_corretas, palavra_escolhida):
    indice = 0

    for letra in palavra_escolhida:
        if (jogada == letra):
            letras_corretas[indice] = letra
        indice += 1


def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    palavra_escolhida = carregaPalavra()

    letras = mostraCamposVazios(palavra_escolhida)

    perdeu = False
    venceu = False
    erros = 0
    letras_faltando = len(letras)

    for l in letras:
        print(l, end=' ')

    while (not venceu and not perdeu):

        jogada = recebeJogada()

        if (jogada in palavra_escolhida):

            preencheJogadaCorreta(jogada, letras, palavra_escolhida)

            letras_faltando = str(letras.count('_'))

            if letras_faltando == "0":
                print("\nPARABÉNS!!")
                print("A palavra era {}".format(palavra_escolhida))

        else:

            erros += 1

            for l in letras:
                print(l, end=' ')

            print('\n\nAinda faltam acertar {} letras'.format(letras_faltando))
            print('Você ainda tem {} tentativas\n'.format(7 - erros))

            desenhaForca(erros)

        if erros == 7:
            perdeu = True

        if "_" not in letras:
            venceu = True

        if letras_faltando != "0":
            for l in letras:
                print(l, end=' ')

    if (venceu):
        print("\n\nParabéns, você ganhou!")

    else:
        print("\n\nVocê perdeu!")
        print("A palavra era {}".format(palavra_escolhida))

    print("Fim do jogo")


if (__name__ == '__main__'):
    jogar()