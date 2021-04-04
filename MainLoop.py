#tela inicial do pygame com as infos do game (classes) e um botão de iniciar game e uma telinha de intruções!
import pygame
pygame.init()

import  Setup
Setup.janela

import TelaInicial
import Intruções
import RunSprites as spr
import EndGame
import EntreCombates
import historia

import Stats_Base
import Combate
import random

player = Setup.player
inimigo = Setup.inimigo

jogo = Setup.jogo
estado = Setup.TELAINICIAL
i = 0

while jogo:

    to_level = 25*(player.level + 1)
    Setup.FPS.tick(30)
    Setup.janela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo=False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if estado == Setup.TELAINSTRUÇÕES:
                estado = Setup.EMCOMBATE
            
            if estado == Setup.HISTORIA4:
                estado = Setup.TELAINSTRUÇÕES
            if estado == Setup.HISTORIA3:
                estado = Setup.HISTORIA4
            if estado == Setup.HISTORIA2:
                estado = Setup.HISTORIA3
            if estado == Setup.HISTORIA1:
                estado = Setup.HISTORIA2            
            
            if estado == Setup.TELAINICIAL:
                estado = Setup.HISTORIA1
        
        elif event.type == pygame.KEYDOWN:
            if estado == Setup.EMCOMBATE:
                if type(turno) == Stats_Base.Heroi:
                    if event.key == pygame.K_a:
                        turno.state = "ATACAR"
                    if event.key == pygame.K_h:
                        turno.state = "HEAL"


            if estado == Setup.GAMEOVER:
                if event.key == pygame.K_c:
                    player.restart()

                    inimigo.restart(player.level)

                    estado = Setup.TELAINICIAL
                    Setup.i = 0

            if estado == Setup.LEVELUP:
                if event.key == pygame.K_c:
                        estado = Setup.EMCOMBATE
                        inimigo.Update(player.level)

            elif estado == Setup.ENTRECOMBATE:
                if event.key == pygame.K_c:
                    if player.level_up == False:
                        estado = Setup.EMCOMBATE
                        inimigo.restart(player.level)
                    else:
                        estado = Setup.LEVELUP
                        Setup.levelup_sound.play() 
            

    if estado == Setup.TELAINICIAL:
        TelaInicial.Inicio()

    elif estado == Setup.TELAINSTRUÇÕES:
        Intruções.intrucoes()
        Stats_Base.create()
        player = Setup.player
        inimigo = Setup.inimigo

    elif estado == Setup.GAMEOVER:
        EndGame.endgame()
    
    elif estado == Setup.HISTORIA4:
        historia.historia4()
    elif estado == Setup.HISTORIA3:
        historia.historia3()
    elif estado == Setup.HISTORIA2:
        historia.historia2()
    elif estado == Setup.HISTORIA1:
        historia.historia1()

    elif estado == Setup.LEVELUP:
        ganhar_xp = False
        Stats_Base.Heroi.Update(player)
        Setup.janela.blit(spr.fundo_1, [0,0])
        Setup.janela.blit(spr.kleber, [50, 300])
        Combate.print_vida()
        parabens = Setup.inicio.render("Parabéns! {0} passou de nível!".format(player.nome), 15, (255,255,255))
        level = Setup.inicio.render("Agora seu level é {0}. ".format(player.level), 15, (255,255,255))
        aviso = Setup.iniciar.render("Conforme você sobe de nível os inimigos ficarão mais fortes também.", 15, (255,255,255))
        Setup.janela.blit(parabens, (150, 30))
        Setup.janela.blit(level, (170, 60))
        Setup.janela.blit(aviso, (100, 440))
        player.level_up = False

    elif estado == Setup.ENTRECOMBATE:
        Setup.i = 0
        EntreCombates.entrecombate()
        if player.xp >= to_level:
            player.level_up = True

    elif estado == Setup.EMCOMBATE:
        if player.vida_variavel <= 0:
            Setup.som_final.play()
            estado = Setup.GAMEOVER
        elif inimigo.vida_variavel <= 0:
            estado = Setup.ENTRECOMBATE
            Combate.ganhar_xp = True
            Setup.victory.play()
        ordem = Combate.ordem_com(player, inimigo)
        turno = ordem[Setup.i]
        if player.vida_variavel > 0 and inimigo.vida_variavel > 0:
            Combate.funcao_combate()

    pygame.display.update()

pygame.quit()