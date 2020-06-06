#tela de instruções do jogo
import pygame
import Setup

def intrucoes():
    
    instruções = Setup.instruções
    janela = Setup.janela

    intro=instruções.render('Bem vindo a Dungeon Infinita!',1,(255,255,255))
    intro2=instruções.render('Você controlará o guerreiro Kléber.',1,(255,255,255))
    intro3=instruções.render('Aperte a tecla "a" para atacar no seu turno.',1,(255,255,255))
    intro4=instruções.render('Tente não falecer, boa sorte!',1,(255,255,255))
    janela.blit(intro,(200,100))
    janela.blit(intro2,(160,150))
    janela.blit(intro3,(130,300))
    janela.blit(intro4,(220,400))
        