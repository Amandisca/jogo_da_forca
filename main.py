import pygame
from pygame.locals import *
from sys import exit

import random

pygame.init()

largura = 600
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Super Forca 2000')

cor = {"azul": [0, 132, 232], "vermelho": [137, 28, 36], "branco": [255, 255, 255]}

#fonte, tamanho, negrito, itálico
fonte = pygame.font.SysFont("arial", 25, True)

relogio = pygame.time.Clock()

sorteio = random.randrange(5, 10)

user_text = ""

print(sorteio)

while True:

    relogio.tick(30)

    mensagem = "Digite sua letra: "

    #mesagem, serrilhamento do texto,
    texto_formatado = fonte.render(mensagem, True, cor["branco"])

    palavra_recebida = fonte.render(user_text, True, cor["branco"])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            user_text = event.unicode

    v = sorteio + 2
    l = largura/v

    tela.fill(cor["azul"])

    tela.blit(texto_formatado, (30, 30))

    tela.blit(palavra_recebida, (195, 30))


    for i in range(sorteio):
        pygame.draw.rect(tela, cor["branco"], (l * (i+1) + i*5, 300, l, 5))

    pygame.display.update()
