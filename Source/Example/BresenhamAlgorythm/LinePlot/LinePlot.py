# Drawing the line pixel by pixel - the wrong way

import pygame
pygame.init()
pygame.display.set_caption("Line Plot")
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

x_origin_no_offset = int(screen_width / 2)
y_origin_no_offset = int(screen_height / 2)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # X Axis
    for x in range(-400, 400):
        screen.set_at((x + x_origin_no_offset, y_origin_no_offset), white)

    # Y Axis
    for y in range(-300, 300):
        screen.set_at((x_origin_no_offset, y + y_origin_no_offset), white)

    # Linear Function
    for x in range(-400, 400):
        #y = 2 * x + 4 # this seems kinda okay
        #y = int(0.05 * x) - 100 # this is fine
        #y = 5 * x + 800 # here you can see the issue
        y = 10 * x + 800 # here you can clearly see the issue

        screen.set_at((x + x_origin_no_offset, y + y_origin_no_offset), green)

    pygame.display.update()
pygame.quit()