import sys

import pygame

from constants import Constants



pygame.init()

finestraJoc = pygame.display.set_mode((Constants.AMPLE_ESCENARI, Constants.ALCADA_ESCENARI))
rellotge = pygame.time.Clock()

gameOver = False

def pintaObjectes():

    finestraJoc.fill(Constants.VERD)
    pygame.draw.rect(finestraJoc, Constants.BLAU, Constants.POSICIO_MARGE_DE_DALT)
    pygame.draw.rect(finestraJoc, Constants.BLAU, Constants.POSICIO_MARGE_DE_BAIX)
    pygame.draw.rect(finestraJoc, Constants.COLOR_J1, Constants.POSICIOJ1)
    pygame.draw.rect(finestraJoc, Constants.COLOR_J2, Constants.POSICIOJ2)

def DetectaEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event per tancar la finestra amb el botó de tancar finestres del sistema.
            sys.exit()  # fa falta afegir un import sys

    teclas =  pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        jugador1.posY + jugador1.vel/2

    if teclas[pygame.K_s]:
        jugador1.posY - jugador1.vel/2

    if teclas[pygame.K_UP]:
        jugador2.posY + jugador2.vel/2

    if teclas[pygame.K_DOWN]:
        jugador2.posY - jugador2.vel/2


from Jugador import jugador

jugador1 = jugador(posX=5, posY=20, color=Constants.COLOR_J1, vel=5)
jugador2 = jugador(posX=10, posY=40, color=Constants.COLOR_J2, vel=5)

while not gameOver:

    pintaObjectes()

    DetectaEvents()

    rellotge.tick(30)
    pygame.display.update()



