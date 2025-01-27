import pygame.font
from pygame.sprite import Group
from ship import Ship

class Score():
    """Reports scoring stats"""
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings
        self.text_color = (50, 50, 50)
        self.font = pygame.font.SysFont(None, 48)

        # Prep initial score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Display score as rendered image"""
        rounded_score = round(self.stats.score)
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Score placement (Top Right)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Render the high score as an image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center High Score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Render level as an image"""
        level = int(self.stats.level)
        level_str = "Lvl: {:,}".format(level)
        self.level_image = self.font.render(str(level_str), True, self.text_color, self.ai_settings.bg_color)

        # Position level
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Shows number of ships left in game"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_lives):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def display_score(self):
            """Draw score on screen"""
            self.screen.blit(self.score_image, self.score_rect)
            self.screen.blit(self.high_score_image, self.high_score_rect)
            self.screen.blit(self.level_image, self.level_rect)
            # Draw Ship Lives
            self.ships.draw(self.screen)

