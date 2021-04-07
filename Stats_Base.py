import pygame
import random
import SuperclasseEntidade

level_inicial = 1

class Heroi(SuperclasseEntidade.Entidade):

    ''' Classe usada para guardar as informações dos personagens'''
    
    def __init__(self):
        super().__init__('Guerreiro')
        self.nome = 'Kléber'
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2)) + 5*self.level
        self.dano = 7 + 5*self.level
        self.heal = self.stats['Mentais']*(0.1*self.level)
        self.vida_variavel = self.vida
        self.xp = 0

    def Update(self):
        if self.level_up == True:
            self.level += 1
            self.xp = 0
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2)) + 5*self.level
        self.vida_variavel = self.vida
        self.dano = 7 + 5*self.level
        self.heal = self.stats['Mentais']*(0.1*self.level)
        self.level_up = False

    def restart(self):
        self.level = level_inicial
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2)) + 5*self.level
        self.dano = 7 + 5*self.level
        self.vida_variavel = self.vida
        self.xp = 0
        self.level_up = False

        


class Inimigo(SuperclasseEntidade.Entidade):    

    def __init__(self):
        super().__init__('Lobo Cinzento')
        lista_nomes = ['Jorge', 'Josué', 'Jeremias', 'Jureg']
        self.novo_nome = random.choice(lista_nomes)
        self.nome = self.novo_nome
        self.vida = (self.stats['Vitalidade']*0.3*(self.level/2)) + 5*self.level
        self.dano = 6 + 4*self.level
        self.vida_variavel = self.vida
        self.level = level_inicial
        self.esquiva = self.stats['Velocidade']*0.2*self.level/2
        self.ataque_hit = self.stats['Força']
        self.xp = 25

        self.state = "NEUTRO"

    def Update(self, level):
        self.level = level
        self.vida = (self.stats['Vitalidade']*0.35*(self.level/2)) + 5*self.level
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
    Guerreiro = Heroi()
    Lobo = Inimigo()  
    return [Guerreiro, Lobo]

'''Essas linhas de código servem para testar se os atributos estão 
funcionando como esperado, permitindo uma visão interna do que 
o código guarda como argumentos'''

# Guerreiro, Lobo = create()
# print(Guerreiro.nome)
# print(Lobo.nome)
# print(Guerreiro.classe)