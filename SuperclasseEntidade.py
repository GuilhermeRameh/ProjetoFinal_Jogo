'''
    Esse Documento servirá como uma Super classe tanto da classe Herói como da classe
    Inimigo, pois elas possuem diversas características em comum e será mais eficaz
    se unirmos as duas sob uma mesma Super classe
'''

import pygame
import random

level_inicial = 1

class Entidade:

    '''Classe utilizada como base tanto da classe Herói como da classe Inimigo'''

    def stats_classe(self, classe):
        if  classe == 'Guerreiro':
            stats = {'Força': 65, 'Velocidade': 55, 'Mentais': 40, 'Vitalidade': 65} 
        elif classe == 'Lobo Cinzento':
            stats = {'Força': 60, 'Velocidade': 60, 'Mentais': 10, 'Vitalidade': 50}

        return stats

    def __init__(self, classe):
        self.classe = classe
        self.stats = self.stats_classe(self.classe)
        self.level = level_inicial
        self.esquiva = self.stats['Velocidade']*0.2
        self.ataque_hit = self.stats['Força']
        self.level_up = False

        self.state = "NEUTRO"

'''
Como apenas a inicialização e os stats das classes eram
parecidos, decidimos puxar estes parametros em uma superclasse e
deixar tanto o método Update como o método Restart como individuais de cada classe
'''