import pygame
import os

'''
MARIO
Cuando ya estén las imágenes de los botones, modificas los números 
para que tengan el tamaño y posición adecuados
'''
class Personajes():
    def __init__(self):
        self.imgs=[] #imágenes de los botones 
        self.pcs = []    #estarán uniformemente distribuidos
        self.sizes = [(200,150)]  #Tamaño único
        
        self.distribuir_imagenes()
        self.cargar_imagenes()
        self.clave_simetrica = None #Tras haberse autenticado el usuario, se empezará a usar criptografía simétrica

    
    def distribuir_imagenes(self):
        for i in range(5):
            #MOdificar valores cuando se tenga las imágenes finales
            pos_X = 80 + i*200
            pos_y = 100
            tupla_pos = (pos_X, pos_y)
            self.pcs.append(tupla_pos)



    def cargar_imagenes(self):
        #Cargar a memoria las imágenes de los botones
        per_0 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        per_1 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        per_2 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        per_3 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        per_4 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")

        '''
        #Darles el tamaño apropiado
        Modificar los tamaños
        '''        
        per_0 = pygame.transform.scale(per_0, self.sizes[0])
        per_1 = pygame.transform.scale(per_1, self.sizes[0])
        per_2 = pygame.transform.scale(per_2, self.sizes[0])
        per_3 = pygame.transform.scale(per_3, self.sizes[0])
        per_4 = pygame.transform.scale(per_3, self.sizes[0])
        self.imgs = [per_0, per_1, per_2, per_3, per_4]

    def ejecutar_funcion_n(self, n, otros=[]):
        pass

    