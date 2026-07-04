from OpenGL.GL import *
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

class Cube(Mesh3D):
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
                         (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
                         (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
                         (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5),
                         (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5),
                         (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5)]

        self.triangles = [0, 2, 3, 0, 3, 1,
                          8, 4, 5, 8, 5, 9,
                          10, 6, 7, 10, 7, 11,
                          12, 13, 14, 12, 14, 15,
                          16, 17, 18, 16, 18, 19,
                          20, 21, 22, 20, 22, 23]

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
