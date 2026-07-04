import pygame
from pygame.locals import *
from Mesh3D import *

pygame.init()
pygame.display.set_caption('OpenGL in Python')
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)


mesh = Mesh3D()
cube = Cube()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #mesh.draw()

    #Looks the same as mesh, because the camera is in the same place
    cube.draw()
    pygame.display.flip()
pygame.quit()