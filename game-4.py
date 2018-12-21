'''
    added event handling
    added box and grid rendering

'''
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# this f'n does the basic pygame initialization stuff.


def init():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # setting up display '2d orthogonal' coord system
    gluOrtho2D(-100, 100, -100, 100)
    # setting clear color i.e. background color
    glClearColor(0.3, 0.5, 1.0, 1.0)

# this one handles all keyboard and mouse events.


def eventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        print event


def drawGrid():
    glColor3fv([1.0, 0.0, 0.0])
    glBegin(GL_LINES)
    glVertex2iv([0, -100])
    glVertex2iv([0, 100])
    glVertex2iv([-100, 0])
    glVertex2iv([100, 0])
    glEnd()

def drawBox():
    glColor3fv([0.0, 1.0, 1.0])
    glPolygonMode(GL_FRONT, GL_LINE)
    glBegin(GL_TRIANGLES)
    glVertex2iv([0, 0])
    glVertex2iv([20, 0])
    glVertex2iv([20, 20])
    glVertex2iv([0, 0])
    glVertex2iv([20, 20])
    glVertex2iv([0, 20])
    glEnd()


# this one draw's stuff to the screen.
def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    drawGrid()
    drawBox()



def main():
    # pygame initialization
    init()

    # this is the main 'game' loop
    while True:

        # poll events here
        eventHandler()

        # render here
        render()

        # swap buffers (don't worry about this)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
