#Imports
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)
        self.rotation = 0
    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), SHOT_RADIUS, 2)
        #circle(surface, color, center, radius) -> Rect

    def update(self, dt):
        self.position += (self.velocity * dt)