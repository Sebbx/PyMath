# Drawing the circle pixel by pixel - Midpoint Circle Algorithm

import pygame
import math

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle Plot Naive")

white = pygame.Color(255, 255, 255)
screen_center = (screen_width * .5, screen_height * .5)

def fill_octants(center, x, y):
    cx = int(center[0])
    cy = int(center[1])
    # draw every octant (1/8th of the circle)
    screen.set_at((cx + x, cy + y), white)
    screen.set_at((cx - x, cy + y), white)
    screen.set_at((cx + x, cy - y), white)
    screen.set_at((cx - x, cy - y), white)
    screen.set_at((cx + y, cy + x), white)
    screen.set_at((cx + y, cy - x), white)
    screen.set_at((cx - y, cy + x), white)
    screen.set_at((cx - y, cy - x), white)

# easiest float version
def draw_circle_float(center, radius):
    x = 0
    y = -radius
    while x < -y:
        y_mid = y + 0.5 # Midpoint of pixel (half pixel below), to make it optimal, we want to get rid of a floating operations

        # Check if the midpoint is inside the circle using pythagoras theorem (check if c^2 is shorter than r^2)
        # d - decision parameter
        d = x * x + y_mid * y_mid
        if d > radius * radius:
            y += 1

        fill_octants(center, x, y)
        x += 1

def draw_circle(center, r):
    x = 0
    y = -r

    # Initial value needs to be set
    # d = x^2 + y_mid^2                 | if (d > r^2)
    # d = x^2 + y_mid^2 - r^2           | if (d > 0)
    # d = 0^2 + (-r + 0.5)^2 - r^2      | (a+b)^2 = a^2 + 2ab + b^2
    # d = 0 + [(-r)^2 + 2(-r) * 0.5 + 0.5^2] - r^2
    # d = r^2 - 2r * 0.5 + 0.25 - r^2
    # d = r^2 - r + 0.25 - r^2
    # d = -r + 0.25

    d = -r

    while x < -y:
        if d > 0:
            y += 1
            d += 2 * (x + y) + 1

        else:
            d += 2 * x + 1

        fill_octants(center, x, y)
        x += 1

def draw_circle2(center, r):
    x = 0
    y = r
    fill_octants(center, x, y)

    # Calculating d for NEXT step
    # x = 1
    # y = r - 0.5

    # f(x, y) = x^2 + y^2 - r^2

    # d = 1^2 + (r * 0.5)^2 - r^2
    # d = 1 + r^2 - 2r * 0.5 + 0.5^2 - r^2
    # d = 1 + r + 0.25
    # d = 1.25 - r
    # d = 1 - r | Rounding for fast integer calculations
    d = 1 - r

    # Calculate for the first octant, rest will be taken from symetry
    while y > x:
        # point is inside the circle
        # Updating d for NEXT step when moving EAST
        if d < 0:
            # Current pixel (P): (x, y)
            # Current d evaluated at midpoint (dm): (x+1, y-0.5)
            # Next pixel chosen: (x+1, y)
            # Next d (d_next) must be evaluated at NEXT east midpoint (dme): (x+2, y-0.5)

            # f(x, y) = x^2 + y^2 - r^2
            # d = (x+1)^2 + (y-0.5)^2 - r^2
            # d_next = (x+2)^2 + (y-0.5)^2 - r^2

            # d = d_next - d

            # d = (x+2)^2 + (y-0.5)^2 - r^2 - [(x+1)^2 + (y-0.5)^2 - r^2]
            # d = (x^2 + 2x * 2 + 2^2) + (y^2 - 2y * 0.5 + 0.5^2) - r^2 - (x^2 + 2x * 1 + 1^2) - (y^2 - 2y * 0.5 + 0.5^2) + r^2
            # d = x^2 + 4x + 4 + y^2 - y + 0.25 - x^2 - 2x - 1 - y^2 + y - 0.25
            # d = 4x + 4 - 2x - 1
            # d = 2x + 3

            d += 2 * x + 3
            x += 1

        # point is outside the circle
        # Updating d for NEXT step when moving SOUTH-EAST (d >= 0)
        else:
            # Current pixel (P): (x, y)
            # Current d evaluated at midpoint (dm): (x+1, y-0.5)
            # Next pixel chosen: (x+1, y-1)
            # Next d (d_next) must be evaluated at NEXT east midpoint (dmse): (x+2, y-1.5)

            # f(x, y) = x^2 + y^2 - r^2
            # d = (x+1)^2 + (y-0.5)^2 - r^2
            # d_next = (x+2)^2 + (y-1.5)^2 - r^2

            # d = d_next - d

            # d = (x+2)^2 + (y-1.5)^2 - r^2 - [(x+1)^2 + (y-0.5)^2 - r^2]
            # d = (x^2 + 2x * 2 + 2^2) + (y^2 - 2y * 1.5 + 1.5^2) - r^2 - (x^2 + 2x * 1 + 1^2) - (y^2 - 2y * 0.5 + 0.5^2) + r^2
            # d = x^2 + 4x + 4 + y^2 - 3y + 2.25 - x^2 - 2x - 1 - y^2 + y - 0.25
            # d = 4x + 4 - 3y + 2.25 - 2x - 1 + y - 0.25
            # d = 2x + 6 - 2y - 1
            # d = 2x - 2y + 5
            # d = 2 (x - y) + 5

            d += 2 * (x - y) + 5
            x += 1
            y -= 1

        fill_octants(center, x, y)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        draw_circle2(screen_center, 150)

    pygame.display.update()
pygame.quit()