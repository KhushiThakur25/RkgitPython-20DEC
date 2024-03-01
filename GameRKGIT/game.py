# Gameboard / screen
# object rendering
# event handling
# object animate
# collision detection

#-pygame
import pygame
pygame.init()
screenWidth = 1000
screenHeight = 500
white = 255,255,255
size = screenWidth,screenHeight
screen = pygame.display.set_mode(size)
bg = pygame.image.load('bgg.png')
move_x = 0
move_y = 0
speed = 0.5
x,y,w,h = 0,0,50,50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = speed
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -speed
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = speed
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -speed
                move_x = 0
        # else:
        #         move_x = 0
        #         move_y = 0
    x += move_x
    y += move_y

    if x > screenWidth - w:
        move_x -= speed
    elif x < 0:
        move_x = speed
    elif y > screenHeight - h:
        move_y -= speed
    elif y < 0:
        move_y = speed 
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,white,[x,y,w,h])
    pygame.display.flip()


