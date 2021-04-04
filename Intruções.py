#tela de instruções do jogo
import pygame
import Setup

def intrucoes():
    
    instruções = Setup.instruções
    janela = Setup.janela

    intro=instruções.render('Bem vindo a Dungeon Infinita!',1,(255,255,255))
    intro2=instruções.render('Você controlará o guerreiro Kléber.',1,(255,255,255))
    intro3=instruções.render('Aperte a tecla "a" para atacar no seu turno.',1,(255,255,255))
    intro_heal=instruções.render('Aperte a tecla "h" para se curar.',1,(255,255,255))
    intro4=instruções.render('Tente não falecer, boa sorte!',1,(255,255,255))
    botão_iniciar=Setup.iniciar.render('Clique em qualquer lugar da tela para iniciar o jogo',1,(255,255,255))
    janela.blit(intro,(200,70))
    janela.blit(intro2,(160,100))
    janela.blit(intro3,(120,200))
    janela.blit(intro_heal,(175, 230))
    janela.blit(intro4,(220,400))
    janela.blit(botão_iniciar,(150, 450))
        