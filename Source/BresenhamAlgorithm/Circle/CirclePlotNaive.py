# Drawing the circle pixel by pixel - the wrong way

import pygame
import math

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle Plot Naive")

white = pygame.Color(255, 255, 255)
screen_center = (screen_width * .5, screen_height * .5)

# Circle formula:
#   (x - a)^2 + (y - b)^2 = r^2

# for a and b == 0
#   x^2 + y^2 = r^2
#   y^2 = r^2 - y^2

# now we can square root right side to get y, but it will result in + and - solution (sqrt(4) may be 2 or -2 if it was an unknown)
# Final formula:
#   y = +-sqrt(r^2 - x^2)

def plot_circle(circle_radius):
    for x in range(-circle_radius, circle_radius):
        y = math.sqrt(math.pow(circle_radius, 2) - math.pow(x, 2))
        screen.set_at((int(x + screen_center[0]), int(y + screen_center[1])), white)
        screen.set_at((int(x + screen_center[0]), int(y * -1 + screen_center[1])), white)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        plot_circle(150)
 
    pygame.display.update()
pygame.quit()