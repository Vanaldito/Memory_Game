import sys

import pygame
from pygame.locals import *

from settings import Settings

class Game:
    """ A class to manage the game """

    def __init__(self):
        """ Create a new game """
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()

    def run(self):
        """ Init the game loop """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill((255,255,255))
            pygame.display.update()

            self.clock.tick(self.settings.FPS)


if __name__=="__main__":
    ai_game = Game()
    ai_game.run()