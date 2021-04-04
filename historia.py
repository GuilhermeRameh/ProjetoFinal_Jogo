import pygame
import Setup
import RunSprites as spr

iniciar = Setup.iniciar
janela = Setup.janela

linha1=iniciar.render('Você é o nobre guerreiro Kleber.',1,(255,255,255))
linha3=iniciar.render('se alojou em uma caverna.',1,(255,255,255))
linha2=iniciar.render('Em meio a uma missão',1,(255,255,255))
linha4=iniciar.render('O que você não esperava',1,(255,255,255))
linha5=iniciar.render('era que essa caverna era habitada',1,(255,255,255))
linha6=iniciar.render('por lobos que não exitaram em matar.',1,(255,255,255))
linha7=iniciar.render('Sua nova missão é SOBREVIVER!',1,(255,255,255))
linha8=iniciar.render('Porém tome cuidado! Entre eles está Jeremias, o(a) Sanguinário!',1,(255,255,255))


def historia1():
    janela.blit(spr.hist1, [0,0])
    janela.blit(linha1,(220,400))
    

def historia2():
    janela.blit(spr.hist2, [0,0])
    janela.blit(linha2,(20,100))
    janela.blit(linha3,(20,130))
    
def historia3():
    janela.blit(spr.hist3, [0,0])
    janela.blit(linha4,(390,300))
    janela.blit(linha5,(390,330))
    janela.blit(linha6,(390,360))
    janela.blit(linha7,(390,390))

def historia4():
    janela.fill((0,0,0))
    janela.blit(linha8, (100, 180))
