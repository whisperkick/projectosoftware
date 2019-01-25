import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS
import Player as pl


img_player1 = sys.argv[1]
img_background = sys.argv[2]


'''
Objects
'''
worldx = 1280
worldy = 800
fps   = 40  # frame rate
ani   = 4   # animation cycles
clock = pygame.time.Clock()
pygame.init()
world    = pygame.display.set_mode([worldx,worldy])


#img = pygame.image.load(os.path.join('images/pueblo/' + str(self.player_id), str(self.player_id) + str(i) + '.png')).convert()
backdrop = pygame.image.load("Images/fondos/" + img_background + ".png").convert()
backdropbox = world.get_rect()


'''
Setup
'''
player = pl.Player(img_player1)   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move
main = True

'''
Main Loop
'''

while main:
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
                #print(os.getcwd())
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