import sys
import time
import random

import pygame
from pygame.locals import *

from settings import Settings
from coins import Coin
from button import Button

class Game:
    """ A class to manage the game """

    def __init__(self):
        """ Create a new game """
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Memory Game")

        self.clock = pygame.time.Clock()
        self.coins = pygame.sprite.Group()
        self.complete = pygame.sprite.Group() # For the sprites completes
        self.button = Button(self)
        self.coins_v = 0
        self.errors = 0
        self.pairs = 0
        self.game_active = False

    def run(self):
        """ Init the game loop """
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

        if (not self.game_active and 
                self.button.rect.collidepoint(event_pos)):
            return self._play_mouse_button()

        for sprite in self.coins.copy():
            if not sprite.rect.collidepoint(event_pos):
                continue

            if self.coins_v == 1:
                self._check_two_coins(sprite)
                continue

            sprite.flip()
            self.v = sprite # Store the sprite in self.v
            self.coins_v += 1

    def _check_two_coins(self, sprite):
        """ Check if the two coins are equal """
        if self.v == sprite:
            return None

        sprite.flip()
        self._update_screen()
        time.sleep(0.5)

        if self.v.name != sprite.name:
            self.v.flip()
            sprite.flip()
            self.errors += 1
            self.coins_v = 0
            return None;

        self.coins_v = 0
        # Change the group
        self.coins.remove(sprite)
        self.coins.remove(self.v)
        self.complete.add(sprite)
        self.complete.add(self.v)

        if len(self.complete) == 16:
            self.game_active = False

    def _update_screen(self):
        """ Update the screen """
        self.screen.fill((255,255,255))

        self.coins.draw(self.screen)
        self.complete.draw(self.screen)

        if not self.game_active:
            self.button.update()

        pygame.display.update()

        self.clock.tick(self.settings.FPS)

    def _create_board(self):
        """ Create a initial board """
        carts = 2 * ["apple", "duck", "bone", "muffin", "pear", "star", "crab", "trumpet"]
        random.shuffle(carts)
        for index in range(len(carts)):
            self.coins.add(Coin(self, carts[index], index%4, index//4))

    def _play_mouse_button(self):
        """ Respond when press mouse button """
        self.complete.empty()
        self._create_board()
        self.game_active = True

if __name__=="__main__":
    ai_game = Game()
    ai_game.run()
