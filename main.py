import pygame

from queen_of_hearts.config.screen import Screen

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(Screen.SIZE_HD)
        self._config_window()
        self.running = True

    def run(self):
        while self.running:
            self._handle_events()

        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _config_window(self):
        pygame.display.set_caption("Titulindo")


if __name__ == "__main__":
    game = Game()
    game.run()
