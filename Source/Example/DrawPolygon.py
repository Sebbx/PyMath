# Draw triangles using left mouse button (clicks)

import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = pygame.Color(255, 255, 255)

times_clicked = 0
points = []

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(pygame.mouse.get_pos())

        if len(points) > 2:
            pygame.draw.polygon(screen, white, points)
            points = []

    pygame.display.update()
pygame.quit()