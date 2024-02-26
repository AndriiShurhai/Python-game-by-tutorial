from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('red')

        # rects
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        # movement
        self.direction = vector()
        self.speed = 200
        self.gravity = 400

        # collisions
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        if keys[pygame.K_RIGHT]:
            input_vector.x += 1

        if keys[pygame.K_LEFT]:
            input_vector.x -= 1

        self.direction.x = input_vector.normalize().x if input_vector else 0 # to have same movement pixels despite on vector

    def move(self, delta_time):
        # horizontal
        self.rect.x += self.direction.x * self.speed * delta_time
        self.collisions('horizontal')

        # vertical
        self.direction.y += self.gravity / 2 * delta_time # because it's framerate independed we need to increase direction two times before and after the movement
        self.rect.y += self.direction.y * delta_time
        self.direction.y += self.gravity / 2 * delta_time # because it's framerate independed we need to increase direction two times before and after the movement
        self.collisions('vertical')

    def collisions(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    # left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:  # check if collision was from the left side
                        self.rect.left = sprite.rect.right

                    # right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:  # check if collision was from the right side
                        self.rect.right = sprite.rect.left

                elif axis == 'vertical':
                    # bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top

                    # top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom

    def update(self, delta_time):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(delta_time)