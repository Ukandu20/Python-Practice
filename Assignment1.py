from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def Bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    p = 2 * dy - dx
    twoDy = 2 * dy
    twoDyMinusDx = 2 * (dy - dx)
    x = x0
    y = y0

    glBegin(GL_POINTS)
    glVertex2i(x, y)
    while x < x1:
        x += 1
        if p < 0:
            p += twoDy
        else:
            y += 1
            p += twoDyMinusDx
        glVertex2i(x, y)
    glEnd()
    glFlush()

def display():
    x0 = 0
    y0 = 0
    x1 = 100
    y1 = 50
    glClear(GL_COLOR_BUFFER_BIT)
    Bresenham(x0, y0, x1, y1)

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 200.0, 0.0, 150.0)

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bresenham's Line Algorithm")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
