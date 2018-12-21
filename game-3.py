import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    # pygame initialization
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    # setting up display '2d orthogonal' coord system
    gluOrtho2D(0, 100, 0, 100)
    # setting clear color i.e. background color
    glClearColor(0.3, 0.5, 1.0, 1.0)
    
    # this is the main 'game' loop
    while True:

        # poll events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # render here
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        

        # swap buffers (don't worry about this)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()