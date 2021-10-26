import pygame

class Button():
    """ A class to create a play button """

    def __init__(self, ai_game):
        """ Create a new play button """
        self.screen = ai_game.screen

        self.font = pygame.font.SysFont(None, 48)
        self.text = "Play"

        self.text_str = self.font.render(self.text, True, (0,0,0), (0,255,0))
        self.rect = self.text_str.get_rect()

        # Rect configs
        self.rect.center = self.screen.get_rect().center

    def update(self):
        """ Draw the text on the screen """
        self.screen.blit(self.text_str, self.rect)
