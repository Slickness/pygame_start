import pygame
import sys

from pygame.locals import *


clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("My Game")

size = width, height = 200, 600

speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode((size[0]*2, size[1]*2))
display = pygame.Surface(size)
player_image = pygame.image.load("images/player.png")
playerrect = player_image.get_rect()

grass_image = pygame.image.load("images/grass.png")
grassrect = grass_image.get_rect()

dirt_image = pygame.image.load("images/dirt.png")
dirtrect = dirt_image.get_rect()

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed[0] += 1
            if event.key == pygame.K_LEFT:
                speed[0] -= 1
            if event.key == pygame.K_UP:
                speed[1] -= 1
            if event.key == pygame.K_DOWN:
                speed[1] += 1
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    pygame.display.flip()
    display.fill(black)
    display.blit(ball, ballrect)
    test = pygame.draw.rect(display, (255,0,0), pygame.Rect(100, 100, 60, 60))
    screen.blit(pygame.transform.scale(display,size),(0,0))


    
    if ballrect.colliderect(test):
        print ("hit")
    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)