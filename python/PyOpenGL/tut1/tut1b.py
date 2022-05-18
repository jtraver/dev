#!/usr/bin/env python2

# https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/
# pygame 2.1.2 (SDL 2.0.18, Python 3.7.3)
# Hello from the pygame community. https://www.pygame.org/contribute.html

# import pygame


import pygame
from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLU import *
import OpenGL


vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

def Cube():
    OpenGL.GL.glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            OpenGL.GL.glVertex3fv(vertices[vertex])
    OpenGL.GL.glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    OpenGL.gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    OpenGL.GL.glTranslatef(0.0,0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        OpenGL.GL.glRotatef(1, 3, 1, 1)
        OpenGL.GL.glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
