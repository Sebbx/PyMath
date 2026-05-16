import pygame
from pygame.locals import *
from OpenGL.GL import *

pygame.init()
pygame.display.set_caption('OpenGL in Python')
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)

class Mesh3D:
    def __init__(self):

        # List of vertices (x, y, z)
        self.vertices = [(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5),
                        (0.5, 0.5, -0.5),
                        (-0.5, 0.5, -0.5)]

        # Triangle indices (index).
        # Every 3 numbers define one triangle.
        # Triangle 1: 0, 2, 3
        # Triangle 2: 0, 3, 1
        self.triangles = [0, 2, 3, 0, 3, 1]

    def draw(self):
        # Loop through triangles.
        for i in range(0, len(self.triangles), 3):

            # Start drawing triangle outline
            glBegin(GL_LINE_LOOP)

            # Get vertex index from triangle array,
            # then use it to access the vertex position

            # First vertex
            glVertex3fv(self.vertices[self.triangles[i]])

            # Second vertex
            glVertex3fv(self.vertices[self.triangles[i +1]])

            # Third Vertex
            glVertex3fv(self.vertices[self.triangles[i + 2]])

            #Finish current shape
            glEnd()


mesh = Mesh3D()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh.draw()
    pygame.display.flip()
pygame.quit()