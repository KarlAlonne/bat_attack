import pygame 
import os 
import random 

BACKGROUND_HIGTH=500 
BACKGROUND_HEIGTH=800 

SPRITE_ROCK = pygame.transform.scale2x(pygame.image.load(os.path.join('sprites','1234.png')))
SPRITE_GROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('sprites','45.png')))
SPRITE_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('sprites','12.png')))
SPRITES_BAT = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('sprites','1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('sprites','2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('sprites','3.png'))),
]  

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class BAT:
    sprites = SPRITES_BAT
    ROTACAO_MAXIMA = 25
    VELOCIDADE_MAXIMA = 20
    TEMPO_ANIMACAO = 5 

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = sprites(0)

    def pular(self):
        self.velocime = -10.5
        self.tempo = 0
        self.altura = self.y

class ROCK:
    pass

class GROUND:
    pass