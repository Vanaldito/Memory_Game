class Settings:
    """ A class to manage the settings game """

    def __init__(self):
        """ Init the settings """
        # Screen settings
        self.screen_width = 600
        self.screen_height = 600

        self.FPS = 60
        # Coins Settings
        self.coin_len = self.screen_height // 9
