import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from score import Score
from button import Button
from alien import Alien
from ship import Ship
import game_functions as gf


def run_game():
    # Initialise the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make play button
    play_button = Button(ai_settings, screen, "Play")

    # Make ship, make a group of bullets, make fleet of aliens
    # Group() imported from pygame.sprite
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Make a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Creates instance to store game stats
    stats = GameStats(ai_settings)
    score_board = Score(ai_settings, screen, stats)

    # Main run loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, score_board, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, score_board, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, score_board, ship, aliens, bullets, play_button)


run_game()
