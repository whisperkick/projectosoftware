import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen)
        self.x = 0
        self.y = 0
        self.ancho = 10
        self.alto = 10
        
class Pantalla:

    def __init__(self):
        self.sprites = {}
        self.canvas = pygame.display.set_mode((800, 600))
        self.eventos =	{
        "Arriba": False,
        "Abajo": False,
        "Derecha": False,
        "Izquierda": False,
        "Salir":False,
        "POSX":0,
        "POSY":0
        }

    def obtener_ultima_pantalla(self):
        pass

    def agregar_sprite(self, nombre, sprite):
        self.sprites[nombre] = sprite
        
    def handle_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.eventos["Salir"]=True
                pygame.quit(); sys.exit()
                print(self.eventos["Salir"])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.eventos["Izquierda"]=True
                    print(self.eventos["Izquierda"])
                if event.key == pygame.K_RIGHT:
                    self.eventos["Derecha"]=True
                    print(self.eventos["Derecha"])
                if event.key == pygame.K_UP:
                    self.eventos["Arriba"]=True
                    print(self.eventos["Arriba"])
                if event.key == pygame.K_DOWN:
                    self.eventos["Abajo"]=True
                    print(self.eventos["Abajo"])
            if event.type == pygame.MOUSEBUTTONUP:
                self.eventos["POSX"]=str(pygame.mouse.get_pos()[0])
                self.eventos["POSY"]=str(pygame.mouse.get_pos()[1])
                print(self.eventos["POSX"])
                print(self.eventos["POSY"])


    def update(self):
        for nombre in self.eventos:
            self.eventos[nombre]=False
            #print(self.eventos[nombre])

    def render(self):
        #print("render")
        #self._canvas.fill([0,0,0])
        for nombre, sprite in self.sprites.items():
            surf = pygame.Surface((sprite.ancho, sprite.alto))
            self.canvas.blit(sprite.image, surf.get_rect(topleft=(sprite.x, sprite.y)))
        pygame.display.flip()
    
class Pantalla1(Pantalla):
    def __init__(self):
        Pantalla.__init__(self)
        #este es el personaje
        p1 = Personaje("images/personajes/hero/hero1.png")
        #este es el fondo
        fondo = Personaje("images/fondos/Background.png")
        self.agregar_sprite("Background",fondo)
        self.agregar_sprite("hero1",p1)
        self.handle_events()
        self.update()

class Pantalla2(Pantalla):
    def __init__(self):
        Pantalla.__init__(self)
        #este es el personaje
        p1 = Personaje("images/personajes/hero/hero1.png")
        #este es el fondo
        fondo = Personaje("images/fondos/cosmos.png")
        self.agregar_sprite("Background",fondo)
        self.agregar_sprite("hero1",p1)
        self.handle_events()
        self.update()





# Para crear una pantalla extra (o la de login) se crea una clase como Ejemplo pantalla y se llama 
# desde game.py en la clase ScreenManager

""" class Login(Pantalla):
    def __init__(self, canvas):
        Pantalla.__init__(self, canvas)
        p1 = Personaje("images/personajes/hero/hero1.png")
        self.agregar_sprite("hero1",p1)
        self.handle_events()
        self.update() """

    #def handle_events(self):
       # pass
    #def update(self):
        #self.sprites["hero1"].x += 100