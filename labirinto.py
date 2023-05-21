import pygame
import time

pygame.init()

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Sprite Piscante")

# Carregando as imagens do sprite
sprite1 = pygame.image.load("Assets/press_space.png")
sprite2 = pygame.image.load("Assets/press_space2.png")

# Configurando o retângulo do sprite
retangulo_sprite = sprite1.get_rect()
retangulo_sprite.center = (largura_tela // 2, altura_tela // 2)

# Definindo o intervalo de tempo para piscar o sprite (em segundos)
intervalo_piscar = 0.5

piscar = True  # Variável para controlar o estado do sprite

tempo_anterior = time.time()

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Verificar se é hora de piscar o sprite
    tempo_atual = time.time()
    if tempo_atual - tempo_anterior >= intervalo_piscar:
        piscar = not piscar
        tempo_anterior = tempo_atual

    # Desenhar o sprite na tela
    tela.fill((255, 255, 255))  # Preencher a tela com branco
    if piscar:
        tela.blit(sprite1, retangulo_sprite)
    else:
        tela.blit(sprite2, retangulo_sprite)

    pygame.display.flip()

pygame.quit()