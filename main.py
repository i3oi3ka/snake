import pygame
import random
import time

speed_of_snake = 13

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

white_color = pygame.Color(255, 255, 255)
black_color = pygame.Color(0, 0, 0)
red_color = pygame.Color(220, 20, 0)
green_color = pygame.Color(124, 252, 0)

pygame.init()

display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.transform.scale(pygame.image.load('BG.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("python - Snake")
game_clock = pygame.time.Clock()

position_of_snake = [450, 500]
body_of_snake = []
for i in range(5):
    body_of_snake.append([position_of_snake[0]+10*i, position_of_snake[1]])
initial_direction = 'LEFT'
snake_direction = initial_direction

game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    display_screen.fill(white_color)
    display_screen.blit(bg, (0, 0))

    if initial_direction == 'UP':
        position_of_snake[1] -= 10
    if initial_direction == 'DOWN':
        position_of_snake[1] += 10
    if initial_direction == 'LEFT':
        position_of_snake[0] -= 10
    if initial_direction == 'RIGHT':
        position_of_snake[0] += 10

    body_of_snake.insert(0, list(position_of_snake))
    body_of_snake.pop()

    for position in body_of_snake:
        pygame.draw.rect(display_screen, red_color, pygame.Rect(position[0], position[1], 10, 10))
    pygame.display.update()
    game_clock.tick(speed_of_snake)
pygame.quit()
