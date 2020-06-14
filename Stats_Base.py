import pygame

level_inicial = 1
level_up = False

class Heroi:

    ''' Classe usada para guardar as informações dos personagens'''
    
    def stats_classe(self, classe):
        self.nome = "Kléber"
        self.classe = classe
        if  classe == 'Guerreiro':
            stats = {'Força': 75, 'Velocidade': 55, 'Mentais': 40, \
                'Vitalidade': 75}
            self.armadura = stats['Força']*0.2
            self.res_mag = stats['Mentais']*0
            self.esquiva = stats['Velocidade']*0.2
            self.ataque_hit = stats['Força']
        return stats
    
    def __init__(self, classe):
        self.classe = classe
        self.stats = self.stats_classe(self.classe)
        self.level = level_inicial
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2))\
             + 5*self.level
        self.dano = 10 + 5*self.level
        self.vida_variavel = self.vida
        self.xp = 0

        self.state = "NEUTRO"


        
    def Update(self):
        if level_up == True:
            self.level += 1
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2))\
             + 5*self.level
        self.dano = 7 + 5*self.level
        # self.armadura = self.armadura + armadura_bonus
        # self.res_mag = self.res_mag + res_mag_bonus
        # self.esquiva = self.esquiva + esquiva_esquiva
        level_up = False


class Inimigo:
    def stats_inimigo(self, inimigo):
        self.classe = inimigo
        if  self.classe == 'Lobo Cinzento':
            self.nome = "Jorge"
            stats = {'Força': 65, 'Velocidade': 60, 'Mentais': 10, \
                'Vitalidade': 30}
            self.level = level_inicial
            self.dano = 2 + 3*self.level
            self.armadura = stats['Força']*0.1*self.level/2
            self.res_mag = stats['Mentais']*0.05*self.level/2
            self.esquiva = stats['Velocidade']*0.2*self.level/2
            self.ataque_hit = stats['Força']
            self.xp = 25
        return stats
    
    def __init__(self, inimigo):
        self.classe = inimigo
        self.stats = self.stats_inimigo(self.classe)
        self.vida = (self.stats['Vitalidade']*0.2*(self.level/2))\
             + 5*self.level
        self.dano = 10 + 5*self.level
        self.vida_variavel = self.vida
        

        self.state = "NEUTRO"

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