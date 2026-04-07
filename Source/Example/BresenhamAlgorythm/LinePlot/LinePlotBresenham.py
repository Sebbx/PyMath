# Drawing the line pixel by pixel from mouse clicks - the right Bresenham way
from xmlrpc.server import DocXMLRPCServer

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
    x0, y0 = point0
    x1, y1 = point1

    # dx (delta x), distance from x1 to x0
    dx = abs(x1 - x0)

    # sx (step x), direction in x, left or right
    if x0 < x1:
        sx = 1 # right direction
    else:
        sx = -1 # left direction

    # distance from y1 to y0
    dy = -abs(y1 - y0)

    # direction (up or down)
    if y0 < y1:
        sy = 1
    else:
        sy = -1

    err = dx + dy

    current_x = x0
    current_y = y0

    while True:
        screen.set_at((current_x, current_y), white)
        
        # to refresh screen while debugging
        pygame.display.update()
        pygame.event.pump()
        
        if current_x == x1 and current_y == y1:
            break

        e2 = 2 * err

        if e2 >= dy:
            err += dy
            current_x += sx

        if e2 <= dx:
            err += dx
            current_y += sy
            
            
def plot_line2(point0, point1):
    x0, y0 = point0
    x1, y1 = point1
    
    dx = x1 - x0
    dy = y1 - y0
    D = 2 * dy - dx
    y = y0
    
    for x in range(x0, x1):
        screen.set_at((x, y), white)
        if D > 0:
            y = y + 1
            D = D - 2 * dx
            
        else:
            D = D + 2 * dy
        

timesClicked = 0
done = False
while not done:
    for event in pygame.event.get():
        
        # for debugger
        plot_line2((600, 100), (610, 200))
        
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