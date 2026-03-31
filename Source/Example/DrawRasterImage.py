# Drawing a raster image on top of another image

import pygame
pygame.init()

screen_width = 800
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Mighty Kicia on Throne")

# ".." goes back in hierarchy
background = pygame.image.load("../../Asset/Image/KratosThrone.jpg")
mighty_kicia = pygame.image.load("../../Asset/Image/MightyKicia.png")

screen.blit(background, (0, 0))
screen.blit(mighty_kicia, (400, 75))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.update()
pygame.quit()