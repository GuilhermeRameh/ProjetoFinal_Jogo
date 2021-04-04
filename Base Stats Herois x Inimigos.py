import pygame
level_inicial = 1
level_up = False

# armadura_bonus = 0
# res_mag_bonus = 0
# esquiva = 0
class Heroi:
    ''' Classe usada para guardar as informações dos personagens'''
    
    def stats_classe(self, classe):
        self.classe = classe
        if  classe == 'Guerreiro':
            stats = {'Força': 75, 'Velocidade': 55, 'Mentais': 40, \
                'Vitalidade': 75}
            self.armadura = stats['Força']*0.2
            self.res_mag = stats['Mentais']*0
            self.esquiva = stats['Velocidade']*0.2
        return stats
    
    def __init__(self, classe):
        self.classe = classe
        self.stats = self.stats_classe(self.classe)
        self.level = level_inicial
        self.vida = (self.stats['Vitalidade']*0.2*(self.level/2))\
             + 5*self.level

    def Update(self):
        if level_up == True:
            self.level += 1
        self.vida = (self.stats['Vitalidade']*0.2*(self.level/2))\
             + 5*self.level
        # self.armadura = self.armadura + armadura_bonus
        # self.res_mag = self.res_mag + res_mag_bonus
        # self.esquiva = self.esquiva + esquiva_esquiva
        level_up = False

Guerreiro = Heroi('Guerreiro')
hero_level = Guerreiro.level


class Inimigo:
    def stats_inimigo(self, inimigo):
        self.inimigo = inimigo
        if  inimigo == 'Lobo Cinzento':
            stats = {'Força': 65, 'Velocidade': 60, 'Mentais': 10, \
                'Vitalidade': 30}
        return stats
    
    def __init__(self, inimigo):
        self.inimigo = inimigo
        self.stats = self.stats_inimigo(self.inimigo)
        self.level = level_inicial
        self.vida = (self.stats['Vitalidade']*0.2*(self.level/2))\
             + 5*self.level
        self.armadura = self.stats['Força']*0.1*self.level/2
        self.res_mag = self.stats['Mentais']*0.05*self.level/2
        self.esquiva = self.stats['Velocidade']*0.2*self.level/2

Lobo = Inimigo('Lobo Cinzento')

'''Essas linhas de código servem para testar se os atributos estão 
funcionando como esperado, permitindo uma visão interna do que 
o código guarda como argumentos'''

print(Guerreiro.armadura)
print(Guerreiro.res_mag)
print(Guerreiro.esquiva)
print('\n')
print(Lobo.level)
print(Lobo.armadura)
print(Lobo.res_mag)
print(Lobo.esquiva)