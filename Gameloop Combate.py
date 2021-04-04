import pygame
import Stats_Base
import random 

combate  = True

# def lista_player_inimigos(p1, i1):
#     players.append(p1)
#     inimigos.append(i1)

def ordem_com(player, inimigo):

    vel_P = Stats_Base.Guerreiro.stats['Velocidade']
    vel_I = Stats_Base.Lobo.stats_inimigo['Velocidade']
    
    if vel_I > vel_P:
        ordem = [inimigo, player]
    else:
        ordem = [player, inimigo]

    return ordem

class Ataque:
    player = Stats_Base.Guerreiro
    inimigo = Stats_Base.Lobo
    def player_ataque(self):
        hit = random.randint(0, 100):
        if hit <= player.stats['Força']:
            inimigo.vida -= player.dano
        else:
            inimigo.vida -= random.randint(player.dano/3, player.dano/2)

print player_ataque
# Loop de combate:
# Esse loop serve para rodar os dados de batalha e manter a batalha ativa
# enquanto tanto o inimigo como o heroi têm hp

