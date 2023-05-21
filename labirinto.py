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
BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'piso.jpg')), (WIDTH, HEIGHT + 10))
Rato = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'rato.png')), (SIZE, SIZE))
Armadilha = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'armadilha.png')), (SIZE, SIZE))
Queijo = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'queijo.png')), (SIZE, SIZE))
Pegada = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pegada.png')), (SIZE, SIZE))


def draw_window():
    WIN.blit(BG, (0, 0))
    armadilhas = []
    for i in range(0, 10):
        for j in range(0, 10):
            if random.randint(0, 100) > SIZE:
                WIN.blit(Armadilha, (i * SIZE, j * SIZE))
                armadilhas.append(f'{i * SIZE},{j * SIZE}')
    while True:
        pos_x_rato = random.randint(0, 9) * SIZE
        pos_y_rato = random.randint(0, 9) * SIZE
        pos_rato = f'{pos_x_rato},{pos_y_rato}'
        if pos_rato not in armadilhas:
            break
        else:
            print(f"Rato Colidiu! {pos_x_rato},{pos_y_rato}")
    print("pos_rato: ", pos_rato)
    WIN.blit(Rato, (pos_x_rato, pos_y_rato))
    while True:
        pos_x_queijo = random.randint(0, 9) * SIZE
        pos_y_queijo = random.randint(0, 9) * SIZE
        pos_queijo = f'{pos_x_queijo},{pos_y_queijo}'
        if pos_queijo not in armadilhas and pos_queijo != pos_rato:
            break
        else:
            print(f"Queijo colidiu! {pos_x_queijo},{pos_y_queijo}")
    print("pos_queijo: ", pos_queijo)
    WIN.blit(Queijo, (pos_x_queijo, pos_y_queijo))
    # busca
    pos_atual = f"{pos_x_rato}{pos_y_rato}"
    pos_x = pos_x_rato
    pos_y = pos_y_rato
    prox_up = f"{pos_x},{pos_y - SIZE}"
    prox_left = f"{pos_x - SIZE},{pos_y}"
    prox_down = f"{pos_x},{pos_y + SIZE}"
    prox_right = f"{pos_x + SIZE},{pos_y}"
    up = True
    right = False
    down = False
    left = False
    print(len(armadilhas))
    print(armadilhas)

    # def tentar_caminho(x, y, tamanho, lista):
    #     vazio = False
    #     posicao = f"{x // 70},{(y // 70) - 1}"
    #     print("posição: ", posicao)
    #     if posicao not in lista and 0 <= y - 70 <= tamanho:
    #         vazio = True
    #     return vazio
    # def caminho_up(pos_x, pos_y, armadilhas):
    #     if f"{pos_x},{pos_y}" not in armadilhas:


    def verificar(pos_x, pos_y, z):
        achou = False
        prox_up = f"{pos_x},{pos_y - SIZE}"
        prox_left = f"{pos_x - SIZE},{pos_y}"
        prox_down = f"{pos_x},{pos_y + SIZE}"
        prox_right = f"{pos_x + SIZE},{pos_y}"
        if prox_up == z or prox_left == z or prox_down == z or prox_right == z:
            achou = True
            return achou
        else:
            return achou

    while True:
        print(f"pos_atual: {pos_x},{pos_y}", )
        if verificar(pos_x_rato, pos_y_rato, pos_queijo):
            print("AChou!")
            break
        while f"{pos_x},{pos_y - SIZE}" not in armadilhas and pos_y - SIZE >= 0 and verificar(pos_x, pos_y, pos_queijo) == False:
            print(f"up: {pos_x},{pos_y - SIZE}")
            pos_y = pos_y - SIZE
            WIN.blit(Pegada, (pos_x, pos_y))
            if verificar(pos_x, pos_y, pos_queijo):
                print("AChou!")
                break
        while f"{pos_x - SIZE},{pos_y}" not in armadilhas and pos_x - SIZE >= 0 and verificar(pos_x, pos_y, pos_queijo) == False:
            print(f"left: {pos_x - SIZE},{pos_y}")
            pos_x = pos_x - SIZE
            WIN.blit(Pegada, (pos_x, pos_y))

            if verificar(pos_x, pos_y, pos_queijo):
                print("AChou!")
                break
        while f"{pos_x},{pos_y + SIZE}" not in armadilhas and pos_y + SIZE <= 530 and verificar(pos_x, pos_y, pos_queijo) == False:
            print(f"down: {pos_x},{pos_y + SIZE}")
            pos_y = pos_y + SIZE
            WIN.blit(Pegada, (pos_x, pos_y))

            if verificar(pos_x, pos_y, pos_queijo):
                print("AChou!")
                break
        while f"{pos_x + SIZE},{pos_y}" not in armadilhas and pos_x + SIZE <= 530 and verificar(pos_x, pos_y, pos_queijo) == False:
            print(f"right: {pos_x + SIZE},{pos_y}")
            pos_x = pos_x + SIZE
            WIN.blit(Pegada, (pos_x, pos_y))

            if verificar(pos_x, pos_y, pos_queijo):
                print("AChou!")
                break
        if verificar(pos_x, pos_y, pos_queijo):
            print("Parabéns!")
            break
        else:
            print(f"UP: {pos_x},{pos_y - SIZE}")
            print(f"LEFT: {pos_x - SIZE},{pos_y}")
            print(f"DOWN: {pos_x},{pos_y + SIZE}")
            print(f"RIGTH: {pos_x + SIZE},{pos_y}")
            print(armadilhas)
            print("sem Saida")
            break
    # pygame.time.delay(2000)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    draw_window()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        # pygame.time.delay(2000)
        pygame.display.update()
    main()


if __name__ == "__main__":
    main()
