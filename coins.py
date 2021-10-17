import pygame

from pygame.sprite import Sprite

class Coin(Sprite):
    """ A class to manage coins  """

    def __init__(self, ai_game, image, x, y):
        """ Create a new coin """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.name = image

        self.image_front = pygame.transform.scale(pygame.image.load(f"Assets/{image}.jpg"), (self.settings.coin_len, self.settings.coin_len))
        self.image_back = pygame.transform.scale(pygame.image.load("Assets/back.jpg"), (self.settings.coin_len, self.settings.coin_len))

        self.image = self.image_back
        self.rect = self.image.get_rect()
        self.rect.x = (2*x+1)*self.settings.coin_len
        self.rect.y = (2*y+1)*self.settings.coin_len

    def flip(self):
        """ Flip the coin """
        if self.image == self.image_back:
            self.image = self.image_front
        else:
            self.image = self.image_back
