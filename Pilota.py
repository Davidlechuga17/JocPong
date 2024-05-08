import random

from ObjecteEscenari import ObjecteEscenari
from constants import Constants

class Pilota(ObjecteEscenari):
    velocitat = 5
    mida = 5

    def __init__(self, posX, posY, velocitat_x, velocitat_y, color):
        self.posX = posX
        self.posY = posY
        self.velocitat_x = velocitat_x
        self.velocitat_y = velocitat_y
        self.color = color

    def moure(self):
        self.posY += self.velocitat_y
        self.posX += self.velocitat_x

    def rebota_vertical(self):
        self.velocitat_y = -self.velocitat_y

    def rebota_horitzontal(self):
        self.velocitat_x = -self.velocitat_x
        self.velocitat_x += 1

    def colision_jugador(self, jugador):
        return (jugador.posX + 10 >= self.posX >= jugador.posX and
                self.posY >= jugador.posY and self.posY <= jugador.posY + 40)

    def reiniciar(self):
        self.posX = Constants.AMPLE_ESCENARI // 2
        self.posY = Constants.ALCADA_ESCENARI // 2
        self.velocitat_x = Pilota.velocitat
        self.velocitat_y = Pilota.velocitat * random.choice([-1, 1])

