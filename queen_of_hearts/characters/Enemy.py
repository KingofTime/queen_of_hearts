import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position: list[int]) -> None:
        super(Enemy, self).__init__()
        self.surface = pygame.Surface((15,15))
        self.surface.fill((0,0,205))
        self.rect = self.surface.get_rect(center=position)
        
        self.attributes = {"speed": 2}
    
    def update(self):
        self.rect.move_ip(-self.attributes["speed"], 0)
        if self.rect.right < 0:
            self.kill()