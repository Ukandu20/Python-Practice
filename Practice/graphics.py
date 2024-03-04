import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cubic B-Spline")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# B-spline calculation
def cubic_bspline(control_points, t):
    if len(control_points) == 1:
        return control_points[0]
    else:
        new_points = []
        for i in range(len(control_points) - 1):
            x = (1 - t) * control_points[i][0] + t * control_points[i + 1][0]
            y = (1 - t) * control_points[i][1] + t * control_points[i + 1][1]
            new_points.append((x, y))
        return cubic_bspline(new_points, t)

# Draw curve
def draw_curve(control_points):
    for t in np.linspace(0, 1, num=100):
        point = cubic_bspline(control_points, t)
        pygame.draw.circle(screen, RED, (int(point[0]), int(point[1])), 1)

# Main loop
def main():
    control_points = []
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left-click detected
                    control_points.append(event.pos)
                    pygame.draw.circle(screen, BLUE, event.pos, 3)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:  # 'c' key pressed
                    control_points.clear()

        # Redraw control points
        for point in control_points:
            pygame.draw.circle(screen, BLUE, point, 3)

        # Draw the curve if there are enough control points
        if len(control_points) >= 4:
            draw_curve(control_points)

        pygame.display.flip()
        pygame.time.delay(10)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
