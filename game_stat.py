class Game_state:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.game_active = True
        self.restart_stat()
    
    def restart_stat(self):
        self.ships_left = self.settings.ship_limit