import pygame
import random

#Initialize
pygame.init()

#creating screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load(r"D:\Python projects\Python-modules\Python-Modules\Pygame\background.png")

#title
pygame.display.set_caption("Space Invaders")

#icon
icon = pygame.image.load(r"D:\Python projects\Python-modules\Python-Modules\Pygame\ufo.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load(r'D:\Python projects\Python-modules\Python-Modules\Pygame\battleship.png')
playerx = 370
playery = 480
playerx_change = 0

#enemy
enemyImg = pygame.image.load(r'D:\Python projects\Python-modules\Python-Modules\Pygame\enemy.png')
enemyx = random.randint(0, 736)
enemyy = random.randint(50, 150)
enemyx_change = 4
enemyy_change = 40

#bullet
bulletImg = pygame.image.load(r'D:\Python projects\Python-modules\Python-Modules\Pygame\bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = 'ready'

def player(x, y):   
    screen.blit(playerImg, (x, y))

def enemy(x, y):   
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):  
    global bullet_state
    bullet_state = 'fire' 
    screen.blit(bulletImg, (x+16, y+10))

#Game loop
running = True
while running: 
    #changing background colors
    screen.fill((0,255,255))
    #changing background picture
    screen.blit(background, (0, 0))
    
    #capturing the  key
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:   
                playerx_change = -5
            if event.key == pygame.K_RIGHT:  
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                bulletx = playerx
                fire_bullet(bulletx, bullety)
        
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:  
                playerx_change = 0
            
    playerx += playerx_change
    
    #player movement
    if playerx <= 1 :  
        playerx = 1 
    elif playerx >= 735:  
        playerx = 735
    
    enemyx += enemyx_change
    
    #enemy movement
    if enemyx <= 1 :  
        enemyx_change = 4
        enemyy += enemyy_change
    elif enemyx >= 735:  
        enemyx_change = -4
        enemyy += enemyy_change 
    
    #bullet movement
    if bullety <= 0 :  
        bullety = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':   
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change
        
    player(playerx, playery)
    enemy(enemyx, enemyy)
    pygame.display.update()