from random import randint
import pygame
import os
import pygame.mixer

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE SHIPS WAR")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

BORDER = pygame.Rect(WIDTH/2 - 2.5, 0, 5, HEIGHT)

BG_SOUND = pygame.mixer.Sound(os.path.join('Assets/gta.mp3'))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

LIFE_FONT = pygame.font.SysFont('comicsans', 25)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_POSITION = ((WIDTH/4) - SPACESHIP_WIDTH/2, HEIGHT/2 - SPACESHIP_HEIGHT/2)
RED_SPACESHIP_POSITION = ((WIDTH/4)*3 - SPACESHIP_WIDTH/2, HEIGHT/2 - SPACESHIP_HEIGHT/2)
'''

YELLOW_SPACESHIP_POSITION = (random.randint(SPACESHIP_HEIGHT, BORDER[0] - SPACESHIP_HEIGHT),
                             random.randint(20, HEIGHT - SPACESHIP_WIDTH))
RED_SPACESHIP_POSITION = (random.randint(BORDER[0] + 20, WIDTH - SPACESHIP_HEIGHT), 
                          random.randint(20, HEIGHT - SPACESHIP_WIDTH))
'''
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_SCALE = pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP_ROTATE = pygame.transform.rotate(YELLOW_SPACESHIP_SCALE, 90)
YELLOW_SPACESHIP = YELLOW_SPACESHIP_ROTATE

RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_SCALE = pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_ROTATE = pygame.transform.rotate(RED_SPACESHIP_SCALE, 270)
RED_SPACESHIP = RED_SPACESHIP_ROTATE


def draw_window(red, yellow, yellow_bullets, red_bullets, yellow_life, red_life):
    WIN.blit(SPACE, (0, 0))
    #WIN.fill(WHITE)
    pygame.draw.rect(WIN, WHITE, BORDER)

    red_life_text = LIFE_FONT.render("RED: " + str(red_life), True, WHITE)
    yellow_life_text = LIFE_FONT.render("YELLOW: " + str(yellow_life), True, WHITE)

    WIN.blit(yellow_life_text, (10, 10))
    WIN.blit(red_life_text, (WIDTH - 10 - red_life_text.get_width(), 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_w] and yellow.y > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + SPACESHIP_HEIGHT < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_s] and yellow.y + SPACESHIP_WIDTH < HEIGHT:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER.x + VEL:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_UP] and red.y > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + SPACESHIP_HEIGHT < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y + SPACESHIP_WIDTH < HEIGHT:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, True, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)


def main():

    red = pygame.Rect(RED_SPACESHIP_POSITION[0], RED_SPACESHIP_POSITION[1], SPACESHIP_HEIGHT, SPACESHIP_WIDTH)
    yellow = pygame.Rect(YELLOW_SPACESHIP_POSITION[0], YELLOW_SPACESHIP_POSITION[1], SPACESHIP_HEIGHT, SPACESHIP_WIDTH)

    yellow_bullets = []
    red_bullets = []

    yellow_life = 10
    red_life = 10

    clock = pygame.time.Clock()
    run = True
    BG_SOUND.play()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.height, yellow.y + (yellow.height/2) + 5, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + (red.height / 2) + 5, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_life -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_life -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_life <= 0:
            winner_text = "Yellow Wins!"
        if yellow_life <= 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, yellow_bullets, red_bullets, yellow_life, red_life)

    main()
    #pygame.quit()


if __name__ == "__main__":
    main()
