#tela inicial do pygame com as infos do game (classes) e um botão de iniciar game e uma telinha de intruções!
import pygame

pygame.init()

janela=pygame.display.set_mode((800,500))
pygame.display.set_caption('Jogo RPG')

pygame.font.init()
fonte=pygame.font.get_default_font()
inicio=pygame.font.SysFont(fonte, 50)
iniciar=pygame.font.SysFont(fonte, 30)
infinita=pygame.font.SysFont(fonte, 90)

jogo=True

while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo=False

    janela.fill((0,0,0))
    
    texto=inicio.render('Bem vindo a Kleber e a Dungeon',1,(255,255,255))
    infinitaa=infinita.render('INFINITA!',1,(255,255,255))
    botão_iniciar=iniciar.render('Clique em qualquer lugar da tela para iniciar o jogo',1,(255,255,255))
    janela.blit(texto, (130,150))
    janela.blit(botão_iniciar, (135,350))
    janela.blit(infinitaa,(250,200))
    
    pygame.display.update()        

pygame.quit()