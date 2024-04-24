import random
import pygame

from constants import Constants
from main import finestraJoc


class Pilota():
    velocitat = 5
    mida = 5

    def __init__(self, posicio_x, posicio_y, velocitat_x, velocitat_y, color):
        self.posicio_x = posicio_x
        self.posicio_y = posicio_y
        self.velocitat_x = velocitat_x
        self.velocitat_y = velocitat_y
        self.color = color

    def moure(self):
        self.posicio_y += self.velocitat_y
        self.posicio_x += self.velocitat_x

    def rebota_vertical(self):
        self.velocitat_y = -self.velocitat_y

    def rebota_horitzontal(self):
        self.velocitat_x = -self.velocitat_x
        self.velocitat_x += 1
        self.velocitat_y += 1

    def colision_jugador(self, jugador):
        return (jugador.posX + 10 >= self.posicio_x >= jugador.posX and
                self.posicio_y >= jugador.posY and self.posicio_y <= jugador.posY + 40)

    def reiniciar(self):
        self.posicio_x = Constants.AMPLE_ESCENARI // 2
        self.posicio_y = Constants.ALCADA_ESCENARI // 2
        self.velocitat_x = Pilota.velocitat
        self.velocitat_y = Pilota.velocitat * random.choice([-1, 1])

    def pinta(self):
        pygame.draw.circle(finestraJoc, self.color, (self.posicio_x, self.posicio_y), Pilota.mida)