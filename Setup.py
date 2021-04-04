import pygame
import Stats_Base
pygame.init()
pygame.mixer.init()

janela=pygame.display.set_mode((800,500))
pygame.display.set_caption('Kléber e a Dungeon INFINITA!')

pygame.font.init()
fonte=pygame.font.get_default_font()
inicio=pygame.font.SysFont(fonte, 50)
iniciar=pygame.font.SysFont(fonte, 30)
infinita=pygame.font.SysFont(fonte, 90)
instruções=pygame.font.SysFont(fonte,40)
fim=pygame.font.SysFont(fonte, 150)
continuar=pygame.font.SysFont(fonte, 40)


# Declara os estados
TELAINICIAL = 1
TELAINSTRUÇÕES = 2
EMCOMBATE = 3
ENTRECOMBATE = 4
LEVELUP = 5
GAMEOVER = 6
HISTORIA1 = 7
HISTORIA2 = 8
HISTORIA3 = 9
HISTORIA4 = 10


FPS = pygame.time.Clock()
 
tecla = pygame.key.get_pressed()

player = Stats_Base.create()[0]
inimigo = Stats_Base.create()[1]

musica=pygame.mixer_music.load ("Audios/cave.ogg")
pygame.mixer.music.play(-1)


ataque_lobo=pygame.mixer.Sound("Audios/animal.wav")
ataque_espada=pygame.mixer.Sound("Audios/sword.wav")
som_final=pygame.mixer.Sound('Audios/defeat.ogg')
levelup_sound = pygame.mixer.Sound('Audios/levelup.ogg')
victory = pygame.mixer.Sound("Audios/Victory.ogg")



i = 0
h = 0
flash = 0

jogo=True