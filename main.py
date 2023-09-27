import pygame
import sys
from particle import *
import random
import itertools
import math

pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Starter Template")


clock = pygame.time.Clock()


blue_particles = []
red_particles = []
yellow_particles = []


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
                    i.x = WIDTH - 10
                    ux = -(ux)
                if i.y >= HEIGHT:
                    i.y = HEIGHT - 10
                    ux = -(ux)
                if i.y <= 0:
                    i.y = 0 + 10
                    ux = -(ux)
                if i.x <= 0:
                    i.x = 0 + 10
                    ux = -(ux)
                i.x += ux * force
                i.y += uy * force


def applyAllRules():  # apply all rules for particles here
    applyRule(blue_particles, red_particles, 1)
    applyRule(red_particles, blue_particles, -5)
    applyRule(red_particles, red_particles, 10)
    applyRule(blue_particles, blue_particles, -1)
    applyRule(blue_particles, yellow_particles, 5)
    applyRule(red_particles, yellow_particles, -3)
    applyRule(yellow_particles, red_particles, 2)


generateParticles(20, 100, 45)  # generate particles here


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill(BLACK)

    for particle in itertools.chain(blue_particles, red_particles, yellow_particles):
        particle.draw(win)

    applyAllRules()

    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()
sys.exit()
