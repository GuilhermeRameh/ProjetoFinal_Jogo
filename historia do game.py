import pygame

pygame.init()

janela=pygame.display.set_mode((800,500))
pygame.display.set_caption('Kleber e a Dungeon INFINITA!')

pygame.font.init()
fonte=pygame.font.get_default_font()
historia=pygame.font.SysFont(fonte, 60)

jogo=True

while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo=False

    janela.fill((0,0,0))
    
    linha1=historia.render('Você, o nobre guerreiro Kleber,',1,(255,255,255))
    linha2=historia.render('se alojou em uma caverna',1,(255,255,255))
    linha3=historia.render('em meio a uma missão.',1,(255,255,255))
    linha4=historia.render('O que você não esperava',1,(255,255,255))
    linha5=historia.render('era que essa caverna era habitada',1,(255,255,255))
    linha6=historia.render('por lobos que não exitaram em matar.',1,(255,255,255))
    linha7=historia.render('Sua nova missão é SOBREVIVER!"',1,(255,255,255))
    janela.blit(linha1,(20,50))
    janela.blit(linha2,(20,110))
    janela.blit(linha3,(20,170))
    janela.blit(linha4,(20,230))
    janela.blit(linha5,(20,290))
    janela.blit(linha6,(20,350))
    janela.blit(linha7,(20,410))
    
    pygame.display.update()  

pygame.quit()