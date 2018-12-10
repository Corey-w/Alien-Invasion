import sys
import pygame
from bullet import Bullet
def check_events(ai_settings, screen, ship, bullets):
    """Responds to user inputs"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
          check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet & add it to the bullet group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

    # Vertical Movement Code
    # elif event.key == pygame.K_UP:
    #     ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_down = True

def check_keyup_events(event, ship):
    """Responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    # Vertical Movement Code
    # elif event.key == pygame.K_UP:
    #     ship.moving_up = False
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_down = False


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship & aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
