import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets):
    """Responds to user inputs"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, score_board, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
          check_keyup_events(event, ship)

def start_game(ai_settings, screen, stats, score_board, ship, aliens, bullets):
    if not stats.game_active:
        # Reset the game settings
        ai_settings.dynamic_settings()
        # Hide mouser cursor
        pygame.mouse.set_visible(False)
        # Reset game statistics
        stats.reset_stats()
        stats.game_active = True

        # Reset Scoreboard
        score_board.prep_score()
        score_board.prep_high_score() # TODO make changes to save high scores
        score_board.prep_level()
        score_board.prep_ships()

        # Empty Groups
        aliens.empty()
        bullets.empty()

        # Create a new fleet of aliens and center ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_play_button(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when play is clicked"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(ai_settings, screen, stats, score_board, ship, aliens, bullets)


def check_keydown_events(event, ai_settings, screen, stats, score_board, ship, aliens, bullets):
    """Responds to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, score_board, ship, aliens, bullets)

    # Vertical Movement Code
    # elif event.key == pygame.K_UP:
    #     ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_down = True

def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire new bullet if limit hasn't been reached"""
    # Create a new bullet & add it to the bullet group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

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


def update_screen(ai_settings, screen, stats, score_board,  ship, aliens, bullets, play_button):
    """Update images on the screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship & aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Display scoreboard information
    score_board.display_score()

    # Draw play button if game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, score_board, ship, aliens, bullets):
    """Updates bullet position and removes old bullets"""
    # Update bullet positons
    bullets.update()
    # Remove bullets after they pass out of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Print statement used for verifying bullet removal
    # print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, stats, score_board, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, score_board, ship, aliens, bullets):
    """Respond to collisions"""
    # Check for bullets that have hit aliens
    # Remove bullets and aliens if hit
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_hit_points * len(aliens)
            score_board.prep_score()
        check_high_scores(stats, score_board)

    # Destroy remaining bullets, build new fleet, increase speed
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        # Increase game level
        stats.level += 1
        score_board.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def ship_hit(ai_settings, stats, score_board, screen, ship, aliens, bullets):
    """Responds to ship being hit by aliens"""
    if stats.ships_lives > 0:
        # remove 1 life from ship_lives
        stats.ships_lives -= 1

        # Update ship lives
        score_board.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Creates a new fleet and re-centers the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Brief pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, score_board, screen, ship, aliens, bullets):
    """Check if aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        # Treats alien reaching bottom as if ship was hit
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, score_board, screen, ship, aliens, bullets)

def check_high_scores(stats, score_board):
    """Check for existing highscores"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()


def update_aliens(ai_settings, stats, score_board, screen, ship, aliens, bullets):
    """Check if fleet at an edge; update positions of aliens within fleet """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for collisions between ship and aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, score_board, screen, ship, aliens, bullets)
        # Used for debugging
        #print("Ship Has Been Hit!!!")

    # Check if any aliens made it to the bottom!
    check_aliens_bottom(ai_settings, stats, screen, score_board, ship, aliens, bullets)

def get_number_of_aliens_x(ai_settings, alien_width):
    """Work out number of aliens per row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_of_aliens_x = int(available_space_x / (2 * alien_width))
    return number_of_aliens_x

def get_number_of_rows(ai_settings, ship_height, alien_height):
    """Determine number of rows that will fit on screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_of_rows = int(available_space_y / (2 * alien_height))
    return number_of_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Create an alien in row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship,  aliens):
    """Create fleet of aliens"""
    # Creates alien and finds number of aliens in row
    # Spacing between aliens = 1 alien width
    alien = Alien(ai_settings, screen)
    number_of_aliens_x = get_number_of_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_of_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Change direction & drop if fleet hits edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(ai_settings, aliens)
            break

def change_fleet_directions(ai_settings, aliens):
    """Change direction & drop fleet"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


