#tela inicial do pygame com as infos do game (classes) e um botão de iniciar game e uma telinha de intruções!
import pygame

pygame.init()

janela=pygame.display.set_mode((1000,650))
pygame.display.set_caption('Jogo RPG')

jogo=True
while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo=False
    
    janela.fill((0,0,0))
    
    pygame.display.update()        

pygame.quit()