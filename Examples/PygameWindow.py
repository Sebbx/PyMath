# Minimal setup to display pygame window

import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = pygame.Color(255, 255, 255)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    pygame.display.update()
pygame.quit()