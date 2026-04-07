# Drawing the line pixel by pixel from mouse clicks - the wrong way

import pygame
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Line Plot")
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

def plot_line(point0, point1):
    # for loop requires x0 being smaller than x1. This is fixing the not being able to draw on the left side bug
    if point0[0] > point1[0]:
        temp = point0
        point0 = point1
        point1 = temp

    x0, y0 = point0
    x1, y1 = point1

    # slope = rise / run
    m = (y1 - y0) / (x1 - x0)

    # c = y intercept point
    # Derived from the equation: y = mx + c == c = y - mx
    # With known slope (m) we can calculate c (intercept point) with both points, (x0, y0 or x1, y1), result will be the same
    c = y0 - m * x0

    for x in range(x0, x1):
        y = m * x + c
        screen.set_at((int(x), int(y)), white)


timesClicked = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if timesClicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            timesClicked += 1

            if timesClicked > 1:
                plot_line(point1, point2)
                timesClicked = 0

    pygame.display.update()
pygame.quit()