# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

#holds the game constants
from constants import *

#player class
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot



def main():
    pygame.init()
    # game clock for fps
    game_clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #class variable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # inits screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #declares player
    player_spaceship = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    #declares field
    asteroid_field = AsteroidField()

    #infite while loop to create the board and player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        updatable.update(dt) 
        
        for asteroid in asteroids:
            if asteroid.collision(player_spaceship):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        
        screen.fill("black")        
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()