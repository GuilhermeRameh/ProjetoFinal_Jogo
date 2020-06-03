import pygame
import Stats_Base
import random 


# def lista_player_inimigos(p1, i1):
#     players.append(p1)
#     inimigos.append(i1)

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

#print player_ataque
# Loop de combate:
# Esse loop serve para rodar os dados de batalha e manter a batalha ativa
# enquanto tanto o inimigo como o heroi têm hp

