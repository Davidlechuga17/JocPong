import sys
import pygame
from constants import Constants
from Pilota import Pilota
from Jugador import Jugador

pygame.init()

finestraJoc = pygame.display.set_mode((Constants.AMPLE_ESCENARI, Constants.ALCADA_ESCENARI))
rellotge = pygame.time.Clock()

pilota = Pilota(300, 200, 10, 10, (255, 255, 255))

jugador1 = Jugador(posX=10, posY=180, color=Constants.COLOR_J1, vel=5)
jugador2 = Jugador(posX=580, posY=180, color=Constants.COLOR_J2, vel=5)

gameOver = False


def pintaObjectes():
    finestraJoc.fill(Constants.VERD)
    pygame.draw.rect(finestraJoc, Constants.BLAU, Constants.POSICIO_MARGE_DE_DALT)
    pygame.draw.rect(finestraJoc, Constants.BLAU, Constants.POSICIO_MARGE_DE_BAIX)

    #pygame.draw.rect(finestraJoc, jugador1.color, (jugador1.posX, jugador1.posY, 10, 40))
    #pygame.draw.rect(finestraJoc, jugador2.color, (jugador2.posX, jugador2.posY, 10, 40))

    #pygame.draw.circle(finestraJoc, pilota.color, (pilota.posicio_x, pilota.posicio_y), Pilota.mida)

def DetectaEvents(jugador1, jugador2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    teclas = pygame.key.get_pressed()

    Jugador.MovimentJugador1(teclas, pygame, jugador1)
    Jugador.MovimentJugador2(teclas, pygame, jugador2)

while not gameOver:
    pintaObjectes()
    jugador1.pinta()
    jugador2.pinta()
    pilota.pinta()
    DetectaEvents(jugador1, jugador2)

    if pilota.colision_jugador(jugador1) or pilota.colision_jugador(jugador2):
        pilota.rebota_horitzontal()

    # Actualitza la posició de la pilota
    pilota.moure()

    # Rebota a les vores superior i inferior
    if pilota.posicio_y <= 15:
        pilota.rebota_vertical()

    if pilota.posicio_y >= Constants.ALCADA_ESCENARI - 15:
        pilota.rebota_vertical()

    # Rebota a los bordes izquierdo y derecho del escenario
    if pilota.posicio_x <= 0 or pilota.posicio_x >= Constants.AMPLE_ESCENARI:
        pilota.reiniciar()

    rellotge.tick(30)
    pygame.display.update()