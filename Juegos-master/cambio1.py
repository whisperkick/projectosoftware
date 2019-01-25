import pygame

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        self.x = 0
        self.y = 0
        self.ancho = 10
        self.alto = 10
        

class Pantalla:
    def __init__(self, objeto):
        self.objeto = objeto
        self.screen_dim = [1280, 800]
        self.iniciar_pantalla()
        self.fondo = ''
        self._bool_sgt_pnt = False #Cambiar a la siguiente pantalla
        #self.botones = [] #Almacenará el objeto boton como imagen
        #self.textos = [] #Almacenará el objeto boton, y el area que ocupa (tupla esq-largo-ancho)
        self.obj_pressed = None #Indica que objeto está siendo presionado en un momento determinado
        self.result_fun_n = None
        self.mensaje = [None, 0] #es el texto que se va a enviar al motor (0), y de ser el caso reenviado al servidor(1)

        self.world = 0 
        self.backdrop = 0
        self.backdropbox = 0
        self.clock = 0
        self.fps   = 40  # frame rate        
        self.clock = pygame.time.Clock()


    def set_objeto(self, nuevo_objeto):
        self.objeto = nuevo_objeto


    def set_bool_sgt_pnt(self, b):
        self._bool_sgt_pnt = b


    def iniciar_pantalla(self):            
        ani   = 4   # animation cycles
        clock = pygame.time.Clock()
        pygame.init()    
   

    def cambiar_fondo(self, fondo, titulo="Abajo los corruptos"):
        self.world = pygame.display.set_mode(self.screen_dim)
        pygame.display.set_caption(titulo)  
        self.backdrop = pygame.image.load(os.getcwd() + "/images/menu/" + fondo + ".jpeg").convert()    
        self.backdropbox = self.world.get_rect()


    def dibujar_botones(self, img_botones=[], pocs = [] ):        
        k = len(img_botones)
                
        for i in range(k):
            self.world.blit(img_botones[i], pocs[i])
    
    
    def lugar_funcional(self, pos, img_pos=[], img_tam=[]):
        #devuelve si se presionó o no un objeto     
        #pos --> posición del mouse (x,y)
        #img_botones = [esquina, dimensiones]
        rango_x = [0,0]
        rango_y = [0,0]
        nr = len(img_pos) #número de img_botones
        
        #¿Los botones son del mismo tamaño?
        nt = len(img_tam)
        largo = 0
        alto = 0


        #El mouse se encuentra en el rango definido previamente
        cx = False 
        cy = False

        #verificar cada región funcional (botones, text_box)
        for i in range(nr):
            if nt == 1:
                largo = img_tam[0][0]
                alto = img_tam[0][1]
            else:
                largo = img_tam[i][0]
                alto = img_tam[i][1]

            #[pos_en_array        (x,y)]
            rango_x = [img_pos[i][0], img_pos[i][0] + largo]
            rango_y = [img_pos[i][1], img_pos[i][1] + alto]
            
            #definir booleanos
            cx = (pos[0] >= rango_x[0]) and (pos[0] <= rango_x[1] + 1)
            cy = (pos[1] >= rango_y[0]) and (pos[1] <= rango_y[1] + 1)


            #compara la posición del mouse con los rangos establecidos
            if (cx and cy):
                print("Se ha presionado el lugar funcional " + str(i))
                #print(str(type(self.objeto)))
                #Se modifica el valor de la variable self.obj_pressed
                
                if i == 0:
                    if (str(type(self.objeto)) == "<class 'prejuego.Login.Login'>"):
                        #Obtener de los inputbox
                        usuario = ''
                        psw = ''
                        #print('enviar usuario y contraseña')
                        men_enc = self.objeto.ejecutar_funcion_n(i, [usuario, psw])
                        self.mensaje = [men_enc, 1]
                    else:
                        #pasar a la siguiente pantalla
                        self._bool_sgt_pnt = True

class Personajes():
    def __init__(self):
        self.imgs=[] #imágenes de los botones 
        self.pcs = []    #estarán uniformemente distribuidos
        self.sizes = [(200,150)]  #Tamaño único
        
        
        self.distribuir_imagenes()
        self.cargar_imagenes()
        self.clave_simetrica = None #Tras haberse autenticado el usuario, se empezará a usar criptografía simétrica

    
    def distribuir_imagenes(self,pos_x,pos_y):
        for i in range(len(self.personajes)):
            #MOdificar valores cuando se tenga las imágenes finales
            tupla_pos = (pos_X, pos_y)
            self.pcs.append(tupla_pos)



    def cargar_imagenes(self,imagen):
        #Cargar a memoria las imágenes de los botones
        
        self.personajes = pygame.sprite.Group()
        personajes.add(imagen)
      
       '''' per_0 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        per_1 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        per_2 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        per_3 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        per_4 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")

        #Darles el tamaño apropiado
        Modificar los tamaños
              
        per_0 = pygame.transform.scale(per_0, self.sizes[0])
        per_1 = pygame.transform.scale(per_1, self.sizes[0])
        per_2 = pygame.transform.scale(per_2, self.sizes[0])
        per_3 = pygame.transform.scale(per_3, self.sizes[0])
        per_4 = pygame.transform.scale(per_3, self.sizes[0])
        self.imgs = [per_0, per_1, per_2, per_3, per_4]''''

    def ejecutar_funcion_n(self, n, otros=[]):
        pass

    
class EjemploPantalla(Pantalla):
    def __init__(self, canvas):
        Pantalla.__init__(self, canvas)
        p1 = Pelota()
        p1.agregar_sprite(p1)

    def handle_events(self):
        pass
    def update(self):
        self.sprites[0].x = 400