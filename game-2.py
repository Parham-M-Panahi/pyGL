import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setVertex(self):
        glVertex2i(self.x, self.y)

p1 = Point(50, 10)       
p2 = Point(50, 70)       

def draw():
    glBegin(GL_LINES)
    p1.setVertex()
    p2.setVertex()
    glEnd()
    glFlush()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluOrtho2D(0, 100, 0, 100)

    glClearColor(0.3, 0.5, 1.0, 1.0)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()