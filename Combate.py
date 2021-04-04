import pygame
import Stats_Base
import Setup
import random
import TelaInicial
import RunSprites as spr

player = Setup.player
inimigo = Setup.inimigo

def ordem_com(player, inimigo):

    vel_P = player.stats['Velocidade']
    vel_I = inimigo.stats['Velocidade']

    if vel_I > vel_P:
        ordem = [inimigo, player]
    else:
        ordem = [player, inimigo]

    return ordem

def player_ataque(player, inimigo):
    hit = random.randint(1, 100)
    if hit <= player.ataque_hit:
        inimigo.vida_variavel -= player.dano
    else:
        inimigo.vida_variavel -= int(random.uniform(player.dano/3, player.dano/2))

def inimigo_ataque(player, inimigo):
    hit = random.randint(1, 100)
    if hit <= inimigo.stats['Força']:
        player.vida_variavel -= inimigo.dano
    else:
        player.vida_variavel -= int(random.uniform(inimigo.dano/3, inimigo.dano/2))

def player_heal(player):
    if player.vida_variavel < player.vida:
        player.vida_variavel += player.heal
    if player.vida_variavel > player.vida:
        player.vida_variavel = player.vida

def print_vida():
    janela = Setup.janela

    if player.vida_variavel == player.vida:
        janela.blit(spr.heart[100], [90, 220])
    elif 3*player.vida/4 < player.vida_variavel <= player.vida:
        janela.blit(spr.heart[75], [90, 220])
    elif player.vida/2 < player.vida_variavel <= 3*player.vida/4:
        janela.blit(spr.heart[50], [90, 220])
    elif player.vida/4 < player.vida_variavel <= player.vida/2:
        janela.blit(spr.heart[25], [90, 220])
    elif 0 < player.vida_variavel <= player.vida/4:
        janela.blit(spr.heart[0], [90, 220])

    if inimigo.vida_variavel == inimigo.vida:
        janela.blit(spr.heart[100], [640, 220])
    elif 3*inimigo.vida/4 < inimigo.vida_variavel <= inimigo.vida:
        janela.blit(spr.heart[75], [640, 220])
    elif inimigo.vida/2 < inimigo.vida_variavel <= 3*inimigo.vida/4:
        janela.blit(spr.heart[50], [640, 220])
    elif inimigo.vida/4 < inimigo.vida_variavel <= inimigo.vida/2:
        janela.blit(spr.heart[25], [640, 220])
    elif 0 < inimigo.vida_variavel <= inimigo.vida/4:
        janela.blit(spr.heart[0], [640, 220])
    elif inimigo.vida_variavel <= 0:
        janela.blit(spr.death, [640, 220])


def funcao_combate():
    janela = Setup.janela
    inicio = Setup.inicio
    
    Setup.FPS.tick(0.5)
    Setup.janela.blit(spr.fundo_1, [0,0])
    janela.blit(spr.kleber, [50, 300])
    janela.blit(spr.jorge, [650, 310])
    print_vida()


    ordem = ordem_com(player, inimigo)
    turno = ordem[Setup.i]

    janela.blit(spr.fundo_1, [0,0])
    declara_turno = inicio.render("Turno de {0}, o(a) {1}".format(turno.nome, turno.classe), 15, (255,255,255))
    janela.blit(declara_turno, (160, 30))
    janela.blit(spr.kleber, [50, 300])
    janela.blit(spr.jorge, [650, 310])
    print_vida()
    
    if type(turno) == Stats_Base.Heroi:
        # print('heroi')
        janela.blit(spr.kleber, [50, 300])
        janela.blit(spr.jorge, [650, 310])
        print_vida()

        if turno.state == "ATACAR":
            # print('ataca')
            vida_anterior = inimigo.vida_variavel
            player_ataque(player, inimigo)
            turno.state = "NEUTRO"

            player_ataca = inicio.render("{0}, o(a) {1} ataca!".format(turno.nome, turno.classe), 15, (255,255,255))
            dano = inicio.render("O ataque causa {0} dano!" .format(vida_anterior - inimigo.vida_variavel), 15, (255,255,255))
            janela.blit(spr.fundo_1, [0,0])
            janela.blit(player_ataca, (180, 30))
            janela.blit(dano, (200, 60))
            janela.blit(spr.kleber, [50, 300])
            janela.blit(spr.jorge, [650, 310])
            print_vida()
            Setup.ataque_espada.play()

            if Setup.i == 0:
                Setup.i = 1
            else:
                Setup.i = 0
        
        if turno.state == "HEAL":
            if Setup.h == 0:
                player_heal(player)
                janela.blit(spr.fundo_1, [0,0])
                janela.blit(spr.kleber, [50, 300])
                janela.blit(spr.jorge, [650, 310])
                print_vida()
                titulo = inicio.render("{0} cura {1} de vida!" .format(turno.nome, player.heal), 15, (255,255,255))
                janela.blit(titulo, (200, 30))
                turno.state = "NEUTRO"
                Setup.h = 3
                if Setup.i == 0:
                    Setup.i = 1
                else:
                    Setup.i = 0
            else:
                cura = Setup.inicio.render("Você  não pode realizar essa ação.", 15, (255,255,255))
                espera = Setup.inicio.render("Espere mais {0} turnos para fazê-lo.".format(Setup.h), 15, (255,255,255))
                Setup.janela.blit(cura, (150, 60))
                Setup.janela.blit(espera, (140, 90))

    elif type(turno) == Stats_Base.Inimigo:
        # print('inimigo')
        ataque_aleatorio = random.randint(1, 100)
        if ataque_aleatorio > 41 - turno.level:
            turno.state = 'ATACAR'
            # print('ataca')
            # print(player.vida)
            vida_anterior = player.vida_variavel
            inimigo_ataque(player, inimigo)
            # print(player.vida)
            turno.state = 'NEUTRO'

            janela.blit(spr.fundo_1, [0,0])
            inimigo_ataca = inicio.render("{0}, o(a) {1} ataca!".format(turno.nome, turno.classe), 15, (255,255,255))
            janela.blit(inimigo_ataca, (150, 30))
            inimigo_ataca2 = inicio.render("O ataque causa {0} dano!" .format(vida_anterior - player.vida_variavel), 15, (255,255,255))
            janela.blit(inimigo_ataca2, (165, 60))
            janela.blit(spr.kleber, [50, 300])
            janela.blit(spr.jorge, [650, 310])
            print_vida()
            Setup.ataque_lobo.play()

#                   mantem no turno do player repetindo o main loop e assim
#                   que o inimigo faz sua ação já troca para o player de novo
        else:
            # print('nao ataca')
            janela.blit(spr.fundo_1, [0,0])
            inimigo_nao_ataca = inicio.render("{0}, o(a) {1} não faz nada...".format(turno.nome, turno.classe), 15, (255,255,255))
            janela.blit(inimigo_nao_ataca, (50, 30))
            janela.blit(spr.kleber, [50, 300])
            janela.blit(spr.jorge, [650, 310])
            print_vida()
        
        if Setup.i == 0:
            Setup.i = 1
        else:
            Setup.i = 0
        if Setup.h > 0:
            Setup.h -= 1
        else:
            Setup.h = 0

ganhar_xp = True

def xp(player, inimigo):
    player.xp += inimigo.xp
    ganhar_xp = False