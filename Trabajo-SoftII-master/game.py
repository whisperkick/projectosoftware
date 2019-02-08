import pygame
from pantalla import *

class ScreenManager:
    instancia = None

    @classmethod
    def get_instance(cls): # Metodo de clase
        if cls.instancia == None:
            cls.instancia = ScreenManager()
        return cls.instancia

    def __init__(self):
        pygame.init()
        img_background = "Background"
        #self._pantalla_actual = EjemploPantalla(canvas)
        self.clock = pygame.time.Clock()
        #backdrop = pygame.image.load("images/fondos/" + img_background + ".png").convert()
        #backdropbox = canvas.get_rect()
        self.pantalla = []
        self.indice_actual = -1
        
        

    def cambiar_pantalla(self,nueva_pantalla):
        #condicion de prueba
        self.condicion = 0
        self.aux = True
        self.pantalla.append(nueva_pantalla)
        self.indice_actual = self.indice_actual + 1
        self._pantalla_actual = self.pantalla[self.indice_actual]

    def condicion_pantalla(self):

        #CONDICION DE PRUEBA
        if self.condicion < 100:
            self.aux = True
        else:
            self.aux = False

    def run(self):
        while self.aux == True:
            self._pantalla_actual.handle_events()
            self._pantalla_actual.update()
            self._pantalla_actual.render()
            self.clock.tick(60)
            self.condicion_pantalla()
            self.condicion = self.condicion + 1

def main():

    pantalla1 = Pantalla1()
    pantalla2 = Pantalla2()
    manager = ScreenManager.get_instance()
    manager.cambiar_pantalla(pantalla1)
    manager.run()
    manager.cambiar_pantalla(pantalla2)
    manager.run()
    

if __name__ == "__main__":

    main()