# Draw simple rectangles on 2d space

import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = pygame.Color(255, 255, 255)

def draw_start(x, y, size):
    pygame.draw.rect(screen, white, (x, y, size, size))

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_start(150, 220, 40)
    draw_start(20, 30, 5)
    draw_start(90, 650, 75)
    draw_start(400, 200, 90)

    pygame.display.update()

pygame.quit()