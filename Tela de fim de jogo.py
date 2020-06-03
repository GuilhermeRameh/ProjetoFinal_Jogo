import pygame

pygame.init()

janela=pygame.display.set_mode((1000,650))
pygame.display.set_caption('Kleber e a Dungeon INFINITA!')

pygame.font.init()
fonte=pygame.font.get_default_font()
fim=pygame.font.SysFont(fonte, 150)
continuar=pygame.font.SysFont(fonte, 40)

jogo=True

while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo=False

    janela.fill((0,0,0))
    
    faleceu=fim.render('VOCÊ MORREU!',1,(255,255,255))
    proximo=continuar.render('Para continuar aperte C ou para sair feche a tela',1,(255,255,255))
    janela.blit(faleceu,(100,250))
    janela.blit(proximo,(200,400))

    pygame.display.update()  

pygame.quit()