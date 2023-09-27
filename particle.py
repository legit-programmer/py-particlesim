import pygame
import math
import random


class Particle:
    def __init__(self, x, y, r, x_vel, y_vel, color) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color

    def draw(self, win: pygame.Surface):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r)
        
