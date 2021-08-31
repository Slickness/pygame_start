import pygame
import sys


clock = pygame.time.Clock()
pygame.init()

size = width, height = 400, 400

speed = [0, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

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
                speed[0] += 1
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    
    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)