import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien Class - single alien"""

    def __init__(self, ai_settings, screen):
        """Initialise alien and set starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set rect attribute
        self.image = pygame.image.load("images/alien_image.jpg")
        self.rect = self.image.get_rect()

        # start each alien at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at current position"""
        self.screen.blit(self.image, self.rect)

