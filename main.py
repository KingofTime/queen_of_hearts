import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from queen_of_hearts.characters.Player import Player
from queen_of_hearts.config.screen import Screen

pygame.init()


class Game:
    def __init__(self):
        self.screen_size: list = Screen.SIZE_HD
        self.screen = pygame.display.set_mode(self.screen_size)
        self.player = Player(
            [self.screen_size[0] / 2, self.screen_size[1] / 2]
        )
        self.running = True

        self._config_window()
        self._update_screen()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self._handle_event(event)

            pressed_keys = pygame.key.get_pressed()
            self.player.handle_event(pressed_keys)
            self.player.check_border_player_area(self.screen_size)

            self._update_screen()
            pygame.display.flip()

        pygame.quit()

    def _handle_event(self, event: pygame.event.Event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
        elif event.type == QUIT:
            self.running = False

    def _config_window(self):
        pygame.display.set_caption("Titulindo")

    def _update_screen(self):
        self.screen.fill((255, 255, 255))
        self.player.update(self.screen)


if __name__ == "__main__":
    game = Game()
    game.run()
