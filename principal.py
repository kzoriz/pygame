import pygame
from pygame.locals import *
import sys
from random import randint
from sys import exit
import pygame.mixer
#Dimensão da tela
largura = 640
altura = 480

#Cores
preto = (0, 0, 0)
cinza = (119, 136, 153)
branco = (255, 255, 255)
verde = (0, 255, 0)
verde_jogo = (155, 196, 4)
# formas
espessura = 20

#posição

x = largura/2 - 10
y = altura/2 - 10

x_circle = randint(32, 608)
y_circle = randint(32, 448)


pygame.mixer.init()
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.load("Assets/gta.mp3")
pygame.mixer.music.play(-1)
pygame.init()
tela = pygame.display.set_mode((largura, altura))
tela.fill(verde_jogo)
pygame.display.set_caption('Kzoriz')
icone = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(icone)

relogio = pygame.time.Clock()

font = pygame.font.Font(None, 36)
text = font.render("Você Bateu!!", True, (0, 0, 0))

up = False
down = False
left = False
right = True
direcao = "RIGHT"

while True:
    relogio.tick(60)
    tela.fill(verde_jogo)
    #fundo = pygame.image.load("fundo.jpg").convert()
    #fundo = pygame.transform.scale(fundo, (largura, altura))
    #tela.blit(fundo, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT and direcao != "LEFT":
                up = False
                right = True
                down = False
                left = False
                direcao = "RIGHT"
            if event.key == K_DOWN and direcao != "UP":
                down = True
                up = False
                right = False
                left = False
                direcao = "DOWN"
            if event.key == K_UP and direcao != "DOWN":
                up = True
                down = False
                right = False
                left = False
                direcao = "UP"
            if event.key == K_LEFT and direcao != "RIGHT":
                up = False
                down = False
                left = True
                right = False
                direcao = "LEFT"

    ret = pygame.draw.rect(tela, (0, 0, 200), (x, y, 20, 20))
    circle = pygame.draw.circle(tela, (255, 0, 0), (x_circle, y_circle), 10)

    if ret.colliderect(circle):
        x_circle = randint(30, 610)
        y_circle = randint(30, 450)

    pygame.draw.line(tela, (0, 0, 0), (18, 20), (largura - 18, 20), 5)# horizontal cima
    pygame.draw.line(tela, (0, 0, 0), (18, altura - 20), (largura - 18, altura - 20), 5)#horizontal baixo
    pygame.draw.line(tela, (0, 0, 0), (largura - 20, altura - 20), (largura - 20, 20), 5)#lateral direita
    pygame.draw.line(tela, (0, 0, 0), (20, 20), (20, altura - 20), 5)#lateral esquerda
    # tela, cor, posição x e y, altura e largura

    if down:
        y = y + 2
    elif up:
        y = y - 2
    elif left:
        x = x - 2
    elif right:
        x = x + 2
    if y >= altura - (20 + 20):
        x = largura / 2 - 10
        y = altura / 2 - 10
        tela.blit(text, (largura / 2 - 80, altura / 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        right = True
        left = False
        up = False
        down = False
        direcao = "RIGHT"
    elif y <= 20:
        x = largura / 2 - 10
        y = altura / 2 - 10
        tela.blit(text, (largura / 2 - 80, altura / 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        right = True
        left = False
        up = False
        down = False
        direcao = "RIGHT"
    elif x >= largura - (20 + 20):
        x = largura / 2 - 10
        y = altura / 2 - 10
        tela.blit(text, (largura / 2 - 80, altura / 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        right = True
        left = False
        up = False
        down = False
        direcao = "RIGHT"
    elif x <= 20:
        x = largura / 2 - 10
        y = altura / 2 - 10
        tela.blit(text, (largura / 2 - 80, altura / 2))
        pygame.display.flip()
        pygame.time.wait(1000)
        right = True
        left = False
        up = False
        down = False
        direcao = "RIGHT"



    '''
    # tela ,cor, posicao, e raio
    pygame.draw.circle(tela, (150, 0, 0), (300, 300), 40)
    # tela, cor, inicio , fim e espessura
    pygame.draw.line(tela, (0, 0, 0), (largura/2, 0), (largura/2, altura), 5)
    '''
    pygame.display.update()