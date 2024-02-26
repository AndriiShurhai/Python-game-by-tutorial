# import required data
from settings import *
from sprites import Sprite
from player import Player

class Level():
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()  # getting a display so our Level will be also drown

        # groups of sprites
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        self.setup(tmx_map)

    def setup(self, tmx_map):
        for x, y, surface in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surface, (self.all_sprites, self.collision_sprites))  # sprite will be on two sprites groups

        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)  # player will have an access to collision sprites but not actualyy in this group itself

    def world_shift(self):
        pass

    def run(self, delta_time):
        self.display_surface.fill("black")
        self.all_sprites.update(delta_time)
        self.all_sprites.draw(self.display_surface)