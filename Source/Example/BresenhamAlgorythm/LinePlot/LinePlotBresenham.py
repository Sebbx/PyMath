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

    # Example we will use in ALL comments below: point0 = (0, 0), point1 = (5, 3)

    # dx (delta x), distance from x1 to x0
    # In our example: dx = abs(5 - 0) = 5
    dx = abs(x1 - x0)

    # sx (step x), direction in x, left or right
    # In our example x0 < x1, so sx = 1 (we move right)
    if x0 < x1:
        sx = 1 # right direction
    else:
        sx = -1 # left direction

    # dy = negative absolute difference in Y.
    # The minus sign is required by the algorithm so that the error calculations work correctly.
    # In our example: dy = -abs(3 - 0) = -3
    dy = -abs(y1 - y0)

    # direction (down or up)
    # In our example y0 < y1, so sy = 1 (we move down)
    if y0 < y1:
        sy = 1 # down
    else:
        sy = -1 # up

    # err = decision variable (error accumulator). A counter that tracks when to move in X or Y.
    # It combines dx and dy to find the best integer path between pixels.
    # This variable is updated every step and is ONLY used to decide when to move X or Y or both.
    # In our example: err = 5 + (-3) = 2
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

        # We multiply err by 2 ONLY so we can avoid using floating-point numbers (like /2).
        # This e2 is used in the two decisions below. It is exactly the same as checking "err >= dy/2" and "err <= dx/2",
        # but without any division and without floats.
        e2 = 2 * err

        # FIRST DECISION: should we move in X direction?
        # We check if e2 >= dy
        # In numbers (our example, first iteration): e2 = 4, dy = -3 → 4 >= -3 is True → we move X and add dy to err
        # This is exactly the same as checking if err >= dy/2 (because 2*err >= dy means err >= dy/2)
        # When this is True, we have crossed the 0.5 pixel boundary in X, so we step X and correct the error.
        if e2 >= dy:
            err += dy
            current_x += sx

        # SECOND DECISION: should we move in Y direction?
        # We check if e2 <= dx
        # In numbers (our example, first iteration): e2 = 4, dx = 5 → 4 <= 5 is True → we move Y and add dx to err
        # This is exactly the same as checking if err <= dx/2 (because 2*err <= dx means err <= dx/2)
        # When this is True, we have crossed the 0.5 pixel boundary in Y, so we step Y and correct the error.
        # Important: this if uses the SAME e2 (and same old err) as the first if - we do NOT use the updated err yet.
        if e2 <= dx:
            err += dx
            current_y += sy

        # After both decisions we have possibly moved X, or Y, or both.
        # Then the loop repeats: we draw the new position and check again.
        # In our full example the pixels drawn are exactly:
        # (0,0) → (1,1) → (2,1) → (3,2) → (4,2) → (5,3)
        # This is the best possible line on a pixel grid.

def plot_line_float(point0, point1):
    x0, y0 = point0
    x1, y1 = point1

    dx = x1 - x0
    dy = y1 - y0

    # Calculate number of steps required
    # We need to iterate by greater delta dimension and round shorter dimension
    steps = max(abs(dx), abs(dy))

    # Calculate the groth for each dimension
    # One dimension will always be = 1, the one that's the delta is greater

    x_step = dx / steps
    y_step = dy / steps

    # Start from the beginning
    current_x = x0
    current_y = y0

    for i in range(int(steps + 1)):
        screen.set_at((int(round(current_x)), int(round(current_y))), white)
        pygame.display.update()
        pygame.event.pump()

        current_x += x_step
        current_y += y_step

timesClicked = 0
done = False
while not done:
    for event in pygame.event.get():

        point0 = (500, 500)
        point1 = (490, 100)
        # for debugger
        plot_line(point0, point1)
        #plot_line_float(point0, point1)
        
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()
pygame.quit()