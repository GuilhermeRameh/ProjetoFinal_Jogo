import pygame
import Stats_Base
import Setup
import random 
import RunSprites as spr

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
        inimigo.vida -= player.dano
    else:
        inimigo.vida -= int(random.uniform(player.dano/3, player.dano/2))

def inimigo_ataque(player, inimigo):
    hit = random.randint(1, 100)
    if hit <= inimigo.stats['Força']:
        player.vida -= inimigo.dano
    else:
        player.vida -= int(random.uniform(inimigo.dano/3, inimigo.dano/2))

def funcao_combate():

    janela = Setup.janela
    inicio = Setup.inicio
    i = Setup.i

    Setup.FPS.tick(0.5)
    Setup.janela.blit(spr.fundo_1, [0,0])

    player = Stats_Base.Guerreiro
    inimigo = Stats_Base.Lobo
    ordem = ordem_com(player, inimigo)
    turno = ordem[i]

    janela.blit(spr.fundo_1, [0,0])
    declara_turno = inicio.render("Turno de {0}, o(a) {1}".format(turno.nome, turno.classe), 15, (255,255,255))
    janela.blit(declara_turno, (160, 30))
    
    if type(turno) == Stats_Base.Heroi:
        print('heroi')

        if turno.state == "ATACAR":
            print('ataca')
            player_ataque(player, inimigo)
            turno.state = "NEUTRO"
            
            player_ataca = inicio.render("{0}, o(a) {1} ataca!".format(turno.nome, turno.classe), 15, (255,255,255))
            janela.blit(spr.fundo_1, [0,0])
            janela.blit(player_ataca, (180, 30))

            if i == 0:
                i = 1
            else:
                i = 0
    

    elif type(turno) == Stats_Base.Inimigo:
        print('inimigo')
        ataque_aleatorio = random.randint(1, 2)
        if ataque_aleatorio == 2:
            turno.state = 'ATACAR'
            print('ataca')
            vida_original = ordem[i+1].vida
            inimigo_ataque(player, inimigo)
            turno.state = 'NEUTRO'

            janela.blit(spr.fundo_1, [0,0])
            inimigo_ataca = inicio.render("{0}, o(a) {1} ataca!".format(turno.nome, turno.classe), 15, (255,255,255))
            janela.blit(inimigo_ataca, (150, 30))
            inimigo_ataca2 = inicio.render("O ataque causa {0} dano!" .format(vida_original - ordem[i+1].vida), 15, (255,255,255))
            janela.blit(inimigo_ataca2, (165, 60))
            
#                   mantem no turno do player repetindo o main loop e assim
#                   que o inimigo faz sua ação já troca para o player de novo
        else:
            print('nao ataca')

            janela.blit(spr.fundo_1, [0,0])
            inimigo_nao_ataca = inicio.render("{0}, o(a) {1} não faz nada...".format(turno.nome, turno.classe), 15, (255,255,255))
            janela.blit(inimigo_nao_ataca, (90, 30))
        if i == 0:
            i = 1
        else:
            i = 0
