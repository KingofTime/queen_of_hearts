import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP


class Player(pygame.sprite.Sprite):
    def __init__(self, position: list[int]):
        super(Player, self).__init__()
        self.surface = pygame.Surface((75, 25))
        self.surface.fill((0, 0, 0))
        self.rect = self.surface.get_rect(center=position)

        self.attributes = {"speed": 5}

    def update(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)

    def check_border_player_area(self, player_area: tuple[int]):
        if self.rect.left < 0:
            self.rect.right = player_area[0]
        if self.rect.right > player_area[0]:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > player_area[1]:
            self.rect.bottom = player_area[1]

    def handle_event(self, pressed_keys: dict):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, self.attributes["speed"] * -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.attributes["speed"])
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(self.attributes["speed"] * -1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.attributes["speed"], 0)
