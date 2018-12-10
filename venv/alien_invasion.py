import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from alien import Alien
from ship import Ship
import game_functions as gf

def run_game():
    # Initialise the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make ship, make a group of bullets, make fleet of aliens
    # Group() imported from pygame.sprite
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Make a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Set background color
    bg_color = (230, 230, 230)

    # Main run loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
