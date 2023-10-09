import pygame
import sys
from particle import *
import random
import itertools
import math
from gui import *

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

    max_len = max([len(red_particles), len(
        blue_particles), len(yellow_particles)])
    print(max_len)
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
        fx = 0
        fy = 0
        for j in particle2:
            distance = math.sqrt((j.x-i.x)**2 + (j.y-i.y)**2)
            dx = i.x - j.x
            dy = i.y - j.y

            if distance > 0 and distance < 80:
                force = 1/distance * strength
                
                fx += dx * force
                fy += dy * force
        i.x_vel = (i.x_vel+fx)*0.5
        i.y_vel = (i.y_vel+fy)*0.5
        i.x += i.x_vel
        i.y += i.y_vel
        if i.x <= 0 or i.x >= WIDTH:
            i.x_vel *= -1
        if i.y <= 0 or i.y >= HEIGHT:
            i.y_vel *= -1


def applyAllRules():  # apply all rules for particles here
    applyRule(blue_particles, red_particles, 1)
    applyRule(red_particles, blue_particles, -1)
    # applyRule(red_particles, red_particles, -5)
    applyRule(blue_particles, blue_particles, -2)
    applyRule(blue_particles, yellow_particles, 3)
    applyRule(blue_particles, red_particles, 5)
    applyRule(red_particles, blue_particles, 2)
    applyRule(red_particles, red_particles, -2)

    applyRule(red_particles, yellow_particles, -0.15)

    applyRule(yellow_particles, yellow_particles, -1)
    # applyRule(red_particles, red_particles, -0.01)



generateParticles(200, 200, 100)  # particles count: BLUE RED YELLOW


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill(BLACK)

    for particle in itertools.chain(blue_particles, red_particles, yellow_particles):
        particle.draw(win)

    applyAllRules()
    Slider(win, 'Helo', 50, 50, 50)

    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()
sys.exit()
