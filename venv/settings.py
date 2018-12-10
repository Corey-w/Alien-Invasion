
class Settings():
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """ Initilise the games settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 100, 100)

        # Ship settings
        self.ship_lives = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # Game level settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.dynamic_settings()

    def dynamic_settings(self):
        """Dynamically changing settings"""
        # Ship settings
        self.ship_speed_factor = 1.5
        # Bullet Settings
        self.bullet_speed_factor = 3
        # Alien settings
        self.alien_speed_factor = 1
        # Fleet_direction 1 = right; -1 = left
        self.fleet_direction = 1
        # Scoring
        self.alien_hit_points = 50

    def increase_speed(self):
        """Increase game speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # Increase score values with each level
        self.alien_hit_points = int(self.alien_hit_points * self.score_scale)

        # Used for debugging score
        print(self.alien_hit_points)
