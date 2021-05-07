import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bulllet import Bullet
from alien import Alien
from game_stat import Game_state
from button import Button


class Alien_invasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.width, self.settings.height))
        pygame.display.set_caption('Alien Invasion')
        self.stat = Game_state(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()
            if self.stat.game_active:
                self.bullets.update()
                for bullet in self.bullets.copy():
                    if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)
                collisions = pygame.sprite.groupcollide(
                    self.bullets, self.aliens, True, True)
                if not self.aliens:
                    self.bullets.empty()
                    self._create_fleet()
                self._update_alien()
                self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.play_button.draw_button()
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bulllet()
        self.aliens.draw(self.screen)
        self.ship.update()
        pygame.display.flip()

    def _ship_hit(self):
        if self.stat.ships_left > 0:
            self.stat.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(1.0)
        else:
            self.stat.game_active = False

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.height - (3 * alien_height) -
                             ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create the first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_Allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_alien(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_dir *= -1

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()