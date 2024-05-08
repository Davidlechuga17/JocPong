
from ObjecteEscenari import ObjecteEscenari
from constants import Constants



class Jugador(ObjecteEscenari):

    def __init__(self, posX, posY, color, vel, punts=0):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.vel = vel
        self.punts = punts

    def MovimentJugador1(teclas, pygame, jugador1):
        if teclas[pygame.K_w] and jugador1.posY>Constants.POSICIO_MARGE_DE_DALT[3]:
            jugador1.posY -= jugador1.vel

        if teclas[pygame.K_s] and jugador1.posY<Constants.ALCADA_ESCENARI-Constants.POSICIO_MARGE_DE_BAIX[3]-41:
            jugador1.posY += jugador1.vel

    def MovimentJugador2(teclas, pygame, jugador2):
        if teclas[pygame.K_UP] and jugador2.posY>Constants.POSICIO_MARGE_DE_DALT[3]:
            jugador2.posY -= jugador2.vel

        if teclas[pygame.K_DOWN] and jugador2.posY<Constants.ALCADA_ESCENARI-Constants.POSICIO_MARGE_DE_BAIX[3]-41:
            jugador2.posY += jugador2.vel
