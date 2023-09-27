import pygame
import sys
from particle import *
import random
import itertools
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 1280
HEIGHT = 720
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Starter Template")

# Clock for controlling the frame rate
clock = pygame.time.Clock()


blue_particles = []
red_particles = []
yellow_particles = []
# init particles


def generateParticles(bcount, rcount, ycount):
    for i in range(bcount):
        blue_particles.append(Particle(random.randrange(
            WIDTH), random.randrange(HEIGHT), 2, 1, 1, BLUE))

    for i in range(rcount):
        red_particles.append(Particle(random.randrange(
            WIDTH), random.randrange(HEIGHT), 2, 1, 1, RED))

    for i in range(ycount):
        yellow_particles.append(Particle(random.randrange(
            WIDTH), random.randrange(HEIGHT), 2, 1, 1, GREEN))
# x, y, r, m, xvel, yvel


def applyRule(particle1: list, particle2: list, strength: int):
    for i in particle1:
        for j in particle2:
            distance = math.sqrt((j.x-i.x)**2 + (j.y-i.y)**2)
            if distance < 250:
                force = strength
                ux = random.choice([1, -1])
                uy = random.choice([1, -1])
                try:
                    ux = (j.x-i.x) / distance
                    uy = (j.y-i.y) / distance
                except ZeroDivisionError:
                    pass
                print(ux, uy)
                if i.x >= WIDTH:
                    i.x = WIDTH - 5
                    ux = -(ux)
                if i.y >= HEIGHT:
                    i.y = HEIGHT - 5
                    ux = -(ux)
                if i.y <= 0:
                    i.y = 0 + 5
                    ux = -(ux)
                if i.x <= 0:
                    i.x = 0 + 5
                    ux = -(ux)
                i.x += ux * force
                i.y += uy * force
    # print(force)



generateParticles(13, 12, 45)
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

    for particle in itertools.chain(blue_particles, red_particles, yellow_particles):
        particle.draw(win)
    applyRule(blue_particles, red_particles, 1)
    applyRule(red_particles, blue_particles, -5)
    applyRule(red_particles, red_particles, 10)
    applyRule(blue_particles, blue_particles, -1)
    applyRule(blue_particles, yellow_particles, 5)
    applyRule(red_particles, yellow_particles, -3)
    applyRule(yellow_particles, red_particles, 2)

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame and the program
pygame.quit()
sys.exit()
