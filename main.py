import pygame
import sys

from pygame.locals import *

def movement():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                if speed[0] == 1:
                    speed[0] = 0
                else:    
                    speed[0] = 1
            if event.key == pygame.K_LEFT:
                if speed[0] == -1:
                    speed[0] = 0
                else:    
                    speed[0] = -1
            if event.key == pygame.K_SPACE:
                speed[0] = 0
clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("My Game")

Tile_SIZE = 16
width_tiles = 10
height_tiles = 20
size = width, height = Tile_SIZE * width_tiles, Tile_SIZE * height_tiles

speed = [0, 0]
black = 0, 0, 0
bgspeed = [0,1]
### backgroun ####
bg1 = pygame.Rect(0,0,width, height)
bg2 = pygame.Rect(0, -height, width, height)
bg_image= pygame.image.load("images/bg.png")
#####

screen = pygame.display.set_mode((size[0]*2, size[1]*2))
display = pygame.Surface(size)
player_imageR = pygame.image.load("images/player.png")
player_imageL = pygame.transform.flip(player_imageR,True,False)
playerrect = player_imageR.get_rect()

grass_image = pygame.image.load("images/grass.png")
grassrect = grass_image.get_rect()

dirt_image = pygame.image.load("images/dirt.png")
dirtrect = dirt_image.get_rect()

speed = [0,1]

floor = []
for x in range(width_tiles):
    floor_tile = pygame.Rect(x*Tile_SIZE, height - Tile_SIZE, Tile_SIZE,Tile_SIZE)
    floor.append(floor_tile)
    

while True:
    movement()
            # if event.key == pygame.K_UP:
            #     speed[1] -= 1
            # if event.key == pygame.K_DOWN:
            #     speed[1] += 1

    #pygame.display.flip()
    display.fill(black)
    
    display.blit(bg_image, bg1)
    display.blit(bg_image, bg2)

    bg1 = bg1.move(bgspeed)
    bg2 = bg2.move(bgspeed)

    if bg1[1] >= height:
        bg1[1] = -height
    if bg2[1] >= height:
        bg2[1] = -height
    for rect in floor:
        display.blit(grass_image, rect)

    
    if speed[0] == -1:
        display.blit(player_imageL, playerrect)
    else:
        display.blit(player_imageR, playerrect)
    #print (playerrect.move(speed).collidelist(floor))
    if playerrect.move(speed).collidelist(floor) != -1:
        
        speed[1] = 0
    playerrect = playerrect.move(speed)
    screen.blit(pygame.transform.scale(display,(size[0]*2, size[1]*2)),(0,0))


    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)