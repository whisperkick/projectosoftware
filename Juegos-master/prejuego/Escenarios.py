import pygame
import os

'''
Cuando ya estén las imágenes de los fondos, modificar los números 
para que tengan el tamaño y posición adecuados
'''
class Escenarios():
    def __init__(self):
        self.imgs=[] #imágenes de los fondos
        self.btns = [] #bones[(imagen, posicion)]
        self.pcs = []    #estarán uniformemente distribuidos
        self.sizes = [(240,150)]  #Tamaño único
        
        self.distribuir_imagenes()
        self.cargar_imagenes()
    
    
    '''
    Crear las fórmulas para distribuir uniformemente los 10
    fondos a elegir
    '''
    def distribuir_imagenes(self):
        for i in range(10):
            pos_X = 0
            pos_y = 0
            tupla_pos = (pos_X, pos_y)
            self.pcs.append(tupla_pos)


    '''
    Cambiar "Background" por el nombre de los archivos
    '''
    def cargar_imagenes(self):
        #Cargar a memoria las imágenes de los fondos
        btn_0 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_1 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_2 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_3 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_0 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_1 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_2 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_3 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_2 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")
        btn_3 = pygame.image.load(os.getcwd() + "/images/fondos/Background.png")

        '''
        #Darles el tamaño apropiado
        Modificar los tamaños
        '''        
        btn_f0 = pygame.transform.scale(btn_0, self.sizes[0])
        btn_f1 = pygame.transform.scale(btn_1, self.sizes[0])
        btn_f2 = pygame.transform.scale(btn_2, self.sizes[0])
        btn_f3 = pygame.transform.scale(btn_3, self.sizes[0])
        btn_f4 = pygame.transform.scale(btn_0, self.sizes[0])
        btn_f5 = pygame.transform.scale(btn_1, self.sizes[0])
        btn_f6 = pygame.transform.scale(btn_2, self.sizes[0])
        btn_f7 = pygame.transform.scale(btn_3, self.sizes[0])
        btn_f8 = pygame.transform.scale(btn_0, self.sizes[0])
        btn_f9 = pygame.transform.scale(btn_1, self.sizes[0])
        
        '''
        Completar esto cuando se necesiciste la pantalla para 
        elegir los fondos; es solo tipear repetitivamente
        '''
        #self.imgs = [btn_f0, ... btn_f9]