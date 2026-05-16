import pygame
from pygame.locals import *
from OpenGL.GL import *

pygame.init()
pygame.display.set_caption('OpenGL in Python')
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL) #Set mode as double buffer
white = pygame.Color(255, 255, 255)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clears the screen using the GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT bitmask, which removes color and depth information.
    pygame.display.flip() # flip() replaces the update() method and switches the buffer images so that the background buffer is sent to the screen.
pygame.quit()