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
    pygame.draw.rect(finestraJoc, Constants.COLOR_J1, (jugador1.posX, jugador1.posY, 10, 40))
    pygame.draw.rect(finestraJoc, Constants.COLOR_J2, (jugador2.posX, jugador2.posY, 10, 40))

def DetectaEvents(jugador1, jugador2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event per tancar la finestra amb el botó de tancar finestres del sistema.
            sys.exit()  # fa falta afegir un import sys

    teclas =  pygame.key.get_pressed()

    Constants.MovimentJugador1(teclas, pygame, jugador1)

    Constants.MovimentJugador2(teclas, pygame, jugador2)

from Jugador import jugador

jugador1 = jugador(posX=10, posY=180, color=Constants.COLOR_J1, vel=5)
jugador2 = jugador(posX=580, posY=180, color=Constants.COLOR_J2, vel=5)

while not gameOver:

    pintaObjectes()

    DetectaEvents(jugador1, jugador2)

    rellotge.tick(30)
    pygame.display.update()