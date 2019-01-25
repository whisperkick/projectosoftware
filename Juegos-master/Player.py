import pygame
import sys
import os

class Player(pygame.sprite.Sprite):

    def __init__(self, player_id):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.frameL = 0 # player moves to the left

        self.player_id = player_id
        self.images = [] #moving to the right
        self.throw = []  # player throws object - arm movement only
        self.player_dies = [] #player dies
        self.player_gets_hurt = [] #player is injuried by the other player

        self.wfq = 4 # frames walking
        self.twq = 0 # frames throwing an object
        self.dwq = 0 # frames dying
        self.total_frames = self.wfq + self.twq + self.dwq
        self.ani = 4
        self.ALPHA = (255, 255, 255)

        self.set_animaciones()


    def set_animaciones(self):
        
        for i in range(1, self.total_frames + 1):
            img = pygame.image.load(os.path.join('images/personajes/' + str(self.player_id), str(self.player_id) + str(i) + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(self.ALPHA)  # set alpha

   
    
    def control(self, x, y):
        #control player movement
        self.movex += x
        self.movey += y

    def update(self):        
        #Update sprite position        
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        
        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > self.wfq:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // -1], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > self.wfq - 1:
                self.frame = 0
            self.image = self.images[(self.frame)]

    def detenido(self):
        self.image = self.images[0]


