import random

import pygame


class Pilota():
    velocitat = 10
    mida = 5
    def __init__(self, posicio_x, posicio_y, velocitat_x, velocitat_y, color):
        self.posicio_x = posicio_x
        self.posicio_y = posicio_y
        self.velocitat_x = velocitat_x
        self.velocitat_y = velocitat_y
        self.color = color

    def actualitza(self, ample_pantalla, alt_pantalla, jugador_esquerra, jugador_dreta):
        self.posicio_x += self.velocitat_x
        self.posicio_y += self.velocitat_y

        if self.posicio_y <= 0 or self.posicio_y >= alt_pantalla:
            self.velocitat_y *= -1

        if self.posicio_x <= 0:
            if jugador_esquerra.y < self.posicio_y < jugador_esquerra.y + jugador_esquerra.altura:
                self.velocitat_x *= -1
                self.velocitat += 1
            else:
                self.__reinicia(ample_pantalla // 2, alt_pantalla // 2)

        if self.posicio_x >= ample_pantalla:
            if jugador_dreta.y < self.posicio_y < jugador_dreta.y + jugador_dreta.altura:
                self.velocitat_x *= -1
                self.velocitat += 1
            else:
                self.__reinicia(ample_pantalla // 2, alt_pantalla // 2)

    def __reinicia(self, posicio_x, posicio_y):
        self.posicio_x = posicio_x
        self.posicio_y = posicio_y
        self.velocitat = Pilota.velocitat
        self.velocitat_x = self.velocitat * random.choice([-1, 1])
        self.velocitat_y = self.velocitat * random.choice([-1, 1])

    def pinta(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (self.posicio_x, self.posicio_y), Pilota.mida)