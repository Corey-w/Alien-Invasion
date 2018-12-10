
class GameStats():
    """Tracks the games stats"""

    def __init__(self, ai_settings):
        """Initialise stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initialise stats that change during gameplay"""
        self.ships_lives = self.ai_settings.ship_lives
        self.score = 0
