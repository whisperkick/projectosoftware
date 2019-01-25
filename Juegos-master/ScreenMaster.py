import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS

'''
pygame debe tener librerías con estas funcionalidades, pero 
solo encontré para dibujar formas geométricas
    #import Boton as btn
    #import CajaTexto as txb
'''


class ScreenMaster(pygame.sprite.Sprite): 
            
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


    #Ya no se usará; sin embargo puede servir de referencia
    #para algún cambio en loopear_2()
    def loopear(self, repetir, fondo=''):        
        
        sc_login = self.objeto
        sc_login.cargar_imagenes()
        #self.botones = sc_login.imgs
        #str_sgt_pnt = 'login' #Nombre del siguiente fondo a cargar
        
        while repetir:
            pres = False # Botón izq del mouse presionado
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                    main = False            
                
                #Verificar si el botón del mouse está presionado
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pres = True
                
                #######################
                #######################
                ###presionar  enter####
                #######################
                #######################    

            if pres:
                #retorna una tupla (x,y) de las coordenadas del mouse
                pos = pygame.mouse.get_pos()
                #print(str(pos))
                self.lugar_funcional(pos, sc_login.pcs, sc_login.sizes)
                if self.obj_pressed != None :
                    self.accion_obj_presionado(self.obj_pressed)
                self.obj_pressed = None

            if self._bool_sgt_pnt:
                self.cambiar_fondo(fondo)
                #Posiblemente main = False
            
            
            #Mantener viva la ventana 
            self.world.blit(self.backdrop, self.backdropbox)    
            self.dibujar_botones(sc_login.imgs, sc_login.pcs)
            pygame.display.flip()
            self.clock.tick(self.fps)

    
    def loopear_2(self):
        
        if not self._bool_sgt_pnt:
            # Botón izq del mouse presionado 
            # corregir, por ahora responde a cualquier boton, scroll
            pres = False 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                    main = False            
                
                #Verificar si el botón del mouse está presionado
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pres = True
                
                #######################
                #######################
                ###presionar  enter####
                #######################
                #######################    

            if pres:
                #retorna una tupla (x,y) de las coordenadas del mouse
                pos = pygame.mouse.get_pos()
                #print(str(pos))
                self.lugar_funcional(pos, self.objeto.pcs, self.objeto.sizes)

            if self._bool_sgt_pnt:
                self.cambiar_fondo(self.fondo)
                #Posiblemente main = False
            
            
            #Mantener viva la ventana 
            self.world.blit(self.backdrop, self.backdropbox)    
            self.dibujar_botones(self.objeto.imgs, self.objeto.pcs)
            pygame.display.flip()
            self.clock.tick(self.fps)





'''       
def main():
    print(3 * "\n")
    print("Hola desde el main")
    abc = ScreenMaster()
    abc.cambiar_fondo("login")
    abc.loopear()

if __name__ == "__main__":
    main()
    
'''    
