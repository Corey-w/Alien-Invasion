import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initiliase the ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship elements
        self.image = pygame.image.load('images/nightraiderfixed.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value fro the ships center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        # Vertical Movement Code
        # self.moving_down = False
        # self.moving_up = False

    def update(self):
        """Update the ships position based on the movement flag"""
        # Update the ships center not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Vertical Movement Code
        # if self.moving_up:
        #     self.rect.centery -= self.ai_settings.ship_speed_factor
        # if self.moving_down:
        #     self.rect.centery += self.ai_settings.ship_speed_factor

        # Update rect from self.center
        self.rect.centerx = self.center


    def blitme(self):
        """Draw ship in its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centers the ship"""
        self.center = self.screen_rect.centerx
