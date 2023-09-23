import pygame
import math


class Particle:
    def __init__(self, x, y, r, mass, x_vel, y_vel, color) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.mass = mass
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.force_x = 1
        self.force_y = 1

    def draw(self, win: pygame.Surface):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r)
        # pygame.draw.circle(win, self.color, (250, 25), 25)

    def applyMotion(self):
        # self.x_vel *= self.force_x
        # self.y_vel *= self.force_y
        self.x += self.x_vel 
        self.y += self.y_vel
        

    def checkCollision(self, win: pygame.Surface, particles:list):
        if self.x-self.r <= 0:
            self.x_vel = -(self.x_vel)

        if self.x+self.r >= win.get_width():
            self.x_vel = -(self.x_vel)

        if self.y-self.r <= 0:
            self.y_vel = -(self.y_vel)

        if self.y+self.r >= win.get_height():
            self.y_vel = -(self.y_vel)


        for particle in particles:
            if self!=particle:
                distance = math.sqrt((particle.x-self.x) **
                                    2 + (particle.y-self.y)**2)
                if distance<(particle.r + self.r):
                    particle.x_vel = -(particle.x_vel)
                    self.x_vel = -(self.x_vel)
                    particle.y_vel = -(particle.y_vel)
                    self.y_vel = -(self.y_vel)

    def applyForce(self, particles: list):
        for particle in particles:
            if particle != self:

                distance = math.sqrt((particle.x-self.x) **
                                    2 + (particle.y-self.y)**2)
                force = (self.mass*particle.mass)/distance
                sintheta = distance / (particle.y - self.y)
                # print(sintheta)
                theta_rad = math.asin(0.5)
                print(theta_rad)
                
                self.force_x = math.cos(theta_rad)*force
                print(self)
                self.force_y = math.sin(theta_rad)*force
                
