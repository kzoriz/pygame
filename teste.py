import random
import pygame
import os
import pygame.mixer

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LABIRINTO")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
SIZE = 60
FPS = 60
BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'piso.jpg')), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ratoqueijo.png')), (WIDTH, HEIGHT))
BG3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ratosad.png')), (WIDTH, HEIGHT))
LOGO = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'logo.png')), (518, 150))
PRESS_SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'press_space.png')), (212, 50))
ACHOU = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'achou.png')), (356, 150))
NAO_ACHOU = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'sem_caminho.png')), (468, 75))
Rato = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'rato.png')), (SIZE, SIZE))
Armadilha = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'armadilha.png')), (SIZE, SIZE))
Queijo = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'queijo.png')), (SIZE, SIZE))
Pegada = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pegada.png')), (SIZE, SIZE))
Parede = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'parede.png')), (SIZE, SIZE))
x = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'x.png')), (SIZE, SIZE))

BG_SOUND = pygame.mixer.Sound(os.path.join('Assets/FunnySong.mp3'))
INTRO_SOUND = pygame.mixer.Sound(os.path.join('Assets/intro2.mp3'))
PASSOS_SOUND = pygame.mixer.Sound(os.path.join('Assets/passo.mp3'))
BUZZ_SOUND = pygame.mixer.Sound(os.path.join('Assets/buzz.mp3'))
WINS_SOUND = pygame.mixer.Sound(os.path.join('Assets/wins.mp3'))
FAIL_SOUND = pygame.mixer.Sound(os.path.join('Assets/fail.mp3'))
QISSO_SOUND = pygame.mixer.Sound(os.path.join('Assets/queisso.mp3'))
RAPAZ_SOUND = pygame.mixer.Sound(os.path.join('Assets/Rapaz.mp3'))
SUSPENSE_SOUND = pygame.mixer.Sound(os.path.join('Assets/Suspense.mp3'))

WIN.blit(BG, (0, 0))

TAMANHO = 10
DESTINO = 'D'
CAMINHO = '.'
SEM_SAIDA = 'X'
VAZIO = ' '
INICIO = 'I'
tabuleiro = [[],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             []]


def inicializar_matriz(matriz, TAMANHO):
    for i in range(TAMANHO):
        matriz[i].insert(i, '|')
        for j in range(1, TAMANHO):
            if j == TAMANHO - 1:
                matriz[i].insert(j, '|')
            else:
                x = random.randint(0, 100)
                if x > 70:
                    matriz[i].insert(j, '#')
                else:
                    matriz[i].insert(j, ' ')

    for i in range(TAMANHO):
        matriz[0][i] = '_'
        matriz[TAMANHO - 1][i] = '_'
    return matriz


def gerar_numero(min, max):
    valor = random.randint(0, max - min)
    coordenada = min + valor
    return coordenada


def imprimir(matriz):
    for i in matriz:
        print(i)


def posicao_vazia(linha, coluna):
    for i in range(0, 10):
        for j in range(0, 10):
            if tabuleiro[i][j] == '#':
                WIN.blit(Armadilha, (i * SIZE, j * SIZE))
                pygame.display.update()
            elif tabuleiro[i][j] == 'I':
                WIN.blit(Rato, (i * SIZE, j * SIZE))
                pygame.display.update()
            elif tabuleiro[i][j] == 'D':
                WIN.blit(Queijo, (i * SIZE, j * SIZE))
                pygame.display.update()
            elif tabuleiro[i][j] == '|' or tabuleiro[i][j] == '_':
                WIN.blit(Parede, (i * SIZE, j * SIZE))
                pygame.display.update()
    print("posicao_vazia")
    vazio = False
    if 0 <= linha < TAMANHO and coluna >= 0 and coluna < TAMANHO:
        vazio = (tabuleiro[linha][coluna] == VAZIO)
        imprimir(tabuleiro)
    pygame.display.update()
    return vazio


def tentar_caminho(prox_linha, prox_coluna):
    # print("tentar_caminho")
    achou = False
    pygame.display.update()
    if tabuleiro[prox_linha][prox_coluna] == DESTINO:
        # print("tentar_caminho |")
        achou = True
        WIN.blit(BG2, (0, 0))
        pygame.display.update()
    elif posicao_vazia(prox_linha, prox_coluna):
        # print("tentar_caminho ||")
        tabuleiro[prox_linha][prox_coluna] = CAMINHO
        WIN.blit(Pegada, (prox_linha * SIZE, prox_coluna * SIZE))
        PASSOS_SOUND.play()
        imprimir(tabuleiro)
        pygame.display.update()
        pygame.time.delay(500)
        achou = procurar_caminho(prox_linha, prox_coluna)
        if not achou:
            tabuleiro[prox_linha][prox_coluna] = SEM_SAIDA
            WIN.blit(x, (prox_linha * SIZE, prox_coluna * SIZE))
            SUSPENSE_SOUND.play()
            BUZZ_SOUND.play()
            ran = random.randint(0, 100)
            if ran > 70:
                QISSO_SOUND.play()
            elif ran < 30:
                RAPAZ_SOUND.play()
            imprimir(tabuleiro)
            pygame.display.update()
            pygame.time.delay(500)
    return achou


def procurar_caminho(linha_atual, coluna_atual):
    print("tenta subir")
    prox_linha = linha_atual - 1
    prox_coluna = coluna_atual
    achou = False
    achou = tentar_caminho(prox_linha, prox_coluna)
    if not achou:
        prox_linha = linha_atual + 1
        prox_coluna = coluna_atual
        achou = tentar_caminho(prox_linha, prox_coluna)
    if not achou:
        prox_linha = linha_atual
        prox_coluna = coluna_atual - 1
        achou = tentar_caminho(prox_linha, prox_coluna)
    if not achou:
        prox_linha = linha_atual
        prox_coluna = coluna_atual + 1
        achou = tentar_caminho(prox_linha, prox_coluna)

    return achou


# tabuleiro = inicializar_matriz(tabuleiro, TAMANHO)
# linha_inicio = gerar_numero(1, 8)
# coluna_inicio = gerar_numero(1, 8)
# linha_destino = gerar_numero(1, 8)
# coluna_destino = gerar_numero(1, 8)
#
# tabuleiro[linha_inicio][coluna_inicio] = INICIO
#
# tabuleiro[linha_destino][coluna_destino] = DESTINO
# imprimir(tabuleiro)


# def draw_window():
#     WIN.blit(BG, (0, 0))
#     for i in range(0, 10):
#         for j in range(0, 10):
#             if tabuleiro[i][j] == '#':
#                 WIN.blit(Armadilha, (i * SIZE, j * SIZE))
#                 pygame.display.update()
#             elif tabuleiro[i][j] == 'I':
#                 WIN.blit(Rato, (i * SIZE, j * SIZE))
#             elif tabuleiro[i][j] == 'D':
#                 WIN.blit(Queijo, (i * SIZE, j * SIZE))
#     pygame.display.update()


# BG_SOUND.play()
# achou = procurar_caminho(linha_inicio, coluna_inicio)
#
# if achou:
#     print("achou caminho!")
#     pygame.display.update()
#     WIN.blit(BG2, (0, 0))
#     pygame.display.update()
#     BG_SOUND.stop()
#     WINS_SOUND.play()
# else:
#     print("nao tem caminho!")
#     pygame.display.update()
#     WIN.blit(BG3, (0, 0))
#     pygame.display.update()
#     BG_SOUND.stop()
#     FAIL_SOUND.play()

def main():
    global tabuleiro
    clock = pygame.time.Clock()
    run = True
    WIN.blit(BG, (0, 0))
    WIN.blit(LOGO, (WIDTH/2 - 259, HEIGHT/3 - 75))
    WIN.blit(PRESS_SPACE, (WIDTH/2 - 106, HEIGHT/2 - 25))

    INTRO_SOUND.play()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    INTRO_SOUND.stop()
                    tabuleiro = inicializar_matriz(tabuleiro, TAMANHO)
                    linha_inicio = gerar_numero(1, 8)
                    coluna_inicio = gerar_numero(1, 8)
                    linha_destino = gerar_numero(1, 8)
                    coluna_destino = gerar_numero(1, 8)

                    tabuleiro[linha_inicio][coluna_inicio] = INICIO
                    tabuleiro[linha_destino][coluna_destino] = DESTINO
                    imprimir(tabuleiro)
                    BG_SOUND.play()
                    WIN.blit(BG, (0, 0))
                    achou = procurar_caminho(linha_inicio, coluna_inicio)

                    if achou:
                        print("achou caminho!")
                        # pygame.time.delay(1000)
                        # pygame.display.update()
                        WIN.blit(BG2, (0, 0))
                        WIN.blit(ACHOU, (WIDTH / 2 - 356 / 2, HEIGHT - 250))
                        pygame.display.update()
                        BG_SOUND.stop()
                        WINS_SOUND.play()
                        pygame.time.delay(3000)
                        WIN.blit(PRESS_SPACE, (WIDTH / 2 - 106, HEIGHT / 2 - 25))
                        break
                    else:
                        print("nao tem caminho!")
                        pygame.time.delay(1000)
                        pygame.display.update()
                        WIN.blit(BG3, (0, 0))
                        WIN.blit(NAO_ACHOU, (WIDTH / 2 - 234, HEIGHT - 250))
                        pygame.display.update()
                        BG_SOUND.stop()
                        FAIL_SOUND.play()
                        pygame.time.delay(3000)
                        WIN.blit(PRESS_SPACE, (WIDTH / 2 - 106, HEIGHT / 2 - 25))
                        break

        pygame.display.update()
    main()


if __name__ == "__main__":
    main()
