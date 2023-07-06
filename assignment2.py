import sys
import math
import pygame
from pygame.locals import QUIT, DOUBLEBUF, OPENGL, MOUSEBUTTONDOWN
from OpenGL.GL import glBegin, glEnd, glVertex2f, glColor3f, glClearColor, glClear, GL_COLOR_BUFFER_BIT, GL_QUADS
from OpenGL.GLU import gluOrtho2D

# Define the viewport dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# Define the coordinates and dimensions of the boxes and the gap between them
BOX1_X = 50.0
BOX1_Y = 50.0
BOX1_WIDTH = 200.0
BOX1_HEIGHT = 200.0
BOX2_X = BOX1_X + BOX1_WIDTH + 50.0
BOX2_Y = BOX1_Y
BOX2_WIDTH = BOX1_WIDTH
BOX2_HEIGHT = BOX1_HEIGHT
GAP_WIDTH = 50.0
GAP_HEIGHT = 50.0
GREEN_BOX_X = BOX2_X
GREEN_BOX_Y = BOX2_Y + BOX2_HEIGHT + GAP_HEIGHT
GREEN_BOX_SIZE = 10.0

# Define the prey and predator properties
PREY_SPEED = 5.0
PREDATOR_SPEED = 2 * PREY_SPEED
PREY_SIZE = 20.0
PREDATOR_SIZE = 30.0

# Define the initial positions of the prey and predator by mouse click
preyX = GREEN_BOX_X + GREEN_BOX_SIZE / 2.0
preyY = GREEN_BOX_Y + GREEN_BOX_SIZE / 2.0
predatorX = -1.0
predatorY = -1.0

# Define the size of the predator and whether it is moving
predatorSize = PREDATOR_SIZE
predatorMoving = False

# Define the escape position
ESCAPE_X = BOX1_X + BOX1_WIDTH
ESCAPE_Y = BOX1_Y + BOX1_HEIGHT / 2.0

# Draw a rectangle with the specified dimensions and color
def drawRectangle(x, y, width, height, r, g, b):
    glBegin(GL_QUADS)
    glColor3f(r, g, b)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

# Draw the pathway with the boxes and the green box
def drawPathway():
    drawRectangle(BOX1_X, BOX1_Y, BOX1_WIDTH, BOX1_HEIGHT, 2.0, 1.0, 1.0)
    drawRectangle(BOX2_X, BOX2_Y, BOX2_WIDTH, BOX2_HEIGHT, 1.0, 1.0, 1.0)
    drawRectangle(GREEN_BOX_X, GREEN_BOX_Y, GREEN_BOX_SIZE, GREEN_BOX_SIZE, 0.0, 1.0, 0.0)

# Draw the prey
def drawPrey(x, y, size):
    drawRectangle(x - size / 2, y - size / 2, size, size, 0.0, 1.0, 0.0)

# Draw the predator
def drawPredator(x, y, size):
    drawRectangle(x - size / 2, y - size / 2, size, size, 1.0, 0.0, 0.0)

# Update the prey position based on its movement direction and speed
def updatePreyPosition(x, y, direction, speed):
    x += math.cos(direction) * speed
    y += math.sin(direction) * speed
    return x, y

#Check if the predator has caught the prey
def checkPredatorCaught():
    global predatorMoving, predatorSize
distance = math.sqrt((preyX - predatorX) ** 2 + (preyY - predatorY) ** 2)
if distance < (predatorSize / 2.0):
    predatorMoving = False
predatorSize = PREDATOR_SIZE



# Main loop
def main():
    global preyX, preyY, predatorMoving
    pygame.init()
    display = (WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Prey movement direction (in radians)
prey_direction = 0.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            # Update the prey's position based on the mouse click
            if not predatorMoving:
                if pygame.mouse.get_pressed()[0]:
                    preyX, preyY = pygame.mouse.get_pos()
                    predatorMoving = True
                elif pygame.mouse.get_pressed()[2]:  # 2 for right click
                    predatorX, predatorY = pygame.mouse.get_pos()

    # Update the prey's position
    if predatorMoving:
        preyX, preyY = updatePreyPosition(preyX, preyY, prey_direction, PREY_SPEED)

    glClear(GL_COLOR_BUFFER_BIT)
    drawPathway()
    drawPrey(preyX, preyY, PREY_SIZE)

    # Update the predator's position
    if predatorMoving:
        direction = math.atan2(preyY - predatorY, preyX - predatorX)
        predatorX, predatorY = updatePreyPosition(predatorX, predatorY, direction, PREDATOR_SPEED)
        if checkPredatorCaught():
            drawPrey(preyX, preyY, PREY_SIZE)  # redraw prey on top of predator
            predatorX, predatorY = -1.0, -1.0  # reset predator position

    # Draw the predator
    if predatorX != -1.0 and predatorY != -1.0:
        drawPredator(predatorX, predatorY, predatorSize)
        predatorSize += 1  # increase predator size over time

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
sys.exit()
