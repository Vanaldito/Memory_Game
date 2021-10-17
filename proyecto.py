import sys
import time
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
        self.complete = pygame.sprite.Group() # For the sprites completes
        self.coins_v = 0
        self.errors = 0
        self.pairs = 0

    def run(self):
        """ Init the game loop """
        self._create_board()
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """ Check game events """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                self._check_mouse_button()

    def _check_mouse_button(self):
        """ Respond to mouse events """
        event_pos = pygame.mouse.get_pos()
        for sprite in self.coins.copy():
            if sprite.rect.collidepoint(event_pos):
                if self.coins_v == 0:
                    sprite.flip()
                    self.v = sprite # Store the sprite in self.v
                    self.coins_v += 1
                else:
                    self._check_two_coins(sprite)

    def _check_two_coins(self, sprite):
        """ Check if the two coins are equal """
        if self.v != sprite:
            sprite.flip()
            self._update_screen()
            time.sleep(0.5)
            if self.v.name == sprite.name:
                self.coins_v = 0
                # Change the group
                self.coins.remove(sprite)
                self.coins.remove(self.v)
                self.complete.add(sprite)
                self.complete.add(self.v)
                if len(self.complete) == 16:
                    print("Ganaste")
                    pygame.quit()
                    sys.exit()
            else:
                self.v.flip()
                sprite.flip()
                self.errors += 1
                self.coins_v = 0

    def _update_screen(self):
        """ Update the screen """
        self.screen.fill((255,255,255))

        self.coins.draw(self.screen)
        self.complete.draw(self.screen)

        pygame.display.update()

        self.clock.tick(self.settings.FPS)

    def _create_board(self):
        """ Create a initial board """
        carts = 2 * ["apple", "duck", "bone", "muffin", "pear", "star", "crab", "trumpet"]
        random.shuffle(carts)
        for index in range(len(carts)):
            self.coins.add(Coin(self, carts[index], index%4, index//4))

if __name__=="__main__":
    ai_game = Game()
    ai_game.run()
