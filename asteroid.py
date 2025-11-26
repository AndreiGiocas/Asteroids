from circleshape import CircleShape
from constants import  *
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position = self.position + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_dir = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(new_dir)
        new_vector2 = self.velocity.rotate(-new_dir)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid.containers = self.containers
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector1 * 1.2
        asteroid2.velocity = new_vector2 * 1.2