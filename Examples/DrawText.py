# Draw line using left mouse button (clicks)

import pygame
pygame.init()
pygame.font.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
font = pygame.font.SysFont("Times New Roman", 100)

text = font.render("Hello World", False, white)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(text, (10, 10))

    pygame.display.update()
pygame.quit()