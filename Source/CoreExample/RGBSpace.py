import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for y in range(screen_height):
        for x in range(screen_width):
            screen.set_at((x,y), pygame.Color(0, int(x/screen_width * 255), int(y/screen_height * 255)))


    pygame.display.update()

pygame.quit()