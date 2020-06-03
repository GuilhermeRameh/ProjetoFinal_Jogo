#tela de instruções do jogo
import pygame

pygame.init()

janela=pygame.display.set_mode((1000,650))
pygame.display.set_caption('Jogo RPG')

pygame.font.init()
fonte=pygame.font.get_default_font()
dungeon=pygame.font.SysFont(fonte,60)
kleber=pygame.font.SysFont(fonte,60)
tecla=pygame.font.SysFont(fonte,60)
falecer=pygame.font.SysFont(fonte,60)

jogo=True
while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo=False
    
    janela.fill((0,0,0))
    
    intro=dungeon.render('Bem vindo a Dungeon Infinita!',1,(255,255,255))
    intro2=kleber.render('Você controlará o guerreiro Kleber',1,(255,255,255))
    intro3=tecla.render('Aperte a tecla a para atacar no seu turno.',1,(255,255,255))
    intro4=falecer.render('Tente não falecer, boa sorte!',1,(255,255,255))
    janela.blit(intro,(135,100))
    janela.blit(intro2,(135,200))
    janela.blit(intro3,(135,300))
    janela.blit(intro4,(135,400))
    
    pygame.display.update()        

pygame.quit()