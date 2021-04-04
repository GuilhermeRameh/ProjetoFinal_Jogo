import pygame
import random

level_inicial = 1

class Heroi:

    ''' Classe usada para guardar as informações dos personagens'''
    
    def stats_classe(self, classe):
        self.nome = "Kléber"
        self.classe = classe
        if  classe == 'Guerreiro':
            stats = {'Força': 65, 'Velocidade': 55, 'Mentais': 40, \
                'Vitalidade': 65}
            self.esquiva = stats['Velocidade']*0.2
            self.ataque_hit = stats['Força']
            
        return stats
    
    def __init__(self, classe):
        self.classe = classe
        self.stats = self.stats_classe(self.classe)
        self.level = level_inicial
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2))\
             + 5*self.level
        self.dano = 7 + 5*self.level
        self.heal = self.stats['Mentais']*(0.1*self.level)
        self.vida_variavel = self.vida
        self.xp = 0
        self.level_up = False

        self.state = "NEUTRO"        
        
    def Update(self):
        if self.level_up == True:
            self.level += 1
            self.xp = 0
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2))\
             + 5*self.level
        self.vida_variavel = self.vida
        self.dano = 7 + 5*self.level
        self.heal = self.stats['Mentais']*(0.1*self.level)
        self.level_up = False

    def restart(self):
        self.level = level_inicial
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2))\
             + 5*self.level
        self.dano = 7 + 5*self.level
        self.vida_variavel = self.vida
        self.xp = 0
        self.level_up = False

        


class Inimigo:
    def stats_inimigo(self, inimigo):
        self.classe = inimigo
        if  self.classe == 'Lobo Cinzento':
            lista_nomes = ['Jorge', 'Josué', 'Jeremias', 'Jureg']
            self.novo_nome = random.choice(lista_nomes)
            self.nome = self.novo_nome
            stats = {'Força': 60, 'Velocidade': 60, 'Mentais': 10, \
                'Vitalidade': 50}
            self.level = level_inicial
            self.esquiva = stats['Velocidade']*0.2*self.level/2
            self.ataque_hit = stats['Força']
            self.xp = 25
        return stats
    
    def __init__(self, inimigo):
        self.classe = inimigo
        self.stats = self.stats_inimigo(self.classe)
        self.vida = (self.stats['Vitalidade']*0.3*(self.level/2))\
             + 5*self.level
        self.dano = 6 + 4*self.level
        self.vida_variavel = self.vida

        self.state = "NEUTRO"

    def Update(self, level):
        self.level = level
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2))\
            + 5*self.level
        self.vida_variavel = self.vida
        self.dano = 6 + 4*self.level
        lista_nomes = ['Jorge', 'Josué', 'Jeremias', 'Jureg']
        self.novo_nome = random.choice(lista_nomes)
        self.nome = self.novo_nome

    def restart(self, level):
        self.vida_variavel = self.vida
        self.level = level
        lista_nomes = ['Jorge', 'Josué', 'Jeremias', 'Jureg']
        self.novo_nome = random.choice(lista_nomes)
        self.nome = self.novo_nome



def create():
    Guerreiro = Heroi('Guerreiro')
    Lobo = Inimigo('Lobo Cinzento')  
    return [Guerreiro, Lobo]

'''Essas linhas de código servem para testar se os atributos estão 
funcionando como esperado, permitindo uma visão interna do que 
o código guarda como argumentos'''

# print(Guerreiro.armadura)
# print(Guerreiro.res_mag)
# print(Guerreiro.esquiva)
# print('\n')
# print(Lobo.level)
# print(Lobo.armadura)
# print(Lobo.res_mag)
# print(Lobo.esquiva)