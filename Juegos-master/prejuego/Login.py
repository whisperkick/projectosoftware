import cryptography
import hashlib
import os
import pygame


'''
MARIO
Cuando ya estén las imágenes de los botones, modificas los números 
para que tengan el tamaño y posición adecuados
'''
class Login():
    def __init__(self):
        self.imgs=[] #imágenes de los botones
        self.pcs = [(0,0),(350,180),(700,360),(1050,540)]    #posición de la esquina superior izquierda
        self.sizes = [(200,100),(200,100),(200,100),(200,100)]  #largo x alto
        self.cargar_imagenes()
        self.clave_publica_Server = None
    
    
    def cargar_imagenes(self):
        #Cargar a memoria las imágenes de los botones
        btn_0 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        btn_1 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        btn_2 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")
        btn_3 = pygame.image.load(os.getcwd() + "/images/botones/registrar.png")

        '''
        #Darles el tamaño apropiado
        Modificar los tamaños
        '''        
        btn_registrar = pygame.transform.scale(btn_0, self.sizes[0])
        btn_olvide = pygame.transform.scale(btn_1, self.sizes[1])
        btn_creditos = pygame.transform.scale(btn_2, self.sizes[2])
        btn_salir = pygame.transform.scale(btn_3, self.sizes[3])
        self.imgs = [btn_registrar, btn_olvide, btn_creditos, btn_salir]


    def ejecutar_funcion_n(self, n, otros=[]):        
        if n == 0: # Intento de inicio de sesión
            #Se obtuvo los textos de los input box
            usr = otros[0]
            psw = self.sha256_psw(otros[1])
            
            #Encriptar usuario y contraseña
            return self.encriptar_usr_psw(usr, psw)
        elif n == 1: # Olvide contraseña
            pass
        elif n == 2: # Nuevo usuario
            pass
        elif n == 3: # Salir
            pass

        
    def set_clave_asimetrica_server(self, clave):
        self.clave_publica_Server = clave

    def encriptar_usr_psw(self, usuario='', psw=''):
        #Calcular el hash de la contraseña
        psw = self.sha256_psw(psw)
        #Encriptado asimétrico con la clave pública suministrada por el server
        usr_enc = None
        psw_enc = None
        print('encriptando')
        return (usr_enc, psw_enc)
        

    def sha256_psw(self, psw=""):
        #https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing        
        psw_hash = hashlib.sha256(psw.encode('utf-8'))
        return psw_hash.hexdigest()