class Settings:
    def __init__(self):
        #screen setting
        self.width = 1200
        self.height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        #bullet setting
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_Allowed = 5
        #alien setting
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_dir = 1
        #ship settings
        self.ship_limit = 3
