import pygame

#Initialize
pygame.init()

#creating screen
screen = pygame.display.set_mode((800, 600))

#title
pygame.display.set_caption("Space Invaders")

#icon
icon = pygame.image.load(r"D:\Python projects\Python-modules\Python-Modules\Pygame\ufo.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load(r'D:\Python projects\Python-modules\Python-Modules\Pygame\battleship.png')
playerx = 370
playery = 480

def player(x, y):   
    screen.blit(playerImg, (x, y))

#Game loop
running = True
while running: 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False 
    
    #changing background colors
    screen.fill((0,255,255))
    player(playerx, playery)
    pygame.display.update()