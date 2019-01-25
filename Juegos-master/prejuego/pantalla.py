import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, imagen)
        self.image = pygame.image.load(imagen)
        self.x = 0
        self.y = 0
        self.ancho = 10
        self.alto = 10
        

class Pantalla:
    def __init__(self, canvas):
        self.sprites = {}
        self._canvas = canvas

    def agregar_sprite(self, id, sprite):
        self.sprites[id] = sprite
        
    def handle_events(self):
        pass
    def update(self):
        pass

    def render(self):
        self._canvas.fill([0,0,0])
        for sprite in self.sprites:
            self._canvas.blit(sprite.image.get_rect(), Rect(sprite.x, sprite.y, sprite.ancho, sprite.alto))
        pygame.display.flip()
    
class EjemploPantalla(Pantalla):
    def __init__(self, canvas):
        Pantalla.__init__(self, canvas)
        p1 = Pelota()
        p1.agregar_sprite(p1)

    def handle_events(self):
        pass
    def update(self):
        self.sprites[0].x = 400