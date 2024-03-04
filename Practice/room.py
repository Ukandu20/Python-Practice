import sys
import pygame
from pygame.locals import QUIT
from OpenGL.GL import (GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_PROJECTION, GL_MODELVIEW,
                       glClear, glViewport, glMatrixMode, glLoadIdentity, glColor3f,
                       glPushMatrix, glPopMatrix, glTranslated, glScaled, glRotated)
from OpenGL.GLUT import (glutSolidSphere, glutSolidCube)
from OpenGL.GLU import gluPerspective

slices = 16
stacks = 16
r = 1.000
g = 0.000
a = 0
b = 0

def resize(width, height):
    ar = float(width) / float(height)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, ar, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    global slices, stacks, r, g, a, b
    t = pygame.time.get_ticks() / 1000.0
    a = t * 90.0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #flower


glColor3f(0.000, 0.502, 0.000);
glPushMatrix();
glTranslated(-2.8,-1.2,-7);
glScaled(.3,.3,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();

glColor3f(0.000, 0.502, 0.000);
glPushMatrix();
glTranslated(-3.1,-1.2,-7);
glScaled(.3,.3,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();

glColor3f(0.000, 0.502, 0.000);
glPushMatrix();
glTranslated(-2.5,-1.2,-7);
glScaled(.3,.3,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();


glColor3f(0.000, 0.502, 0.000);
glPushMatrix();
glTranslated(-2.74,-.85,-7);
glScaled(.3,.3,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();


glColor3f(0.957, 0.643, 0.376);
glPushMatrix();
glTranslated(-2.8,-2.1,-7);
glScaled(.2,.3,0);
glutSolidCube(3);
glPopMatrix();

glColor3f(0.545, 0.271, 0.075);
glPushMatrix();
glTranslated(-2.8,-1.5,-7);
glScaled(.2,.6,-0);
glutSolidCube(.5);
glPopMatrix();


#paint

glColor3f(0.545, 0.271, 0.075);
glPushMatrix();
glTranslated(-3,.6,-7);
glScaled(.8,.4,0-.08);
glutSolidCube(3);
glPopMatrix();

glColor3f(1,1,1);
glPushMatrix();
glTranslated(-3,.6,-7);
glScaled(1.2,.05,0);
glutSolidCube(2);
glPopMatrix();


glColor3f(1,1,1);
glPushMatrix();
glTranslated(-3,.6,-7);
glScaled(0.05,.6,0);
glutSolidCube(2);
glPopMatrix();

glColor3f(1,1,1);
glPushMatrix();
glTranslated(-3.6,.63,-7);
glScaled(0.05,.25,0);
glutSolidCube(2);
glPopMatrix();


glColor3f(1,1,1);
glPushMatrix();
glTranslated(-2.4,.63,-7);
glScaled(0.05,.25,0);
glutSolidCube(2);
glPopMatrix();



#window


glColor3f(0,0,0);   # h bar
glPushMatrix();
glTranslated(-3,2.4,-7);
glScaled(1,.05,0);
glutSolidCube(2);
glPopMatrix();

glColor3f(0,0,0);   #h bar2
glPushMatrix();
glTranslated(-3,1.6,-7);
glScaled(1,.03,0);
glutSolidCube(2);
glPopMatrix();

glColor3f(0,0,0);   # h bar3
glPushMatrix();
glTranslated(-3,3.2,-7);
glScaled(1,.03,0);
glutSolidCube(2);
glPopMatrix();

#v bar


glColor3f(0,0,0);   
glPushMatrix();
glTranslated(-3,2.4,-7);
glScaled(0.05,.8,0);
glutSolidCube(2);
glPopMatrix();



#sun

glColor3f(1.000, 0.647, 0.000); 
glPushMatrix();
glTranslated(-3.7,2.8,-7);
glScaled(0.3,0.3,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();



glColor3f(0.529, 0.808, 0.980);
glPushMatrix();
glTranslated(-3,2.4,-7);
glScaled(1,.8,0);
glutSolidCube(2);
glPopMatrix();

#door


glColor3f(0,0,0);
glPushMatrix();
glTranslated(2,.3,-7);
glScaled(0.08,.08,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();


glColor3f(0.627, 0.322, 0.176);
glPushMatrix();
glTranslated(3,.4,-7);
glScaled(.6,1,-.0);
glutSolidCube(4);
glPopMatrix();



glColor3f(0.412, 0.412, 0.412);
glPushMatrix();
glTranslated(3,-1.65,-7);
glScaled(.6,0.1,-.0);
glutSolidCube(4);
glPopMatrix();

#right speaker circle

glColor3f(0,0,0);
glPushMatrix();
glTranslated(1,-.69,-7);
glScaled(0.08,.08,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(1,-.54,-7);
glScaled(0.08,.08,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();


#left speaker circle

glColor3f(0,0,0);
glPushMatrix();
glTranslated(-1,-.69,-7);
glScaled(0.08,.08,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(-1,-.54,-7);
glScaled(0.08,.08,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();


#right speaker

glColor3f(0.412, 0.412, 0.412);
glPushMatrix();
glTranslated(1,-.69,-7);
glScaled(.1,.2,0);
glutSolidCube(3);
glPopMatrix();


#left speaker

glColor3f(0.412, 0.412, 0.412);
glPushMatrix();
glTranslated(-1,-.69,-7);
glScaled(.1,.2,0);
glutSolidCube(3);
glPopMatrix();


#desk 2

glColor3f(0.824, 0.412, 0.118);
glPushMatrix();
glTranslated(0,-1,-7);
glScaled(.5,0.1,1);
glutSolidCube(3);
glPopMatrix();




#chair

glColor3f(0.545, 0.271, 0.075);
glPushMatrix();
glTranslated(-0.3,-1.9,-7);
glScaled(0.3,0.1,0);
glutSolidCube(3);
glPopMatrix();


#chair leg

glColor3f(0,0,0);
glPushMatrix();
glTranslated(-0.3,-2.4,-7);
glScaled(.1,.4,0);
glutSolidCube(2);
glPopMatrix();

#chair leg base

glColor3f(0,0,0);
glPushMatrix();
glTranslated(-0.3,-2.8,-7);
glScaled(.3,.05,0);
glutSolidCube(2);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(-0.3,-2.9,-7);
glScaled(0.08,.08,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(-0.1,-2.9,-7);
glScaled(0.08,.08,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(-0.5,-2.9,-7);
glScaled(0.08,.08,0);
glutSolidSphere(.9,stacks, slices);
glPopMatrix();


#desk

glColor3f(0.545, 0.271, 0.075);
glPushMatrix();
glTranslated(0,-1,-7);
glScaled(1,0.1,1);
glutSolidCube(3);
glRotated(90,8,8,8);
glPopMatrix();

#leg left

glColor3f(0,0,0);
glPushMatrix();
glTranslated(-1.5,-2.85,-7);
glScaled(.09,.04,0);
glutSolidCube(3);
glPopMatrix();


glColor3f(0.545, 0.271, 0.075);
glPushMatrix();
glTranslated(-1.5,-2,-7);
glScaled(.1,.6,0);
glutSolidCube(3);
glPopMatrix();




#leg right

glColor3f(0,0,0);
glPushMatrix();
glTranslated(1.5,-2.85,-7);
glScaled(.09,.04,0);
glutSolidCube(3);
glPopMatrix();

glColor3f(0.545, 0.271, 0.075);
glPushMatrix();
glTranslated(1.5,-2,-7);
glScaled(.1,.6,0);
glutSolidCube(3);
glPopMatrix();



#power button
glColor3f(0,0,0);
glPushMatrix();
glTranslated(0.8,-1.9,-7);
glScaled(.1,.1,0);
glutSolidCube(.7);
glPopMatrix();

#red 1.000, 0.000, 0.000
#geen  0.498, 1.000, 0.000
glColor3f(r,g,0);
glPushMatrix();
glTranslated(0.4,-1.9,-7);
glScaled(.1,.1,0);
glutSolidCube(.7);
glPopMatrix();


#slice
glColor3f(0,0,0);
glPushMatrix();
glTranslated(0.6,-2.1,-7);
glScaled(.6,.05,0);
glutSolidCube(.7);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(0.6,-2.2,-7);
glScaled(.6,.05,0);
glutSolidCube(.7);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(0.6,-2.3,-7);
glScaled(.6,.05,0);
glutSolidCube(.7);
glPopMatrix();

#pc

glColor3f(0.412, 0.412, 0.412);
glPushMatrix();
glTranslated(0.6,-2.1,-7);
glScaled(.2,.3,0);
glutSolidCube(3);
glPopMatrix();

#tv legs right



glColor3f(0,0,0);
glPushMatrix();
glTranslated(0,-.8,-7);
glScaled(0.4,.04,0);
glutSolidCube(3);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(0.3,-.65,-7);
glScaled(.2,.6,0);
glutSolidCube(.5);
glPopMatrix();

#tv legs right
glColor3f(0,0,0);
glPushMatrix();
glTranslated(-0.3,-.65,-7);
glScaled(.2,.6,0);
glutSolidCube(.5);
glPopMatrix();



#tv


glColor3f(1,1,1);
glPushMatrix();
glTranslated(0+b,-.1,-7);
glScaled(.1,.1,0);
glutSolidSphere(1,stacks, slices);
glPopMatrix();

glColor3f(1,1,1);
glPushMatrix();
glTranslated(0-b,.2,-7);
glScaled(.1,.1,0);
glutSolidSphere(1,stacks, slices);
glPopMatrix();

glColor3f(0,0,0);
glPushMatrix();
glTranslated(0,.1,-7);
glScaled(.4,.3,0);
glutSolidCube(3);
glPopMatrix();


#frame

glColor3f(0.412, 0.412, 0.412);
glPushMatrix();
glTranslated(0,.1,-7);
glScaled(.6,.4,0);
glutSolidCube(3);
glPopMatrix();

#background top

glColor3f(0.961, 0.871, 0.702);
glPushMatrix();
glTranslated(0.2,5,-20);
glScaled(6,4,.3);
glutSolidCube(5);
glPopMatrix();



#floooor


glColor3f(0.871, 0.722, 0.529);
glPushMatrix();
glTranslated(0,-6,-20);
glScaled(10,4,.3);
glutSolidCube(3);
glPopMatrix();

pygame.display.flip()

def idle():
    global r, g, a, b
    if r == 1.000:
        r = 0.498
        g = 1.000
    else:
        r = 1.000
        g = 0.000
    if b == 0:
        a = 0.1
        b = 1
    else:
        a = 0
        b = 0
    pygame.time.wait(100)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)

    resize(*display)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        display()
        idle()

if __name__ == '__main__':
    main()
