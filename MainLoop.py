#tela inicial do pygame com as infos do game (classes) e um botão de iniciar game e uma telinha de intruções!
import pygame
pygame.init()

import  Setup
Setup.janela

import TelaInicial
import Intruções
import RunSprites as spr

import Stats_Base
import Combate
import random

jogo = Setup.jogo
estado = Setup.TELAINICIAL

while jogo:

    Setup.FPS.tick(30)
    Setup.janela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo=False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if estado == Setup.TELAINSTRUÇÕES:
                estado = Setup.EMCOMBATE
            
            if estado == Setup.TELAINICIAL:
                estado = Setup.TELAINSTRUÇÕES
        
        elif event.type == pygame.KEYDOWN:
            if estado == EMCOMBATE:
                if type(turno) == Stats_Base.Heroi:
                    if event.key == pygame.K_a:
                        turno.state = "ATACAR"

    if estado == Setup.TELAINICIAL:
        TelaInicial.Inicio()

    elif estado == Setup.TELAINSTRUÇÕES:
        Intruções.intrucoes()

    elif estado == Setup.EMCOMBATE:
        Combate.funcao_combate()

    pygame.display.update()        

pygame.quit()