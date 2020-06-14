import Setup
import Stats_Base
import pygame

def Inicio():  

    texto=Setup.inicio.render('Bem vindo a Kléber e a Dungeon',1,(255,255,255))
    infinitaa=Setup.infinita.render('INFINITA!',1,(255,255,255))
    botão_iniciar=Setup.iniciar.render('Clique em qualquer lugar da tela para iniciar o jogo',1,(255,255,255))
    Setup.janela.blit(texto, (130,150))
    Setup.janela.blit(botão_iniciar, (135,350))
    Setup.janela.blit(infinitaa,(250,200))
