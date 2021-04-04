import pygame
import Setup
import Stats_Base
import RunSprites as spr

def endgame():
    
    Setup.janela.fill((0,0,0))
    
    faleceu=Setup.fim.render('VOCÊ MORREU!',1,(255,255,255))
    proximo=Setup.continuar.render('Para continuar aperte C ou para sair feche a tela',1,(255,255,255))
    Setup.janela.blit(faleceu,(10,250))
    Setup.janela.blit(proximo,(75,400))