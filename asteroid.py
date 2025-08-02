import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Asteroids do not move or rotate in this simple implementation
        self.position += self.velocity * dt

    def rotate(self, dt):
        self.rotation += dt * ASTEROID_ROTATION_SPEED