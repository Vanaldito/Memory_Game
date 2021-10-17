import pygame

from pygame.sprite import Sprite

class Coin(Sprite):
    """ A class to manage coins  """

    def __init__(self, ai_game, image):
        """ Create a new coin """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image_front = pygame.transform.scale(pygame.image.load(f"{image}"), (300,300))
        self.image_back = pygame.transform.scale(pygame.image.load("Assets/Back.png"))

        self.image = self.image_back

    def flip(self):
        """ Flip the coin """
        if self.image == self.image_back:
            self.image = self.image_front
        else:
            self.image = self.image_back
