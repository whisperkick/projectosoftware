import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS
'''
Objects
'''
class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey(ALPHA) # set alpha
    def control(self,x,y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y
    def update(self):
        '''
        Update sprite position
        '''
        self.rect.x = self.rect.x + self.movex    
        self.rect.y = self.rect.y + self.movey
        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 4:
                self.frame = 0
            self.image = self.images[self.frame//ani]
            

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.images[(self.frame)]
            
    def detenido(self):
        self.image = self.images[0]



'''
Setup
'''
worldx = 960
worldy = 720
fps   = 40  # frame rate
ani   = 4   # animation cycles
clock = pygame.time.Clock()
pygame.init()
world    = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load("Images/Background.png").convert()
backdropbox = world.get_rect()
ALPHA = (0, 255, 0)
player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move
main = True
'''
Main Loop
'''

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
           
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)
    player.update()