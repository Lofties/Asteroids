#Imports
import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

#Asteroid class

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
        #circle(surface, color, center, radius) -> Rect

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:            
            return
        
        random_angle = random.uniform(20, 50)

        new_asteroid_vector1 = self.velocity.rotate(random_angle)
        new_asteroid_vector2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_asteroid_vector1 * 1.2
        
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_asteroid_vector2 * 1.2
