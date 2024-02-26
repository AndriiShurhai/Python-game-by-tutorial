from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, position, display, groups):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill('gray')
        self.rect = self.image.get_frect(topleft=position)
        self.old_rect = self.rect.copy()