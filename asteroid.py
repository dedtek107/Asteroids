import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    random_angle = random.uniform(20, 50)

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
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill() # Asteroid is too small to split
        else: #self.radius > ASTEROID_MIN_RADIUS:
            # Create two smaller asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            # Set their velocities to be perpendicular to the original asteroid's velocity
            asteroid1.velocity = self.velocity.rotate(self.random_angle) * 1.2
            asteroid2.velocity = self.velocity.rotate(-self.random_angle) * 1.2

            self.kill()