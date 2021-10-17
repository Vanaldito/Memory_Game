import sys
import random

import pygame
from pygame.locals import *

from settings import Settings
from coins import Coin

class Game:
    """ A class to manage the game """

    def __init__(self):
        """ Create a new game """
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()
        self.coins = pygame.sprite.Group()

    def run(self):
        """ Init the game loop """
        print(self._create_board())
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """ Check game events """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def _update_screen(self):
        """ Update the screen """
        self.screen.fill((255,255,255))
        self.coins.draw()
        pygame.display.update()

        self.clock.tick(self.settings.FPS)

    def _create_board(self):
        """ Create a initial board """
        carts = 2 * ["apple", "duck", "bone", "muffin", "pear", "star", "crab", "trumpet"]
        random.shuffle(carts)
        for cart in carts:
            self.coins.add(Coin(self, cart))

if __name__=="__main__":
    ai_game = Game()
    ai_game.run()
