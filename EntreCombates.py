import Setup
import pygame
import Combate
import RunSprites as spr

player = Combate.player
inimigo = Combate.inimigo

def entrecombate():
    janela = Setup.janela
    inicio = Setup.inicio

    Setup.janela.blit(spr.fundo_1, [0,0])
    janela.blit(spr.kleber, [50, 300])

    fim_de_combate = Setup.inicio.render("{0}, o(a) {1} é vitorioso!".format(player.nome, player.classe), 15, (255,255,255))
    xp_texto = Setup.inicio.render("{0} recebe {1} de experiência.".format(player.nome, inimigo.xp), 15, (255,255,255))
    continuar = Setup.iniciar.render('Aperte "c" para continuar para o próximo combate.',1,(255,255,255))
    Setup.janela.blit(fim_de_combate, (150, 30))
    Setup.janela.blit(xp_texto, (155, 70))
    Setup.janela.blit(continuar, (150, 440))
    Combate.xp(player, inimigo)

