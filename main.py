import sys
import pygame
from constants import Constants
from Pilota import Pilota
from Jugador import Jugador

pygame.init()

finestraJoc = pygame.display.set_mode((Constants.AMPLE_ESCENARI, Constants.ALCADA_ESCENARI))
rellotge = pygame.time.Clock()

pilota = Pilota(300, 200, 14, 14, (255, 255, 255))

jugador1 = Jugador(posX=10, posY=180, color=Constants.COLOR_J1, vel=7, punts=0)
jugador2 = Jugador(posX=580, posY=180, color=Constants.COLOR_J2, vel=7, punts=0)

fontText = pygame.font.SysFont("monospace", 25)

gameOver = False

def pintaObjectes():
    finestraJoc.fill(Constants.VERD)
    pygame.draw.rect(finestraJoc, Constants.BLAU, Constants.POSICIO_MARGE_DE_DALT)
    pygame.draw.rect(finestraJoc, Constants.BLAU, Constants.POSICIO_MARGE_DE_BAIX)

    pygame.draw.rect(finestraJoc, jugador1.color, (jugador1.posX, jugador1.posY, 10, 40))
    pygame.draw.rect(finestraJoc, jugador2.color, (jugador2.posX, jugador2.posY, 10, 40))

    pygame.draw.circle(finestraJoc, pilota.color, (pilota.posX, pilota.posY), Pilota.mida)

    textJugador1 = "Jugador 1: "+str(jugador1.punts)+" punts"
    textJugador2 = "Jugador 2: "+str(jugador2.punts)+ " punts"

    etiquetaJugador1 = fontText.render(textJugador1, 1, (255, 0, 0))
    etiquetaJugador2 = fontText.render(textJugador2, 1, (255, 0, 0))

    finestraJoc.blit(etiquetaJugador1, (0, 10))
    finestraJoc.blit(etiquetaJugador2, (310, 360))

def DetectaEvents(jugador1, jugador2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    teclas = pygame.key.get_pressed()

    Jugador.MovimentJugador1(teclas, pygame, jugador1)
    Jugador.MovimentJugador2(teclas, pygame, jugador2)

while not gameOver:
    pintaObjectes()
    DetectaEvents(jugador1, jugador2)

    if pilota.colision_jugador(jugador1) or pilota.colision_jugador(jugador2):
        pilota.rebota_horitzontal()

    # Actualitza la posició de la pilota
    pilota.moure()

    # Rebota a les vores superior i inferior
    if pilota.posY <= 15:
        pilota.rebota_vertical()

    if pilota.posY >= Constants.ALCADA_ESCENARI - 15:
        pilota.rebota_vertical()


    if pilota.posX <= 0:
        jugador2.punts += 1
        pilota.reiniciar()

    if pilota.posX >= Constants.AMPLE_ESCENARI:
        jugador1.punts += 1
        pilota.reiniciar()

    rellotge.tick(30)
    pygame.display.update()