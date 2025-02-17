import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kaleidoscope Simulation")

# Colors
BLACK = (0, 0, 0)

# Number of symmetrical sections
SECTIONS = 8  # Must be even for proper symmetry
ANGLE = 360 / SECTIONS

# Function to draw a shape and its mirrored versions
def draw_kaleidoscope_pattern(x, y, color, size):
    for i in range(SECTIONS):
        angle = math.radians(ANGLE * i)
        new_x = WIDTH // 2 + (x - WIDTH // 2) * math.cos(angle) - (y - HEIGHT // 2) * math.sin(angle)
        new_y = HEIGHT // 2 + (x - WIDTH // 2) * math.sin(angle) + (y - HEIGHT // 2) * math.cos(angle)
        pygame.draw.circle(screen, color, (int(new_x), int(new_y)), size)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill(BLACK)

    # Randomize pattern properties
    for _ in range(10):  # Number of shapes per frame
        x = random.randint(WIDTH // 4, 3 * WIDTH // 4)
        y = random.randint(HEIGHT // 4, 3 * HEIGHT // 4)
        color = [random.randint(50, 255) for _ in range(3)]
        size = random.randint(2, 6)
        draw_kaleidoscope_pattern(x, y, color, size)

    # Update display
    pygame.display.flip()
    clock.tick(30)  # FPS

pygame.quit()
