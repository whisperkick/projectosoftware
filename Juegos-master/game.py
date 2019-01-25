import pygame
from pantalla import *

class ScreenManager:
    def __init__(self):
        pygame.init()
        canvas = pygame.display.set_mode((800, 600))
        self._pantalla_actual = EjemploPantalla(canvas)
        self.clock = pygame.time.Clock()
        #backdrop = pygame.image.load("Images/fondos/" + img_background + ".png").convert()
        #backdropbox = world.get_rect()

    def run(self):
        while True:
            self._pantalla_actual.handle_events()
            self._pantalla_actual.update()
            self._pantalla_actual.render()
            self.clock.tick(60)

def main():
    manager = ScreenManager()
    manager.run()

if __name__ == "__main__":
    main()