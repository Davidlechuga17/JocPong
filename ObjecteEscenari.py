import pygame

import main
from main import finestraJoc


class ObjecteEscenari:

    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color

    def pinta(self):
        pygame.draw.rect(finestraJoc, self.color, (self.posX, self.posY, 10, 40))
