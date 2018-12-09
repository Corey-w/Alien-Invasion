import pygame

class Ship():
    def __init__(self, screen):
        """Initiliase the ship and set its starting position"""
        self.screen = screen

        # Load the ship elements
        self.image = pygame.image.load('images/nightraiderfixed.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        """Draw ship in its current location"""
        self.screen.blit(self.image, self.rect)
