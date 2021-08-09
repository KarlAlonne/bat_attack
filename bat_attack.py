import pygame
from pygame.locals import *
WIDH_SCREEN=400   #largura da tela #
HEIGHT_SCREEN=800 #altura da tela #
pygame.init()
screen=pygame.display.set_mode((WIDH_SCREEN,HEIGHT_SCREEN))

BACKGROUND=pygame.image.load('123.png') 
BACKGROUND=pygame.transform.scale(BACKGROUND,(WIDH_SCREEN,HEIGHT_SCREEN))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            screen.blit(BACKGROUND(0,0))

            pygame.display.update()