# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

#holds the game constants
from constants import *

#player class
from player import Player





def main():
    pygame.init()
    # game clock for fps
    game_clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #class variable
    Player.containers = (updatable, drawable)

    # inits screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #declares player
    player_spaceship = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    #infite while loop to create the board and player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)    
        screen.fill("black")        
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()