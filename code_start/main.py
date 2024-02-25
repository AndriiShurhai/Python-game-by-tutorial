#importing required data
from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join

# creating an instance to run a game
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))   # setting a display
        pygame.display.set_caption("Pirate game")  # setting a caption
        self.clock = pygame.time.Clock()

        self.pytmx_maps = {0: load_pygame(join('..', 'data', 'levels', 'omni.tmx'))}  # loading a map from .tmx file

        self.current_stage = Level(self.pytmx_maps[0])  # creating an instance of Level class

    def run(self):  # running and updating our screen untill user exits
        while True:
            delta_time = self.clock.tick(120) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(delta_time)
            pygame.display.update()  # updating a display each frame

if __name__ == "__main__":
    game = Game()
    game.run()