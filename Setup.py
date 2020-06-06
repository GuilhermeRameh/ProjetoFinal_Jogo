import pygame
pygame.init()
pygame.mixer.init()

janela=pygame.display.set_mode((800,500))
pygame.display.set_caption('Jogo RPG')

pygame.font.init()
fonte=pygame.font.get_default_font()
inicio=pygame.font.SysFont(fonte, 50)
iniciar=pygame.font.SysFont(fonte, 30)
infinita=pygame.font.SysFont(fonte, 90)
instruções=pygame.font.SysFont(fonte,40)


# Declara os estados
TELAINICIAL = 1
TELAINSTRUÇÕES = 2
EMCOMBATE = 3

FPS = pygame.time.Clock()

tecla = pygame.key.get_pressed()

i = 0

jogo=True