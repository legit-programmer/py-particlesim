import pygame
import sys
from particle import *
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Starter Template")

# Clock for controlling the frame rate
clock = pygame.time.Clock()


particles = []
# init particles
def generateParticles(count:int):
    for i in range(count):
        particles.append(Particle(random.randrange(0, WIDTH, 5), random.randrange(0, HEIGHT, 5), random.randrange(10, 50), 50, 1, 1, (random.randrange(0, 255, 10), random.randrange(0, 255, 10), random.randrange(0, 255, 10))))

# x, y, r, m, xvel, yvel


generateParticles(1000)
# Game loop
running = True
while running:

    # Event handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Clear the screen
    win.fill(BLACK)

    # Draw your game elements here

    for particle in particles:
        particle.draw(win)
        particle.applyMotion()
        particle.checkCollision(win, particles)
        # particle.applyForce(particles)
    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame and the program
pygame.quit()
sys.exit()
