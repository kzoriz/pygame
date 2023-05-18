import random

import pygame
import os
import pygame.mixer

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LABIRINTO")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'piso.jpg')), (WIDTH, HEIGHT + 10))
Rato = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'rato.png')), (70, 70))
Armadilha = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'armadilha.png')), (70, 70))
Queijo = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'queijo.png')), (70, 70))
Pegada = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'pegada.png')), (70, 70))


def draw_window():
    WIN.blit(BG, (0, 0))
    armadilhas = []
    for i in range(0, 10):
        for j in range(0, 10):
            if random.randint(0, 100) > 70:
                WIN.blit(Armadilha, (i * 70, j * 70))
                armadilhas.append(f'{i * 70},{j * 70}')
    while True:
        pos_x_rato = random.randint(0, 9) * 70
        pos_y_rato = random.randint(0, 9) * 70
        pos_rato = f'{pos_x_rato},{pos_y_rato}'
        if pos_rato not in armadilhas:
            break
        else:
            print(f"Rato Colidiu! {pos_x_rato},{pos_y_rato}")
    print("pos_rato: ", pos_rato)
    WIN.blit(Rato, (pos_x_rato, pos_y_rato))
    while True:
        pos_x_queijo = random.randint(0, 9) * 70
        pos_y_queijo = random.randint(0, 9) * 70
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
    prox_up = f"{pos_x},{pos_y - 70}"
    prox_left = f"{pos_x - 70},{pos_y}"
    prox_down = f"{pos_x},{pos_y + 70}"
    prox_right = f"{pos_x + 70},{pos_y}"
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

    def verificar(pos_x, pos_y, z):
        achou = False
        prox_up = f"{pos_x},{pos_y - 70}"
        prox_left = f"{pos_x - 70},{pos_y}"
        prox_down = f"{pos_x},{pos_y + 70}"
        prox_right = f"{pos_x + 70},{pos_y}"
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

        while f"{pos_x},{pos_y - 70}" not in armadilhas and pos_y - 70 >= 0 and verificar(pos_x, pos_y, pos_queijo) == False:
            print(f"up: {pos_x},{pos_y}")
            pos_y = pos_y - 70
            WIN.blit(Pegada, (pos_x, pos_y))
            if verificar(pos_x, pos_y, pos_queijo):
                print("AChou!")
                break
        while f"{pos_x - 70},{pos_y}" not in armadilhas and pos_x - 70 >= 0 and verificar(pos_x, pos_y, pos_queijo) == False:
            print(f"left: {pos_x},{pos_y}")
            pos_x = pos_x - 70
            WIN.blit(Pegada, (pos_x, pos_y))
            if verificar(pos_x, pos_y, pos_queijo):
                print("AChou!")
                break
        while f"{pos_x},{pos_y + 70}" not in armadilhas and pos_y + 70 <= 630 and verificar(pos_x, pos_y, pos_queijo) == False:
            print(f"down: {pos_x},{pos_y}")
            pos_y = pos_y + 70
            WIN.blit(Pegada, (pos_x, pos_y))
            if verificar(pos_x, pos_y, pos_queijo):
                print("AChou!")
                break
        while f"{pos_x + 70},{pos_y}" not in armadilhas and pos_x + 70 <= 630 and verificar(pos_x, pos_y, pos_queijo) == False:
            print(f"right: {pos_x},{pos_y}")
            pos_x = pos_x + 70
            WIN.blit(Pegada, (pos_x, pos_y))
            if verificar(pos_x, pos_y, pos_queijo):
                print("AChou!")
                break
        if verificar(pos_x, pos_y, pos_queijo):
            print("Parabéns!")
            break
        else:
            print(f"{pos_x},{pos_y}")
            print(armadilhas)
            print("sem Saida")
            break

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

    main()


if __name__ == "__main__":
    main()
